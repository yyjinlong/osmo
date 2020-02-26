# -*- coding:utf-8 -*-
#
# Copyright @ 2016 OPS, YY Inc.
#
# Author: Jinlong Yang
#

import sys

from oslo_config import cfg
from osmo.db import BASE, model_query
from sqlalchemy import (
    Column,
    Integer,
    String
)

CONF = cfg.CONF
CONF(sys.argv[1:])


class UserModel(BASE):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)


def get_users():
    user_models = model_query(UserModel).all()
    return [model.name for model in user_models if model]


if __name__ == '__main__':

    users = get_users()
    print ('.....result: ', users)
