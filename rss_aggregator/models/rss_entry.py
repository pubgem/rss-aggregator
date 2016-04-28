# rss-aggregator (c) pubgem
from flask.ext.diamond.mixins.crud import CRUDMixin
from flask.ext.diamond.mixins.marshmallow import MarshmallowMixin
from rss_aggregator import db


class RSSEntry(db.Model, CRUDMixin, MarshmallowMixin):
    # __tablename__ = "entry"
    id = db.Column(db.Integer(), primary_key=True)

    raw_xml = db.Column(db.Text)
    date = db.Column(db.DateTime)
    doi = db.Column(db.String(50))

    authors = db.Column(db.Text)  # TODO: Data structure, separat table, or just string?
    title = db.Column(db.String(50))
    issue = db.Column(db.Integer)
    volume = db.Column(db.Integer)
    
