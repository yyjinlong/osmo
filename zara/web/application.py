# -*- coding: utf-8 -*-
#
# Author: jinlong.yang
#

import sys

from oslo.config import cfg

from singleton import Singleton


class QApplication(Singleton):
    name = ""
    version = ""

    def init_app(self):
        pass

    def configure(self):
        """before the application is running,
           make the oslo.config module take effect,
           otherwise other modules such as log module will invalid
        """
        cfg.CONF(sys.argv[1:],
                 project=self.name,
                 version=self.version,
                 default_config_files=None)

    def run(self):
        raise NotImplementedError("app.run is not implemented!")

    def main(self):
        """calling process:
            1. inititialize application
            2. config oslo.config's conf file
            3. application run
        """
        self.init_app()
        self.configure()
        self.run()

    def make_entry_point(self):
        def wrapper():
            self.main()
        return wrapper

