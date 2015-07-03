# -*- coding: utf-8 -*-
#
# Author: jinlong.yang
#

from flask import (
    Blueprint,
    request
)

bp = Blueprint("test", __name__)

@bp.route("/test", methods=["POST", "GET"])
def test():
    ret = request.data
    print ret
    return "success"

