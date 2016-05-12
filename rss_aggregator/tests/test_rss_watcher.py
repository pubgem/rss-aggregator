# rss-aggregator (c) pubgem

from . mixins import DiamondTestCase
from .. import models
from ..rss_watcher import RSSWatcher
from .. import db
from . import fixtures
import datetime
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

    @attr('single')
    def test_watch(self):
        "Testing RSSWatcher.watch"
        # import ipdb; ipdb.set_trace()
        self.rss_watcher.watch()
