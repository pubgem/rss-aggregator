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
        models.User.add_guest_user()

    # @attr('single')
    def test_subscribe(self):
        "Testing models.User.subscribe"
        user = models.User.find(name="guest", email="guest@example.com")
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

    @attr('single')
    def test_unsubscribe(self):
        "Testing models.User.unsubscribe"
        user = models.User.find(name="guest", email="guest@example.com")
        rss_feed1 = fixtures.typical_rss_feed()
        rss_feed2 = models.RSSFeed.find_or_create(
            name="Generic Feed2",
            rss_url="https://www.genericfeed2.com/feed.xml")
        user.subscribe(rss_feed1, rss_feed2)
        self.assertEqual(len(user.subscriptions), 2, "Subscriptions at 2")

        user.unsubscribe(rss_feed2, rss_feed1)
        self.assertEqual(len(user.subscriptions), 0, "Subscriptions as expected")
