# -*- coding:utf-8 -*-
#
# Copyright @ 2020 OPS, YY Inc.
#
# Author: Jinlong Yang
#

import json
import hashlib
from enum import Enum, unique
from operator import itemgetter

import requests


@unique
class HTTP(Enum):

    GET = 0
    POST = 1
    PUT = 2
    DELETE = 3


@unique
class RESULT(Enum):

    SUCC = 0
    FAIL = 1


def context(code, msg='', data=[]):
    r = {}
    r['code'] = code
    r['msg'] = msg
    r['data'] = data
    return json.dumps(r)


def http_handler(url, http_type, headers=None, payload=None):
    """ URL interface return value is json object.
    such as:
    {
        'code': 0/1,
        'msg': 'xxxx',
        'data': []/{}/value
    }
    returns:
        data is list or dict or concrete value if success, or ``None``
    """
    if http_type == HTTP.GET:
        resp = requests.get(url, params=payload, headers=headers)
    elif http_type == HTTP.POST:
        resp = requests.post(url, data=payload, headers=headers)
    else:
        raise Exception('unknown http type!')
    if resp.status_code != 200:
        raise Exception('http status code is: %s' % resp.status_code)
    ret_info = resp.json()
    if ret_info.get('code') != 0:
        raise Exception(ret_info.get('msg'))
    return ret_info.get('data')


def parameter_sign(data, salt):
    """ Interface request parameters sign calculate method.

    Signature calculation process is as follows:
    1. according the "key" to sorted
    2. stitching "key" and "value" to a string, and calculate the md5
    3. use the second step of "md5" add "salt" work out new md5.

    origin data:
    >>> data = {'name': 'yy', 'age': 18}

    calculate origin data's signature:
    >>> new_data = {'age': 18, 'name': 'yy'}
    >>> origin_data = 'age18nameyy'
    >>> encrypt_data = hashlib.md5(origin_data.encode()).hexdigest()
    >>> new_data = (encrypt_data+salt).encode()
    >>> sign = hashlib.md5(new_data).hexdigest().upper()
    >>> return sign
    """
    new_data = sorted(data.items(), key=itemgetter(0))
    origin_data = ''
    for item in new_data:
        origin_data += str(item[0])
        origin_data += str(item[1])
    encrypt_data = hashlib.md5(origin_data.encode()).hexdigest()
    return hashlib.md5((encrypt_data+salt).encode()).hexdigest().upper()


def parameter_auth(data, salt):
    cur_sign = data.pop('sign')
    cal_sign = parameter_sign(data, salt)
    if cur_sign != cal_sign:
        raise Exception(u'sign is not right!')
