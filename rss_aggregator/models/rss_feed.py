# rss-aggregator (c) pubgem
from . import RSSEntry
from ..utils import parse_rss_timestamp
from flask.ext.diamond.mixins.crud import CRUDMixin
from flask.ext.diamond.mixins.marshmallow import MarshmallowMixin
from flask.ext.diamond import ma, db
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
            "summary",
        )


class RSSFeed(db.Model, CRUDMixin, MarshmallowMixin):
    __schema__ = RSSFeedSchema

    id = db.Column(db.Integer(), primary_key=True)

    name = db.Column(db.Text)
    rss_url = db.Column(db.Text)
    doi = db.Column(db.Text)
    parser_class = db.Column(db.Text)

    www = db.Column(db.Text)
    issn = db.Column(db.Text)
    isbn = db.Column(db.Text)
    publisher = db.Column(db.Text)
    summary = db.Column(db.Text)

    def aggregate(self):
        """
        Queries the RSS Feed, checks for a new entry, and checks-in new entry.
        """
        if self.parser_class in ["sciencedirect", "tandf", "springer", "rss"]:
            print("WARN: skip unsupported parser_class {0}".format(self.parser_class))
            return

        d = feedparser.parse(self.rss_url)
        # self.parse_timestamp(d.feed['updated_parsed'])  # used in later optimization
        # Feedparser.Bozo flag
        for i in d['entries']:
            # Iterate through the feed, check if entry already exists
            existing_entry = self.rss_entry.filter_by(
                title=i.title,
                date=parse_rss_timestamp(i.updated_parsed)).all()
            if not existing_entry:
                RSSEntry.checkin_rss_entry(self, i)
