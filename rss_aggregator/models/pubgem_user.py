# rss-aggregator (c) pubgem
from flask.ext.diamond.models.user import User
from flask.ext.diamond import ma, db


class PubgemUser(User):
    """
    """

    subscription = db.relationship('RSSFeed', backref=db.backref('pubgem_user', lazy='dynamic'))
    "A subscription is a relationship with models.RSSEntry"

    subscription_id = db.Column(db.Integer, db.ForeignKey("rss_feed.id"))

    def subscribe(self, rss_feed):
        """

        """
        # self.subscription
        pass
