# rss-aggregator (c) pubgem
from . import models


class RSSWatcher:
    """
    RSSWatcher checks for new entries in a journal's RSS feed and commits them to the database.
    """

    # def __init__(self):
    #     """
    #     Watcher class network and authentication configuration.
    #     """
    #     pass

    def watch(self):
        """
        Iterates through all of the RSSFeeds.
        """
        all_rss_feeds = [feed for feed in models.RSSFeed.query.all()]

        for rss_feed in all_rss_feeds:
            rss_feed.aggregate()
