# rss-aggregator (c) pubgem

from nose.plugins.attrib import attr
from . mixins import DiamondTestCase
from .. import models
from .. import db
from . import fixtures
import datetime


class RSSWatcherTestCase(DiamondTestCase):
    "Coverage for RSSWatcher"

    def setUp(self):
        db.drop_all()
        db.create_all()

        fixtures.offline_rss_feed()
        self.assertIsNotNone(models.RSSFeed.find(**{"name": "Journal of Personality and Social Psychology"}), "Fixture created.")

    @attr('single')
    def test_me(self):
        "Testing test_me"
        self.assertEquals(1+1, 2)
