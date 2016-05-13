# rss-aggregator (c) pubgem
from .. import db
from . import RSSEntry
from ..utils import parse_rss_timestamp
from flask.ext.diamond.mixins.crud import CRUDMixin
from flask.ext.diamond.mixins.marshmallow import MarshmallowMixin
from flask.ext.diamond import ma
import feedparser


class RSSFeedSchema(ma.Schema):
    class Meta:
        # RegEx to help transform args to tuple: ^(\w+) =.*
        additional = (
            "name",
            "rss_url",
            "doi",
            "parser_class",
            "www",
            "issn",
            "isbn",
            "publisher",
        )


class RSSFeed(db.Model, CRUDMixin, MarshmallowMixin):
    id = db.Column(db.Integer(), primary_key=True)

    name = db.Column(db.String(50))
    rss_url = db.Column(db.String(150))
    doi = db.Column(db.String(50))
    parser_class = db.Column(db.String(15))

    www = db.Column(db.String(50))
    issn = db.Column(db.String(25))
    isbn = db.Column(db.String(25))
    publisher = db.Column(db.String(50))
    summary = db.Column(db.Text)

    def aggregate(self):
        """
        Queries the RSS Feed, checks for a new entry, and checks-in new entry.
        """
        d = feedparser.parse(self.rss_url)
        # self.parse_timestamp(d.feed['updated_parsed'])  # used in later optimization
        for i in d['entries']:
            # Iterate through the feed, check if entry already exists
            existing_entry = self.rss_entry.filter_by(
                title=i.title,
                date=parse_rss_timestamp(i.updated_parsed)).all()
            if not existing_entry:
                RSSEntry.checkin_rss_entry(self, i)
