import flask

frontpage = flask.Blueprint(
    'frontpage',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@frontpage.route('/')
def index():
    return flask.render_template('index.html', admin_view=None)
    # return flask.redirect(flask.url_for(".hello"))


# @frontpage.route('/hello')
# def hello():
#     return flask.render_template('hello.html')
