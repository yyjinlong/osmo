# -*- coding:utf-8 -*-
#
# Copyright @ 2016 OPS, YY Inc.
#
# Author: Jinlong Yang
#

from oslo_config import cfg
from oslo_db.sqlalchemy import models
from oslo_db.sqlalchemy import session
from sqlalchemy.ext.declarative import declarative_base

_FACADE = None


def _create_facade_lazily():
    global _FACADE
    if _FACADE is None:
        _FACADE = session.EngineFacade.from_config(cfg.CONF)
    return _FACADE


def get_engine(*args, **kwargs):
    facade = _create_facade_lazily()
    return facade.get_engine(*args, **kwargs)


def get_session(*args, **kwargs):
    facade = _create_facade_lazily()
    return facade.get_session(*args, **kwargs)


def model_query(model, session=None, args=None, **kwargs):
    """
    :model param  : Model to query, Must be subclass of ModelBase
    :model type   : models.ModelBase

    usage session add data:

        def add_test():
            session = get_session()
            with session.begin(subtransactions=True):
                user_model = session.query(UserModel)\
                    .filter(UserModel.name == 'jinlong')\
                    .first()
                if not user_model:
                    user_model = UserModel()
                    user_model.name = 'jinlong'
                    session.add(user_model)

    usage model_query query data:

        def get_test():
            user_model = model_query(UserModel)\
                .filter(UserModel.name == 'jinlong')\
                .first()
            return user_model.id
    """
    if not issubclass(model, models.ModelBase):
        raise TypeError('Model must be subclass of ModelBase.')
    if not session:
        session = get_session()
    query = session.query(model) if not args else session.query(*args)
    return query


BASE = declarative_base(cls=models.ModelBase)
