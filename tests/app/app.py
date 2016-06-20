# -*- coding:utf-8 -*

from osmo.app.application import QApplication
from osmo.core import log as logging

LOG = logging.getLogger(__name__)


class MyApplication(QApplication):
    name = 'myapp'
    version = 'v0.1'

    def run(self):
        logging.setup('myapp log')
        LOG.info('myapp run')


if __name__ == '__main__':
    app = MyApplication()
    app.main()
