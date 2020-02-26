# -*- coding:utf-8 -*-
#
# Copyright @ 2016 OPS, YY Inc.
#
# Author: Jinlong Yang
#

import logging
from datetime import timedelta

from osmo.wsgi import WSGIApplication

LOG = logging.getLogger(__name__)


class WSGITestApplication(WSGIApplication):
    name = 'wsgi'
    version = '0.1'

    def init_flask(self):
        super(WSGITestApplication, self).init_flask()
        LOG.info('Server is started..........')

        app = self.flask_app
        app.static_url_path = '/static'
        app.secret_key = 'my osmo flask web application'
        app.permanent_session_lifetime = timedelta(hours=2)

        # 一定要根据'root_path': '具体路径', 来确定templates和static的路径
        app.template_folder = 'templates'
        app.static_folder = 'static'
        LOG.info('....application root path is: %s' % app.root_path)

        # from pprint import pprint
        # pprint(app.__dict__)

        # @app.route('/')
        # def index():
        #     return render_template('index.html', page_title='jinlong')

        import views.index as index
        app.register_blueprint(index.bp, url_prefix='')


if __name__ == '__main__':

    wtc = WSGITestApplication()
    wtc.run()
