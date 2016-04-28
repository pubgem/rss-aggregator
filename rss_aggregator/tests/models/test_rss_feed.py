# rss-aggregator (c) pubgem

from nose.plugins.attrib import attr
from flask.ext.testing import TestCase
from flask.ext.diamond.mixins.testing import DiamondTestCaseMixin
from ... import models
from ... import db


class RSSFeedTestCase(DiamondTestCaseMixin, TestCase):
    "Coverage for models.RSSFeed"

    def setUp(self):
        db.drop_all()
        db.create_all()

    def tearDown(self):
        super().tearDown()

    @attr('single')
    def test_create(self):
        "Testing rss_aggregator.models.RSSFeed.create"
        rss_feed = models.RSSFeed.create(
            name="Generic Feed",
            rss_url="https://www.genericfeed.com/feed.xml",
        )
        rss_feed = models.RSSFeed.find(rss_feed)
        self.assertIsNotNone(rss_feed, "Object retrievible.")
