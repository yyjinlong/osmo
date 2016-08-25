# -*- coding: utf-8 -*-
#
# Copyright @ 2016 OPS, YY Inc.
#
# Author: Jinlong Yang
#

from gunicorn.glogging import Logger


class GunicornLogger(Logger):

    def access(self, resp, req, environ, request_time):
        """overwrite access method, make ignore healthcheck,
        otherwise, accesslog file will more and more big.
        """
        if environ['RAW_URI'] == '/healthcheck.html':
            return
        super(GunicornLogger, self).access(resp, req, environ, request_time)
