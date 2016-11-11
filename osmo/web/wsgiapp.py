# -*- coding: utf-8 -*-
#
# Copyright @ 2016 OPS, YY Inc.
#
# Author: Jinlong Yang
#

import sys
import multiprocessing

from flask import Flask
from oslo.config import cfg
from werkzeug.serving import run_simple
from gunicorn.app.base import Application

from osmo.app.application import QApplication

web_opts = [
    cfg.StrOpt(
        'run_mode',
        default='werkzeug',
        choices=('gunicorn', 'werkzeug'),
        help='use werkzeug mode run debug'
    ),
    cfg.StrOpt(
        'bind',
        default=None,
        help='server run ip address'
    ),
    cfg.IntOpt(
        'port',
        default=5000,
        help='the port to listen'
    ),
    cfg.BoolOpt(
        'daemon',
        default=False,
        # use supervisor running, so set false
        help='Daemonize the Gunicorn process'
    ),
    cfg.IntOpt(
        'workers',
        default=0,
        help='The number of worker processes for handling requests'
    ),
    cfg.IntOpt(
        'timeout',
        default=600,
        help='Workers more than this seconds are killed and restarted'
    ),
    cfg.StrOpt(
        'accesslog',
        default=None,
        help='access log file'
    ),
    cfg.BoolOpt(
        'accesslog_ignore_healthcheck',
        default=True,
        help='access log file ignore nginx health check'
    ),
    cfg.StrOpt(
        'worker_class',
        default='gevent',
        choices=('sync', 'gevent'),
        help='gunicorn work mode'
    )
]

CONF = cfg.CONF
CONF.register_cli_opts(web_opts, "web")


class WsgiApplication(QApplication):

    def init_app(self):
        super(WsgiApplication, self).init_app()

    def init_flask_app(self, args=None, kwargs=None):
        """Flask Application Create And Initialize.

        Child class only need to implement this method.
        """
        # init flask arguments
        args = [] if args is None else args
        kwargs = {} if kwargs is None else kwargs

        # flask app name is self.name rather than __name__
        # otherwise, flask can't find templates and static directory
        # because, flask root_path's value not right when inherit this class
        args.insert(0, self.name)

        # create flask application
        self.flask_app = Flask(*args, **kwargs)
        self.flask_app.debug = CONF.debug

        # open exception transport
        self.flask_app.config['PROPAGATE_EXCEPTIONS'] = True

    def _wsgi_debug_run(self):
        """use wsgi debug running
        """
        run_simple(CONF.web.bind,
                   CONF.web.port,
                   self.flask_app,
                   use_reloader=CONF.debug,
                   use_debugger=CONF.debug)

    def _gunicorn_prod_run(self):
        """use gunicorn product running
        """
        app = self.flask_app

        class GunicornApp(Application):

            def init(self, parser, opts, args):
                """overwrite parent init method,
                and then return config optional settings.
                """
                # per-fork workers
                workers = CONF.web.workers
                if 0 == workers:
                    workers = multiprocessing.cpu_count() * 2 + 1

                # The logger you want to use to log events in gunicorn
                logger_class = 'gunicorn.glogging.Logger'
                if CONF.web.accesslog_ignore_healthcheck:
                    logger_class = 'osmo.web.glogging.GunicornLogger'

                cfg_options = {
                    'bind': "%s:%s" %(CONF.web.bind, CONF.web.port),
                    'daemon': CONF.web.daemon,
                    'workers': workers,
                    'timeout': CONF.web.timeout,
                    'accesslog': CONF.web.accesslog,
                    'worker_class': CONF.web.worker_class,
                    'logger_class': logger_class
                }
                return cfg_options

            def load(self):
                return app

        # gunicorn custom application file after no any param
        # only have execute file
        sys.argv = [sys.argv[0]]
        GunicornApp().run()

    def run(self):
        if CONF.web.run_mode == 'werkzeug':
            self._wsgi_debug_run()
        elif CONF.web.run_mode == 'gunicorn':
            self._gunicorn_prod_run()

    def main(self):
        """calling process:
            1. initialize application
            2. initialize flask application
            3. flak application run
        """
        self.init_app()
        self.init_flask_app()
        self.run()
