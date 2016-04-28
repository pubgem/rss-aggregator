# rss-aggregator (c) pubgem
from flask.ext.diamond.mixins.crud import CRUDMixin
from flask.ext.diamond.mixins.marshmallow import MarshmallowMixin
from rss_aggregator import db


class RSSEntry(db.Model, CRUDMixin, MarshmallowMixin):
    id = db.Column(db.Integer(), primary_key=True)

    raw_xml = db.Column(db.Text)
    date = db.Column(db.DateTime)
    doi = db.Column(db.String(50))

    authors = db.Column(db.Text)  # TODO: Data structure, separat table, or just string?
    title = db.Column(db.String(50))
    issue = db.Column(db.Integer)
    volume = db.Column(db.Integer)
    pages = db.Column(db.Integer)
    www = db.Column(db.String(50))

    rss_feed = db.relationship('RSSFeed', backref=db.backref('rss_entry', lazy='dynamic'))
    rss_feed_id = db.Column(db.Integer, db.ForeignKey("rss_feed.id"))