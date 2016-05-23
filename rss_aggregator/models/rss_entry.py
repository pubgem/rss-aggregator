# rss-aggregator (c) pubgem
from flask.ext.diamond.mixins.crud import CRUDMixin
from flask.ext.diamond.mixins.marshmallow import MarshmallowMixin
from flask.ext.diamond import ma, db
from ..utils import parse_rss_timestamp


class RSSEntrySchema(ma.Schema):
    class Meta:
        additional = (
            "raw_xml",
            "date",
            "doi",
            "authors",
            "title",
            "issue",
            "volume",
            "pages",
            "www",
            "rss_feed_id",
        )


class RSSEntry(db.Model, CRUDMixin, MarshmallowMixin):
    __schema__ = RSSEntrySchema

    id = db.Column(db.Integer(), primary_key=True)

    raw_xml = db.Column(db.Text)
    date = db.Column(db.DateTime)
    doi = db.Column(db.Text)

    authors = db.Column(db.Text)  # TODO: Data structure beyond just a string?
    title = db.Column(db.Text)
    summary = db.Column(db.Text)
    issue = db.Column(db.Integer)
    volume = db.Column(db.Integer)
    pages = db.Column(db.Integer)
    www = db.Column(db.Text)

    rss_feed = db.relationship('RSSFeed', backref=db.backref('rss_entry', lazy='dynamic'))
    rss_feed_id = db.Column(db.Integer, db.ForeignKey("rss_feed.id"))

    @classmethod
    def checkin_rss_entry(cls, rss_feed, entry, **kwargs):
        """
        Checks in an RSS Entry from an RSS feed.

        :param rss_feed: models.RSSFeed object

        :param entry: models.RSSFeed object
        """
        # import ipdb; ipdb.set_trace()

        return cls.create(
            rss_feed=rss_feed,

            # raw_xml=entry[''],  # TODO: Get raw XML from feedparser!
            doi=entry.dc_identifier,
            date=parse_rss_timestamp(entry.updated_parsed),

            title=entry.title,
            authors=entry.author,
            www=entry.link,
            summary=entry.summary,
        )


# class RSSEntrySchema(ma.ModelSchema):
#     class Meta:
#         model = RSSEntry
