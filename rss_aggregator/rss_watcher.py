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
        all_rss_feeds = [feed for feed in models.RSSFeed.query.all()]

        for rss_feed in all_rss_feeds:
            self.query_rss(rss_feed)

    def query_rss(self, rss_feed):
        """
        Queries the RSS Feed, checks for a new entry.
        """
        d = feedparser.parse(rss_feed.rss_url)
        import ipdb; ipdb.set_trace()
        for i in d['feed']:
            # Iterate through the feed, check if entry is new
            # If new, call checkin_entry, if not, ignore.
            # How to determine if is new? -> check other RSS aggregators
            pass

    def checkin_entry(self):
        """
        Checks-in a new RSS Entry into the database.
        """
        pass
