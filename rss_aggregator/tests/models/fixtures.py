# rss-aggregator (c) pubgem
from ... import models
import datetime


def typical_rss_feed():
    return models.RSSFeed.find_or_create(
            name="Generic Feed",
            rss_url="https://www.genericfeed.com/feed.xml",
        )


def typical_rss_entry():
    return models.RSSEntry.find_or_create(
            title="Generic Entry",
            doi="10.1000/123456",
            date=datetime.datetime(12, 12, 12, 12, 12, 12),
        )
