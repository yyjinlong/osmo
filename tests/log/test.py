# -*- coding: utf-8 -*-

import sys

from oslo.config import cfg
from osmo.core import log as logging

cfg.CONF(sys.argv[1:],
         project='test',
         version='1.0',
         default_config_files=None)

CONF = cfg.CONF
print CONF.log_dir
print '. 代表当前目录'

logging.setup('test')
LOG = logging.getLogger(__name__)

LOG.info('osmo--jinlong.yang new test log')
