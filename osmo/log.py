# -*- coding:utf-8 -*-
#
# Copyright @ 2020 OPS, YY Inc.
#
# Author: Jinlong Yang
#

import os
import logging.config

from oslo_config import cfg

default_opts = [
    cfg.StrOpt('log_dir', default='', help='log dir.'),
    cfg.StrOpt('log_file', default='', help='log file.')
]

CONF = cfg.CONF
CONF.register_cli_opts(default_opts)


class MyLog:

    def __init__(self):
        if not CONF.log_dir:
            raise Exception(u'log dir is not config.')
        if not CONF.log_file:
            raise Exception(u'log file is not config.')
        if not os.path.isdir(CONF.log_dir):
            os.mkdir(CONF.log_dir)
        self.logfile_path = os.path.join(CONF.log_dir, CONF.log_file)

    def setup(self):
        log_format = '%(asctime)s %(name)s ' \
                     '%(filename)s:%(funcName)s:%(lineno)d ' \
                     '[%(levelname)s] %(message)s'
        log_config = {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'standard': {
                    'format': log_format
                }
            },
            'filters': {},
            'handlers': {
                # NOTE(jinlong): 打印到终端的日志
                'console': {
                    'level': 'DEBUG',
                    'class': 'logging.StreamHandler',
                    'formatter': 'standard'
                },
                # NOTE(jinlong): 打印到文件的日志, 收集info及以上的日志.
                # 每个日志文件大小最大为1G, 生成5个备份文件
                'default': {
                    'level': 'INFO',
                    'class': 'logging.handlers.RotatingFileHandler',
                    'formatter': 'standard',
                    'filename': self.logfile_path,
                    'maxBytes': 1*1024*1024*1024,
                    'backupCount': 5,
                    'encoding': 'utf-8',
                },
            },
            'loggers': {
                '': {
                    'handlers': ['default', 'console'],
                    'level': 'DEBUG',
                    'propagate': True,
                },
            },
        }
        logging.config.dictConfig(log_config)


def init():
    MyLog().setup()


#if __name__ == '__main__':
#    import sys
#    CONF(sys.argv[1:], version='v1.0')
#
#    init()
#
#    LOG = logging.getLogger(__name__)
#    LOG.info('It works!')
