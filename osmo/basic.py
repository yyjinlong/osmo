# -*- coding:utf-8 -*-
#
# Copyright @ 2016 OPS, YY Inc.
#
# Author: Jinlong Yang
#

import sys

from oslo_config import cfg
from oslo_log import log as logging

CONF = cfg.CONF
LOG = logging.getLogger(__name__)


class Singleton(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class Basic(Singleton):

    def __init__(self):
        if not (self.name and self.version):
            raise Exception('name and version not initialize.')
        self.setup()
        LOG.debug('Log and Confg perpare has been ready.')

    def setup(self):
        logging.register_options(CONF)
        CONF(sys.argv[1:], version=self.version)
        logging.setup(CONF, self.name)

    def run(self):
        raise NotImplementedError('Basic run method is not implemented!')

    def entry_point(self):
        def wrapper():
            self.run()
        return wrapper
