# -*- coding:utf-8 -*-
#
# Copyright @ 2016 OPS, YY Inc.
#
# Author: Jinlong Yang
#

import sys

from oslo_config import cfg

import osmo.log

CONF = cfg.CONF


class Singleton(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class Application(Singleton):

    def __init__(self):
        if not (self.name and self.version):
            raise Exception('name and version not initialize.')
        self.setup()

    def setup(self):
        CONF(sys.argv[1:], version=self.version)
        osmo.log.init()

    def run(self):
        raise NotImplementedError('`run` method is not implemented!')

    def entry_point(self):
        def wrapper():
            self.run()
        return wrapper
