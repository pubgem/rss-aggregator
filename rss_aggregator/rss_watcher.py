# rss-aggregator (c) pubgem
import feedparser


class RSSWatcher:
    """
    RSSWatcher checks for new entries in a journal's RSS feed and commits them to the database.
    """

    def watch(self):
        """
        Iterates through all of the RSSFeeds.

        :param :
        :type :
        """
        pass

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
