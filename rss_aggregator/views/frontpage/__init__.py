# rss-aggregator (c) pubgem

import flask
from flask.ext.paginate import Pagination
from rss_aggregator import models
from flask.ext.security import current_user

frontpage = flask.Blueprint(
    'frontpage',
    __name__,
    template_folder='templates',
    static_folder='static-frontpage'
)

per_page = 20


def index_all():
    try:
        page = int(flask.request.args.get('page', 1))
    except ValueError:
        page = 1

    rss_entries = models.RSSEntry.query
    total = rss_entries.count()

    pagination = Pagination(
        page=page,
        per_page=per_page,
        total=total,
        # inner_window=0,
        # outer_window=0,
        record_name='rss_entries'
    )

    return flask.render_template(
        'frontpage/index.htm.j2',
        rss_entries=rss_entries.slice(page*per_page, (page*per_page)+per_page),
        pagination=pagination,
    )


def index_filtered():
    try:
        page = int(flask.request.args.get('page', 1))
    except ValueError:
        page = 1

    # subscriptions = current_user.subscriptions

    # subq = session.query(RSSEntry)
    # subq = subq.filter(Equipment.equipment_type == "L").subquery()

    # q = RSSEntry.query.filter(
    #     RSSEntry.rss_feed.in_(
    #         User.get_by_id(1).subscriptions
    #     )
    # )

    rss_entries = models.RSSEntry.query
    total = rss_entries.count()

    pagination = Pagination(
        page=page,
        per_page=per_page,
        total=total,
        record_name='rss_entries'
    )

    return flask.render_template(
        'frontpage/index.htm.j2',
        rss_entries=rss_entries.slice(page*per_page, (page*per_page)+per_page),
        pagination=pagination,
    )

    # result = db.engine.execute("<sql here>")


@frontpage.route('/')
def index():
    if current_user:
        #return "logged in"
        return index_all()
    else:
        return index_all()


@frontpage.route('/subscriptions')
def subscriptions():
    return flask.render_template(
        'frontpage/subscriptions.htm.j2',
    )


@frontpage.route('/user/subscribe/<id>')
def do_subscribe(id):
    new_feed = models.RSSFeed.get_by_id(int(id))
    current_user.subscribe(new_feed)
    return flask.redirect("/subscriptions")


@frontpage.route('/user/unsubscribe/<id>')
def do_unsubscribe(id):
    new_feed = models.RSSFeed.get_by_id(int(id))
    current_user.unsubscribe(new_feed)
    return flask.redirect("/subscriptions")


@frontpage.route('/journal/<id>')
def journal(id):
    try:
        page = int(flask.request.args.get('page', 1))
    except ValueError:
        page = 1

    rss_feed = models.RSSFeed.get_by_id(id)
    print(rss_feed.rss_entry.all())
    rss_entries = rss_feed.rss_entry
    total = rss_entries.count()

    pagination = Pagination(
        page=page,
        per_page=per_page,
        total=total,
        record_name='rss_entries'
    )

    return flask.render_template(
        'frontpage/journal.htm.j2',
        rss_feed=rss_feed,
        rss_entries=rss_entries.slice((page-1)*per_page, ((page-1)*per_page)+per_page),
        pagination=pagination,
    )
