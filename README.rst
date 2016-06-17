Desc

	through use openstack library, to provider convenience for flask application.at the same time by using the oslo.db library to simplify the operation of the database. by adding the log function, can make dameon process between more processes using the log function.


Dependent

	flask
	gunicorn
	gevent
	postgresql
	oslo.db
	oslo.config


Methods

	1) daemon application

		>>> from osmo.app.application import QApplication

	2) log application

		>>> from osmo.core import log as logging

	3) web application

		>>> from osmo.web.wsgiapp import WsgiApplication

	4) database application

		>>> from sqlalchemy.ext.declarative import declarative_base
		>>> from osmo.db import api
		>>> from osmo.db import models

		>>> BASE = declarative_base(cls=models.ModelBase)

		>>> def get_session(*args, **kwargs):
		>>>     return api.get_session(*args, **kwargs)

		>>> def get_engine(*args, **kwargs):
		>>>     return api.get_engine(*args, **kwargs)

		>>> def model_query(model, session=None, args=None, **kwargs):
		>>>     """
		>>>     :param model  : Model to query, Must be subclass of ModelBase
		>>>     :type model   : models.ModelBase

		>>>     usage:
		>>>         user_model = model_query(UserModel)\
		>>>                 .filter(UserModel.name == 'jinlong')\
		>>>                 .first()
		>>>     """
		>>>     if not issubclass(model, models.ModelBase):
		>>>         raise TypeError("model must be subclass of ModelBase")

		>>>     if not session:
		>>>         session = get_session()
		>>>     query = session.query(model) if not args else session.query(*args)
		>>>     return query
