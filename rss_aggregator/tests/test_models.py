# -*- coding: utf-8 -*-
# rss-aggregator (c) pubgem

from nose.plugins.attrib import attr
from flask.ext.testing import TestCase
from flask.ext.diamond.mixins.testing import DiamondTestCaseMixin
from .. import models


class UserTestCase(DiamondTestCaseMixin, TestCase):
    "Coverage for User Model"

    def test_create(self):
        "ensure an account can be created"
        models.User.create(email='an_account', password='a_password')
        an_account = models.User.find(email='an_account')
        assert an_account
        assert an_account.email == 'an_account'
