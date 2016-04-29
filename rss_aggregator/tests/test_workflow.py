# -*- coding: utf-8 -*-
# rss-aggregator (c) pubgem

from nose.plugins.attrib import attr
from .mixins import DiamondTestCase
from .fixtures import typical_workflow
from ..models import User


class WorkflowTestCase(DiamondTestCase):
    def setUp(self):
        super(WorkflowTestCase, self).setUp()
        typical_workflow()

    # @attr("single")
    def test_user(self):
        "user created in typical_workflow during setUp"
        u = User.find(email='guest')
        assert u
        assert u.email == 'guest'
