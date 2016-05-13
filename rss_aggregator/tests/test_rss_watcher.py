# rss-aggregator (c) pubgem

from . mixins import DiamondTestCase
from .. import models
from ..rss_watcher import RSSWatcher
from .. import db
from . import fixtures
from nose.plugins.attrib import attr


class RSSWatcherTestCase(DiamondTestCase):
    "Coverage for RSSWatcher"

    def setUp(self):
        db.drop_all()
        db.create_all()

        fixtures.offline_rss_feed()
        self.assertIsNotNone(models.RSSFeed.find(
            **{"name": "Journal of Personality and Social Psychology"}),
            "Fixture created.")
        self.rss_watcher = RSSWatcher()

    # @attr('single')
    def test_watch(self):
        """
        Testing RSSWatcher.watch
        """
        # Basic RSS retrival test case
        self.rss_watcher.watch()
        rss_feed = fixtures.offline_rss_feed()
        rss_entry_count = len(rss_feed.rss_entry.all())
        self.assertGreater(rss_entry_count, 0, "RSS Entries retrieved")

        # Tests if duplicates are re-entered into system
        self.rss_watcher.watch()
        rss_feed = fixtures.offline_rss_feed()
        new_rss_entry_count = len(rss_feed.rss_entry.all())
        self.assertEquals(new_rss_entry_count, rss_entry_count, "RSS Entries not duplicated")
        # import ipdb; ipdb.set_trace()
