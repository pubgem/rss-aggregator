# rss-aggregator (c) pubgem

from nose.plugins.attrib import attr
from ..mixins import DiamondTestCase
from ... import models
from ... import db
from . import fixtures
import datetime


class RSSEntryTestCase(DiamondTestCase):
    "Coverage for models.RSSEntry"

    def setUp(self):
        db.drop_all()
        db.create_all()

    # @attr('single')
    def test_create(self):
        "Testing rss_aggregator.models.RSSEntry.create"
        models.RSSEntry.create(
            title="Generic Entry",
            doi="10.1000/123456",
            date=datetime.datetime(12, 12, 12, 12, 12, 12),
        )
        retrieved = models.RSSEntry.find(title="Generic Entry")
        self.assertIsNotNone(retrieved, "Object retrievible.")

    # @attr('single')
    def test_read(self):
        "Testing rss_aggregator.models.RSSEntry.find"
        retrieved = fixtures.typical_rss_entry()
        self.assertEquals(retrieved.doi, "10.1000/123456", "Attributes readable.")

    # @attr('single')
    def test_update(self):
        "Testing rss_aggregator.models.RSSEntry.update"
        retrieved = fixtures.typical_rss_entry()

        new_attribute = "Generic Entry 2"
        retrieved.update(title=new_attribute)

        retrieved = models.RSSEntry.find(doi="10.1000/123456")
        self.assertEquals(retrieved.title, new_attribute, "Attributes updated.")

    # @attr('single')
    def test_delete(self):
        "Testing rss_aggregator.models.RSSEntry.delete"
        retrieved = fixtures.typical_rss_entry()
        self.assertIsNotNone(retrieved, "Object retrievible.")

        retrieved.delete()

        retrieved = models.RSSEntry.find(title="Generic Entry")
        self.assertIsNone(retrieved, "Object deleted.")
