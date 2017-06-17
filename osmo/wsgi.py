# -*- coding: utf-8 -*-
#
# Copyright @ 2016 OPS, YY Inc.
#
# Author: Jinlong Yang
#

import sys
import multiprocessing

from flask import Flask
from oslo_config import cfg
from werkzeug.serving import run_simple
from gunicorn.app.base import Application

from osmo.basic import Basic

web_opts = [
    cfg.StrOpt('run_mode', default='werkzeug',
               choices=('gunicorn', 'werkzeug'),
               help='Wsgi server run mode choice, defaule werkzeug.'),
    cfg.StrOpt('bind', default='0.0.0.0',
               help='Wsgi server run ip address.'),
    cfg.IntOpt('port', default=5000,
               help='Wsgi server run port.'),
    cfg.IntOpt('timeout', default=600,
               help='Wsgi worker handle task timeout.'),
    cfg.StrOpt('accesslog', default=None,
               help='Wsgi access log file path.')
]

CONF = cfg.CONF
CONF.register_cli_opts(web_opts, 'WEB')


class WSGISystem(Basic):

    def __init__(self):
        super(WSGISystem, self).__init__()
        self.init_flask()

    def init_flask(self, args=None, kwargs=None):
        """Create and initialize flask application, child class
        only need to implement this method.
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
        """ Use wsgi debug running.
        """
        run_simple(CONF.WEB.bind,
                   CONF.WEB.port,
                   self.flask_app,
                   use_reloader=CONF.debug,
                   use_debugger=CONF.debug)

    def _gunicorn_prod_run(self):
        """ Use gunicorn product running.
        """
        app = self.flask_app

        class GunicornApp(Application):

            def init(self, parser, opts, args):
                # NOTE(Per-fork workers)
                workers = multiprocessing.cpu_count() * 2 + 1

                # NOTE(Usage supervisor running, so set false.)
                daemon = False

                # NOTE(Gunicorn work class use gevent coroutine.)
                worker_class = 'gevent'

                cfg_options = {
                    'bind': "%s:%s" % (CONF.WEB.bind, CONF.WEB.port),
                    'daemon': daemon,
                    'workers': workers,
                    'timeout': CONF.WEB.timeout,
                    'accesslog': CONF.WEB.accesslog,
                    'worker_class': worker_class
                }
                return cfg_options

            def load(self):
                return app

        # gunicorn custom application file after no any param
        # only have execute file.
        sys.argv = [sys.argv[0]]
        GunicornApp().run()

    def run(self):
        if CONF.WEB.run_mode == 'werkzeug':
            self._wsgi_debug_run()
        elif CONF.WEB.run_mode == 'gunicorn':
            self._gunicorn_prod_run()
        else:
            raise Exception('Run mode error, choice werkzeug or gunicorn.')
