# rss-aggregator (c) pubgem


def parse_rss_timestamp(timestamp):
    """
    Parses feedparser's timestamp values (usually given in time.struct_time)

    :type timestamp: time.struct_time
    :returns: datetime.datetime
    """
    import datetime as dt
    return dt.datetime(*timestamp[:7])
