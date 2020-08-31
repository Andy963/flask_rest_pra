# ！/usr/bin/env python
# encoding:utf-8
# Created by Andy at 2020/8/31

from flask import request
from wtforms import Form

from apps.libs.error_code import ParameterException

__author__ = '七月'


class BaseForm(Form):
    def __init__(self):
        data = request.get_json(silent=True)
        args = request.args.to_dict()
        super(BaseForm, self).__init__(data=data, **args)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            # form errors
            raise ParameterException(msg=self.errors)
        return self
