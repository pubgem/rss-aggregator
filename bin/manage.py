#!/usr/bin/env python
# -*- coding: utf-8 -*-
# rss-aggregator (c) pubgem

import sys
import traceback
sys.path.insert(0, '.')

from flask.ext.script import Manager, Shell, Server
from flask.ext.migrate import Migrate, MigrateCommand, upgrade
import alembic
import alembic.config
from rss_aggregator import create_app, db
from rss_aggregator.models import User, Role

app = create_app()
migrate = Migrate(app, db, directory="rss_aggregator/migrations")


def _make_context():
    return {
        "app": app,
        "db": db,
    }

manager = Manager(app)
manager.add_command("shell", Shell(make_context=_make_context))
manager.add_command("runserver", Server(port=app.config['PORT']))
manager.add_command("publicserver", Server(port=app.config['PORT'], host="0.0.0.0"))
manager.add_command('db', MigrateCommand)


@manager.option('-e', '--email', help='email address', required=True)
@manager.option('-p', '--password', help='password', required=True)
@manager.option('-a', '--admin', help='make user an admin user', action='store_true', default=None)
def useradd(email, password, admin):
    "add a user to the database"
    if admin:
        roles = ["Admin"]
    else:
        roles = ["User"]
    User.register(
        email=email,
        password=password,
        confirmed=True,
        roles=roles
    )


@manager.option('-e', '--email', help='email address', required=True)
def userdel(email):
    "delete a user from the database"
    obj = User.find(email=email)
    if obj:
        obj.delete()
        print("Deleted")
    else:
        print("User not found")


@manager.option('-m', '--migration',
    help='create database from migrations',
    action='store_true', default=None)
def init_db(migration):
    "drop all databases, instantiate schemas"
    db.drop_all()

    if migration:
        # create database using migrations
        print("applying migration")
        upgrade()
    else:
        # create database from model schema directly
        db.create_all()
        db.session.commit()
        cfg = alembic.config.Config("rss_aggregator/migrations/alembic.ini")
        alembic.command.stamp(cfg, "head")


@manager.command
def populate_db():
    "insert a default set of objects"
    Role.add_default_roles()
    User.add_guest_user()
    User.add_admin_user(password="aaa")

    from rss_aggregator.tests import fixtures
    fixtures.offline_rss_feed()


@manager.command
def rssfeed_add(path):
    """
    Adds RSS Feeds from a JSON file.

    :param path: path to JSON file.
    :type path: str
    """
    from rss_aggregator import models
    with open(path, 'r') as f:
        models.RSSFeed.loadf(f)


@manager.command
def aggregate():
    """
    Invokes the RSS watcher.

    intended to be used with cron every 10 minutes.
    """
    from rss_aggregator.rss_watcher import RSSWatcher
    rss_watcher = RSSWatcher()
    rss_watcher.watch()

if __name__ == "__main__":
    manager.run()
    # try:

    # except Exception as e:
    #     ex_type, ex, tb = sys.exc_info()
    #     traceback.print_tb(tb)
    #     print("Error: %s" % e)
    #     print("Line: %d" % sys.exc_traceback.tb_lineno)
