# -*- coding: utf-8 -*-
#
# Copyright @ 2016 OPS, YY Inc.
#
# Author: Jinlong Yang
#

from flask import (
    Blueprint,
    request,
    render_template
)

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    return render_template('index.html', page_title='jinlong')


@bp.route('/test', methods=['POST', 'GET'])
def test():
    data = request.data
    print ('.....receive data is: ', data)
    return 'success'
