# rss-aggregator (c) pubgem
from flask.ext.diamond.mixins.crud import CRUDMixin
from flask.ext.diamond.mixins.marshmallow import MarshmallowMixin
from .. import db, ma


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
    publisher = db.Column(db.String(25))
