# ！/usr/bin/env python
# encoding:utf-8
# Created by Andy at 2020/8/31


from apps.libs.error import APIException


class ClientTypeError(APIException):
    # 400 401 403 404
    # 500
    # 200 201 204
    # 301 302
    code = 400
    msg = "client type is invalid"
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000
