# rss-aggregator (c) pubgem

from nose.plugins.attrib import attr
from ..mixins import DiamondTestCase
from ... import models
from ... import db


class RSSFeedTestCase(DiamondTestCase):
    "Coverage for models.RSSFeed"

    def setUp(self):
        db.drop_all()
        db.create_all()

    def tearDown(self):
        super().tearDown()

    # @attr('single')
    def test_create(self):
        "Testing rss_aggregator.models.RSSFeed.create"
        models.RSSFeed.create(
            name="Generic Feed",
            rss_url="https://www.genericfeed.com/feed.xml",
        )
        retrieved = models.RSSFeed.find(name="Generic Feed")
        self.assertIsNotNone(retrieved, "Object retrievible.")

    # @attr('single')
    def test_read(self):
        "Testing rss_aggregator.models.RSSFeed.find"
        models.RSSFeed.create(
            name="Generic Feed",
            rss_url="https://www.genericfeed.com/feed.xml",
        )

        retrieved = models.RSSFeed.find(name="Generic Feed")
        self.assertEquals(retrieved.rss_url, "https://www.genericfeed.com/feed.xml", "Attributes readable.")

    # @attr('single')
    def test_update(self):
        "Testing rss_aggregator.models.RSSFeed.update"
        models.RSSFeed.create(
            name="Generic Feed",
            rss_url="https://www.genericfeed.com/feed.xml",
        )

        retrieved = models.RSSFeed.find(name="Generic Feed")
        new_attribute = "null"
        retrieved.update(rss_url=new_attribute)

        retrieved = models.RSSFeed.find(name="Generic Feed")
        self.assertEquals(retrieved.rss_url, new_attribute, "Attributes updated.")

    # @attr('single')
    def test_delete(self):
        "Testing rss_aggregator.models.RSSFeed.delete"
        models.RSSFeed.create(
            name="Generic Feed",
            rss_url="https://www.genericfeed.com/feed.xml",
        )

        retrieved = models.RSSFeed.find(name="Generic Feed")
        self.assertIsNotNone(retrieved, "Object retrievible.")

        retrieved.delete()

        retrieved = models.RSSFeed.find(name="Generic Feed")
        self.assertIsNone(retrieved, "Object deleted.")
