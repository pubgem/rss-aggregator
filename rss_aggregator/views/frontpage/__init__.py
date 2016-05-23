# rss-aggregator (c) pubgem

import flask
from flask.ext.paginate import Pagination
from rss_aggregator import models

frontpage = flask.Blueprint(
    'frontpage',
    __name__,
    template_folder='templates',
    static_folder='static-frontpage'
)


@frontpage.route('/')
def index():
    try:
        page = int(flask.request.args.get('page', 1))
    except ValueError:
        page = 1

    per_page = 10
    rss_entries = models.RSSEntry.query
    total = rss_entries.count()

    pagination = Pagination(
        page=page,
        per_page=10,
        total=total,
        record_name='rss_entries'
    )

    return flask.render_template(
        'frontpage/index.html',
        rss_entries=rss_entries.slice(page*per_page, (page*per_page)+per_page),
        pagination=pagination,
    )

    # return flask.render_template('index.html', admin_view=None, rss_entry=None)
    # return flask.redirect(flask.url_for(".hello"))


# @frontpage.route('/hello')
# def hello():
#     return flask.render_template('hello.html')
