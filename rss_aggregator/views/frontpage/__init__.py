from rss_aggregator import models
import flask

frontpage = flask.Blueprint(
    'frontpage',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@frontpage.route('/frontpage')
def index():
    return flask.render_template('frontpage/index.html', rss_entries=models.RSSEntry.query.all())
    # return flask.render_template('index.html', admin_view=None, rss_entry=None)
    # return flask.redirect(flask.url_for(".hello"))


# @frontpage.route('/hello')
# def hello():
#     return flask.render_template('hello.html')
