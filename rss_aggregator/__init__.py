# -*- coding: utf-8 -*-
# rss-aggregator (c) pubgem

from flask.ext.diamond import Diamond, db
from flask.ext.diamond.facets.administration import AdminModelView
from .models import Role, PubgemUser

# declare global app instance
application = None


class rss_aggregator(Diamond):
    def init_accounts(self):
        "initialize accounts with the User and Role classes imported from .models"
        result = self.super("accounts", user=PubgemUser, role=Role)
        return result

    def init_administration(self):
        "Initialize admin interface"
        admin = self.super("administration", user=PubgemUser, role=Role)

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
        application.facet("configuration")
        application.facet("logs")
        application.facet("database")
        application.facet("marshalling")
        application.facet("accounts")
        application.facet("blueprints")
        application.facet("signals")
        application.facet("forms")
        application.facet("error_handlers")
        application.facet("request_handlers")
        application.facet("administration")
        # application.facet("rest")
        # application.facet("webassets")
        # application.facet("email")
        # application.facet("debugger")
        # application.facet("task_queue")

    # print application.app.url_map
    return application.app
