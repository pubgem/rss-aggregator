# -*- coding: utf-8 -*-
# rss-aggregator (c) pubgem

from flask.ext.diamond import Diamond, db
from flask.ext.diamond.ext.administration import AdminModelView
from .models import User, Role

# declare global app instance
application = None


class rss_aggregator(Diamond):
    def init_accounts(self):
        "initialize accounts with the User and Role classes imported from .models"
        result = self.super("accounts", user=User, role=Role)
        return result

    def init_administration(self):
        "Initialize admin interface"
        admin = self.super("administration", user=User, role=Role)

        model_list = [
            models.RSSFeed,
            models.RSSEntry,
        ]

        for model in model_list:
            admin.add_view(AdminModelView(
                model,
                db.session,
                name=model.__name__,
                category="Models")
            )

        return admin

    def init_blueprints(self):
        "Application blueprints"

        self.super("blueprints")

        # administration blueprint is custom to this application
        from .views.administration.modelviews import adminbaseview
        self.app.register_blueprint(adminbaseview)


def create_app():
    global application
    if not application:
        application = rss_aggregator()
        application.bootup("configuration")
        application.bootup("logs")
        application.bootup("database")
        application.bootup("marshalling")
        application.bootup("accounts")
        application.bootup("blueprints")
        application.bootup("signals")
        application.bootup("forms")
        application.bootup("error_handlers")
        application.bootup("request_handlers")
        application.bootup("administration")
        # application.bootup("rest")
        # application.bootup("webassets")
        # application.bootup("email")
        # application.bootup("debugger")
        # application.bootup("task_queue")



    # print application.app.url_map
    return application.app
