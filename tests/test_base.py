# -*- coding:utf-8 -*-
#
# Copyright @ 2016 OPS, YY Inc.
#
# Author: Jinlong Yang
#

import time
import logging

from osmo.base import Application

LOG = logging.getLogger(__name__)


class TestApplication(Application):
    name = 'application'
    version = '0.1'

    def __init__(self):
        super(TestApplication, self).__init__()

    def run(self):
        while True:
            self.handler()
            time.sleep(5)

    def handler(self):
        LOG.info('Test Application has been begined.')
        LOG.info('Quit the server with CONTROL-C.')


if __name__ == '__main__':

    test_app = TestApplication()
    test_app.run()
