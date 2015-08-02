# -*- coding: utf-8 -*-
#
# Author: jinlong.yang
#

from flask import Flask
from oslo.config import cfg
from werkzeug.serving import run_simple

from osmo.app.application import QApplication

CONF = cfg.CONF

default_opts = [
    cfg.BoolOpt(
        'debug',
        default = True,
        help = "flask debug mode"
    ),
    cfg.BoolOpt(
        'verbose',
        default = True,
        help = "show detail infos"
    )
]

web_opts = [
        cfg.StrOpt(
            "base_url",
            default = "/",
            help = "the web site's url prefix"
        ),
        cfg.StrOpt(
            "run_mode",
            default = "werkzeug",
            choices = ("gunicorn", "werkzeug"),
            help = "use werkzeug mode run debug"
        ),
        cfg.StrOpt(
            "bind",
            default = "0.0.0.0",
            help = "server run's ip address"
        ),
        cfg.IntOpt(
            "port",
            default = 5000,
            help = "the port to listen"
        )
]

gunicorn_opts = [
]

CONF = cfg.CONF
CONF.register_cli_opts(default_opts)
CONF.register_cli_opts(web_opts, "web")
CONF.register_cli_opts(gunicorn_opts, "gunicorn")


class QFlaskApplication(QApplication):

    def init_app(self):
        """初始化应用
        """
        self.flask_app = None
        self.init_flask_app()

    def init_flask_app(self, args=None, kwargs=None):
        """初始化flask应用
        """
        # init flask arguments
        args = [] if args is None else args
        kwargs = {} if kwargs is None else kwargs
        args.insert(0, __name__)

        # create flask application
        self.flask_app = Flask(*args, **kwargs)
        self.flask_app.debug = CONF.debug

        # 开启异常传播
        self.flask_app.config["PROPAGATE_EXCEPTIONS"] = True

    def _wsgi_debug_run(self):
        """使用wsgi调试运行
        """
        run_simple(CONF.web.bind,
                   CONF.web.port,
                   self.flask_app,
                   use_reloader=CONF.debug,
                   use_debugger=CONF.debug)

    def _gunicorn_prod_run(self):
        """使用gunicorn发布运行
        """
        pass

    def run(self):
        if CONF.web.run_mode == "werkzeug":
            self._wsgi_debug_run()
        elif CONF.web.run_mode == "gunicorn":
            self._gunicorn_prod_run()
