osmo(my openstack module) - keeping moving!
----------------------------------------

## pypi地址

    https://pypi.python.org/pypi/osmo

## 使用方法

    pip install osmo

## 指定git地址进行安装

    1) 安装virtualenv
        $ virtualenv .venv

    2) 激活virtualenv
        $ source .venv/bin/activate

    3) 添加requirements.txt
    git+git://github.com/yyjinlong/osmo.git#egg=osmo

    4) pip安装
        (.venv)➜  test  pip install -r requirements.txt

    5) 错误
    Error: pg_config executable not found.

    6) 解决
    ➜  ~ sudo apt-get install libpq-dev python-dev
    之后再重新执行一遍就搞定

## 依赖

    # NOTE(web应用)
    flask
    gunicorn
    gevent

    # NOTE(db操作)
    psycopg2
    sqlalchemy
    oslo.db

## 应用场景

    一) 创建daemon程序

        使用osmo.app

        >>> from osmo.app.application import QApplication

    二) 日志功能

        使用osmo.core.log

        >>> from osmo.core import log as logging
        >>> logging.setup('application') # 应用初始化时调用

        使用:
        >>> LOG = logging.getLogger(__name__)

    三) 数据库功能

        使用osmo.db: 里边通过调用oslo.db，来对sqlalchemy进行封装并有连接池.

		>>> from sqlalchemy.ext.declarative import declarative_base
		>>> from osmo.db import api
		>>> from osmo.db import models

		>>> BASE = declarative_base(cls=models.ModelBase)

		>>> def get_session(*args, **kwargs):
		>>> 	return api.get_session(*args, **kwargs)

		>>> def get_engine(*args, **kwargs):
		>>> 	return api.get_engine(*args, **kwargs)

		>>> def model_query(model, session=None, args=None, **kwargs):
		>>> 	"""
		>>> 	:param model  : Model to query, Must be subclass of ModelBase
		>>> 	:type model   : models.ModelBase

		>>> 	usage:
		>>> 		user_model = model_query(UserModel)\
		>>> 				.filter(UserModel.name == 'jinlong')\
		>>> 				.first()
		>>> 	"""
		>>> 	if not issubclass(model, models.ModelBase):
		>>> 		raise TypeError("model must be subclass of ModelBase")

		>>> 	if not session:
		>>> 		session = get_session()
		>>> 	query = session.query(model) if not args else session.query(*args)
		>>> 	return query

    四) web应用

        使用osmo.web

        >>> from osmo.web.wsgiapp import WsgiApplication

        注: WsgiApplication使用说明

        1) 所有继承自WsgiApplication的子类，首先都要导入log

            >>> from osmo.core import log as logging
            >>> LOG = logging.getLogger(__name__)

            应用启动前需要setup:
            >>> logging.setup("wsgi application.")

        2) 配置文件里的debug和verbose已在osmo.core.log里注册了
