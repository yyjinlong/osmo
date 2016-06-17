osmo(openstack module) - keeping moving!
----------------------------------------

## 使用方法

    pip install osmo

## 其他方法

    一) git clone方式

        1) 安装virtualenv
            $ virtualenv test

        2) 激活virtualenv
            $ source test/bin/activate

        3) git clone osmo项目

        4) 进入osmo目录

        5) 编译
           $ python setup.py build

        6) 安装
           $ python setup.py install

        7) 查看
            (test)➜  ls .venv/lib/python2.7/site-packages/osmo*
            app  core  db  __init__.py  __init__.pyc  web

            .venv/lib/python2.7/site-packages/osmo-0.0.1.dev2-py2.7.egg-info:
            dependency_links.txt  not-zip-safe  pbr.json  PKG-INFO  requires.txt  SOURCES.txt  top_level.txt

        8) 输入python
            (test)➜  ~  python
            Python 2.7.5 (default, Mar  9 2014, 22:15:05)
            [GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
            Type "help", "copyright", "credits" or "license" for more information.
            >>> import osmo
            >>>


    二) 指定git地址

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

    flask
    gunicorn
    greenlet
    postgresql
    oslo.db
    oslo.config


## 应用场景

    一) 创建daemon程序

        使用osmo.app

        >>> from osmo.app.application import QApplication

    二) 日志功能

        使用osmo.core.log

        >>> from osmo.core import log as logging

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

        使用osmo.web: 通过gunicorn库来自动为你的wsgi应用包含在容器中运行, 并可忽略nginx的healthcheck功能.

        >>> from osmo.web.wsgiapp import WsgiApplication
