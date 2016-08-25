# -*- coding: utf-8 -*-

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
    ret = request.data
    print 'post or get data is: ', ret
    return 'success'
