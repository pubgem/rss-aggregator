# rss-aggregator (c) pubgem


def parse_rss_timestamp(self, timestamp):
    """
    Parses feedparser's timestamp values (usually given in time.struct_time)

    :type timestamp: time.struct_time
    :returns: datetime.datetime
    """
    from datetime import dt
    return dt.datetime(*timestamp[:7])
