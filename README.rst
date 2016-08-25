Description

    python tools library for daemon or web application


Dependency

    0) common

        setuptools == 20.2.2

    1) web application (wsgi framework use flask; database use postgresql)

        # web application

        - flask == 0.10.1
        - gunicorn == 19.3.0
        - gevent == 1.1.1

        # database application

        - oslo.db == 2.1.0
        - psycopg2 == 2.5.5
        - sqlalchemy == 0.9.9

    2) daemon application

        nothing


Methods

	1) daemon application

        >>> from osmo.app.application import QApplication
        >>> from osmo.core import log as logging
        >>>
        >>> LOG = logging.getLogger(__name__)
        >>>
        >>>
        >>> class MyApplication(QApplication):
        >>>     name = 'myapp'
        >>>     version = 'v0.1'
        >>>
        >>>     def run(self):
        >>>         logging.setup('myapp log')
        >>>         LOG.info('myapp run')
        >>>

	2) web application

        >>> from osmo.web.wsgiapp import WsgiApplication
        >>> from osmo.core import log as logging
        >>>
        >>> LOG = logging.getLogger(__name__)
        >>>
        >>>
        >>> class TestApp(WsgiApplication):
        >>>     name = "test_app"
        >>>     version = "v1.0"
        >>>
        >>>     def init_flask_app(self):
        >>>         super(TestApp, self).init_flask_app()
        >>>         logging.setup("test_www")
        >>>         LOG.info("test www app run.....")
        >>>
        >>>         app = self.flask_app
        >>>         app.secret_key = 'haohaoxuexi,tiantianxiangshang.'
        >>>         app.permanent_session_lefttime = timedelta(hours=24)
        >>>
        >>>         app.static_url_path = '/static'
        >>>
        >>>         app.template_folder = 'templates'
        >>>         app.static_folder = 'static'
        >>>
        >>>
        >>>         # Use app route
        >>>         #@app.route('/')
        >>>         #def index():
        >>>         #    return render_template('index.html', page_title='jinlong')
        >>>
        >>>         # Use blueprint route
        >>>         import views.index as index
        >>>         app.register_blueprint(index.bp, url_prefix='')
