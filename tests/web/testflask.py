# -*- coding: utf-8 -*-
#
# Author: jinlong.yang
#

from flask import Flask
from werkzeug.serving import run_simple

args = [__name__]
kwargs = {}
app = Flask(*args, **kwargs)
app.debug = True

if __name__ == '__main__':
    run_simple('localhost', 5000, app)
