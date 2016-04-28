# rss-aggregator (c) pubgem
from flask.ext.diamond.mixins.crud import CRUDMixin
from flask.ext.diamond.mixins.marshmallow import MarshmallowMixin
from rss_aggregator import db


class Entry(db.Model, CRUDMixin, MarshmallowMixin):
    # __tablename__ = "entry"
    id = db.Column(db.Integer(), primary_key=True)

    raw_xml = db.Column(db.Text)
    date = db.Column(db.DateTime)
