# rss-aggregator (c) pubgem

from ..mixins import DiamondTestCase
from ... import db
from ... import models
from . import fixtures
from nose.plugins.attrib import attr


class RSSFeedTestCase(DiamondTestCase):
    "Coverage for models.RSSFeed"

    def setUp(self):
        db.drop_all()
        db.create_all()

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
        retrieved = fixtures.typical_rss_feed()
        self.assertEquals(retrieved.rss_url, "https://www.genericfeed.com/feed.xml", "Attributes readable.")

    # @attr('single')
    def test_update(self):
        "Testing rss_aggregator.models.RSSFeed.update"
        retrieved = fixtures.typical_rss_feed()

        new_attribute = "https://generic.com/feed.xml"
        retrieved.update(rss_url=new_attribute)

        retrieved = models.RSSFeed.find(name="Generic Feed")
        self.assertEquals(retrieved.rss_url, new_attribute, "Attributes updated.")

    # @attr('single')
    def test_delete(self):
        "Testing rss_aggregator.models.RSSFeed.delete"
        retrieved = fixtures.typical_rss_feed()
        self.assertIsNotNone(retrieved, "Object retrievible.")

        retrieved.delete()

        retrieved = models.RSSFeed.find(name="Generic Feed")
        self.assertIsNone(retrieved, "Object deleted.")

    @attr('single')
    def test_schema(self):
        "Testing rss_aggregator.models.RSSFeed.__schema__"
        import marshmallow
        self.assertEquals(
            isinstance(models.RSSEntry.__schema__, marshmallow.schema.SchemaMeta),
            True,
            "Schema declared successfully."
        )
