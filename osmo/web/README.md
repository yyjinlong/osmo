# 说明

    1) WsgiApplication使用说明

        所有继承自WsgiApplication的子类，首先都要导入log:
        from osmo.core import log as logging
        LOG = logging.getLogger(__name__)

        应用启动前需要setup:
        logging.setup("wsgi application.")

    2) 为什么要这么使用？

        osmo.core.log如下代码:
        common_cli_opts = [
            cfg.BoolOpt('debug',
                        short='d',
                        default=False,
                        help='Print debugging output (set logging level to '
                            'DEBUG instead of default WARNING level).'),
            cfg.BoolOpt('verbose',
                        short='v',
                        default=False,
                        help='Print more verbose output (set logging level to '
                            'INFO instead of default WARNING level).'),
        ]
        也就是将默认配置文件里的DEFAULT下的debug和verbose注册了。
        CONF = cfg.CONF
        CONF.register_cli_opts(common_cli_opts)

        所以,在WsgiApplication里,就不需要做重复的工作了,也就是将原有的删掉:
        default_opt =[
            cfg.BoolOpt(
                'debug',
                default = True
            )
        ]
        CONF = cfg.CONF
        CONF.register_opts(default_opt)

    3) 如果不去掉会有什么结果？

        oslo_config.cfg.DuplicateOptError: duplicate option: debug
        同时，其他文件导入osmo.core.log也会报错.

#调试

    $ virtualenv .venv
    $ source .venv/bin/activate
    $ pip install -r requirements.txt
    $ python setup.py build
    $ python setup.py develop
