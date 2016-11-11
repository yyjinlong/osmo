# -*- coding: utf-8 -*-

from datetime import timedelta

from osmo.core import log as logging
from osmo.web.wsgiapp import WsgiApplication

LOG = logging.getLogger(__name__)


class TestApp(WsgiApplication):
    name = 'test_app'
    version = 'v1.0'

    def init_flask_app(self):
        super(TestApp, self).init_flask_app()
        logging.setup('test_www')
        LOG.info('test www app run.....')

        app = self.flask_app
        app.secret_key = 'haohaoxuexi,tiantianxiangshang.'
        app.permanent_session_lefttime = timedelta(hours=24)

        app.static_url_path = '/static'

        # 一定要根据'root_path': '具体路径',来确定templates和static的路径
        app.template_folder = 'templates'
        app.static_folder = 'static'

        # from pprint import pprint
        # pprint(app.__dict__)

        # @app.route('/')
        # def index():
        #     return render_template('index.html', page_title='jinlong')

        import views.index as index
        app.register_blueprint(index.bp, url_prefix='')


if __name__ == '__main__':
    t = TestApp()
    t.main()
