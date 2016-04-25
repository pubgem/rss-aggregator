# -*- coding: utf-8 -*-
# rss-aggregator (c) pubgem

import flask
import flask.ext.security as security
from flask.ext.admin import expose
from flask.ext.diamond.ext.administration import AuthModelView, AdminIndexView

from rss_aggregator import db


adminbaseview = flask.Blueprint('adminbaseview', __name__,
    template_folder='templates', static_folder='static')


class RedirectView(AdminIndexView):
    def is_visible(self):
        return False

    def is_accessible(self):
        return security.current_user.is_authenticated()

    @expose('/')
    def index(self):
        return flask.redirect(flask.url_for('user.list_view'))
