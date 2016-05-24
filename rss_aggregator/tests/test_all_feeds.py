# rss-aggregator (c) pubgem

from . mixins import DiamondTestCase
from .. import models
from ..rss_watcher import RSSWatcher
from .. import db
from . import fixtures
from nose.plugins.attrib import attr
import os

MODULE_PATH = os.path.split(os.path.realpath(__file__))[0]


class AllFeedsTestCase(DiamondTestCase):
    "Test all feeds"

    def setUp(self):
        db.drop_all()
        db.create_all()

        self.rss_watcher = RSSWatcher()

    def tearDown(self):
        pass  # keep the database

    def test_load_all(self):
        """
        """
        self.rss_watcher.load_list("tests/data/sample_apa_journals.json")
        self.assertEquals(models.RSSFeed.query.count(), 27, "correct number of feeds loaded")

    @attr('skip')
    def test_sciencedirect_feed(self):
        """
        """
        feed = models.RSSFeed.find_or_create(
            **{
                "name": "Journal of Experimental Social Psychology",
                "parser_class": "sciencedirect",
                "rss_url": os.path.join(MODULE_PATH, "data/00221031.rss"),
            }
        )
        print(feed)
        feed.aggregate()
        print(models.RSSEntry.query.count())
        assert(False)

    # @attr('single', 'online')
    def test_individual_feeds(self):
        self.rss_watcher.load_list("tests/data/sample_apa_journals.json")

        for feed in models.RSSFeed.query.all():
            print(feed.rss_url)
            feed.aggregate()
            print(models.RSSEntry.query.count())

        assert False

    @attr("skip")
    def skipping(self):
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
