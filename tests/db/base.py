# -*- coding: utf-8 -*-
"""
usage:

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

    def get_test():
        user_model = model_query(UserModel)\
                .filter(UserModel.name == 'jinlong')\
                .first()
        return user_model.id
"""

from sqlalchemy.ext.declarative import declarative_base
from osmo.db import api
from osmo.db import models


BASE = declarative_base(cls=models.ModelBase)

def get_session(*args, **kwargs):
    return api.get_session(*args, **kwargs)

def get_engine(*args, **kwargs):
    return api.get_engine(*args, **kwargs)

def model_query(model, session=None, args=None, **kwargs):
    """
    :param model  : Model to query, Must be subclass of ModelBase
    :type model   : models.ModelBase

    usage:
        user_model = model_query(UserModel)\
                .filter(UserModel.name == 'jinlong')\
                .first()
    """
    if not issubclass(model, models.ModelBase):
        raise TypeError('model must be subclass of ModelBase')

    if not session:
        session = get_session()
    query = session.query(model) if not args else session.query(*args)
    return query
