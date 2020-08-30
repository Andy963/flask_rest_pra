# ！/usr/bin/env python
# encoding:utf-8
# Created by Andy at 2020/8/30
from flask import Blueprint

from apps.libs.redprint import Redprint

api = Redprint('user')

@api.route("get/")
def get_user():
    return "I'm andy"
