# rss-aggregator (c) pubgem

from nose.plugins.attrib import attr
from ..mixins import DiamondTestCase
from ... import models
from ... import db
from . import fixtures


class RSSEntryTestCase(DiamondTestCase):
    "Coverage for models.RSSEntry"

    def setUp(self):
        db.drop_all()
        db.create_all()
        models.PubgemUser.add_guest_user()

    # @attr('single')
    def test_subscribe(self):
        "Testing models.PubgemUser.subscribe"
        user = models.PubgemUser.find(name="guest", email="guest@example.com")
        rss_feed = fixtures.typical_rss_feed()
        user.subscribe(rss_feed)
        self.assertEquals(len(user.subscriptions), 1, "Subscription addition as expected")

        user.subscribe(rss_feed)
        self.assertEquals(len(user.subscriptions), 1, "Duplicate subscription attempt -- subscription count is the same.")

        new_rss_feed = models.RSSFeed.find_or_create(
            name="Generic Feed2",
            rss_url="https://www.genericfeed2.com/feed.xml")
        user.subscribe(new_rss_feed)
        self.assertEquals(len(user.subscriptions), 2, "Second subscription added")
