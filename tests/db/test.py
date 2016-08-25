# -*- coding: utf-8 -*-

import sys

from oslo.config import cfg

from base import model_query
from users import UserModel

cfg.CONF(sys.argv[1:],
         project='test',
         version='1.0',
         default_config_files=None)


def get_users():
    user_models = model_query(UserModel)\
            .all()
    return [model.name for model in user_models if model]

users = get_users()
print '.....result: ', users
