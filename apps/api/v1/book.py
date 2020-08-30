# ！/usr/bin/env python
# encoding:utf-8
# Created by Andy at 2020/8/30
from flask import Blueprint

from apps.libs.redprint import Redprint

api = Redprint('book')

@api.route("get/")
def get_book():
    return "Book"
