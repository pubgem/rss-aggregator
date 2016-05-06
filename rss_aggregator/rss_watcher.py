# rss-aggregator (c) pubgem
from . import models
import feedparser


class RSSWatcher:
    """
    RSSWatcher checks for new entries in a journal's RSS feed and commits them to the database.
    """

    def watch(self):
        """
        Iterates through all of the RSSFeeds.
        """
        all_rss_feeds = map(
            lambda feed: feed,
            models.RSSFeed.query.all()
        )

        for feed in all_rss_feeds:
            print(feed.name, feed.url)

    def query_rss(self, rss):
        """
        Queries the RSS Feed for a new entry
        """
        feedparser.parse(rss)

    def checkin_entry(self):
        """
        Checks-in a new RSS Entry into the database.
        """
        pass
