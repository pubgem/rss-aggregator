# rss-aggregator (c) pubgem
from flask.ext.diamond.models.user import User
from flask.ext.diamond import ma, db

pubgemuser_rssfeed = db.Table('pubgemuser_rssfeed',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('rss_feed_id', db.Integer(), db.ForeignKey('rss_feed.id')))


class PubgemUser(User):
    """
    """

    subscriptions = db.relationship(
        'RSSFeed',
        secondary=pubgemuser_rssfeed,
        backref=db.backref('pubgem_user', lazy='dynamic'),
        # enable_typechecks=False)
    )
    "A subscription is a relationship with models.RSSEntry"

    def subscribe(self, *rss_feeds):
        """
        Subscribes a PubgemUser to an RSSFeed.

        :param *rss_feeds: a list of models.RSSFeed objects
        """
        valid_feeds = [i for i in rss_feeds if i not in self.subscriptions]  # Removes any duplicate subscriptions
        self.subscriptions.extend(valid_feeds)
        # import ipdb; ipdb.set_trace()

    def unsubscribe(self, *rss_feeds):
        """
        Unsubscribes a PubgemUser from an RSSFeed.
        """
        valid_feeds = [i for i in rss_feeds if i not in self.subscriptions]  # Removes any duplicate subscriptions
        self.subscriptions.extend(valid_feeds)
        # import ipdb; ipdb.set_trace()
