# -*- coding: utf-8 -*-
# rss-aggregator (c) pubgem

from flask.ext.diamond import Diamond, db
from flask.ext.diamond.ext.administration import AdminView, AdminModelView


# declare these globalish objects before initializing models
app_instance = None


# import models after setting up the other objects
from . import models


class rss_aggregator(Diamond):
    def init_administration(self):
        "Initialize admin interface"

        admin = self.super("administration")

        model_list = [
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
    global app_instance
    if not app_instance:
        app_instance = test_app()
        app_instance.init_app(
            extensions=[
                "configuration",
                "logs",
                "database",
                "accounts",
                "blueprints",
                "signals",
                "forms",
                "error_handlers",
                "request_handlers",
                "administration",
                # "rest",
                # "webassets",
                # "email",
                # "debugger",
                # "task_queue",
            ]
        )

    # print app_instance.app.url_map
    return app_instance.app
