# -*- coding: utf-8 -*-
#
# Author: jinlong.yang
#

import sys

from oslo.config import cfg

from osmo.app.singleton import Singleton


class QApplication(Singleton):

    def init_app(self):
        """before the application is running,
           make the oslo.config module take effect,
           otherwise other modules such as log module will invalid.

           Notice: every subclass must be define two static variable:
                   name and version.
        """
        cfg.CONF(sys.argv[1:],
                 project=self.name,
                 version=self.version,
                 default_config_files=None)

    def run(self):
        raise NotImplementedError("app.run is not implemented!")

    def main(self):
        """calling process:
            1. initialize application
            2. application run
        """
        self.init_app()
        self.run()

    def make_entry_point(self):
        def wrapper():
            self.main()
        return wrapper
