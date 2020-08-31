# ！/usr/bin/env python
# encoding:utf-8
# Created by Andy at 2020/8/30
from flask import Blueprint
from apps.api.v1 import book, user, client, token


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    book.api.register(bp_v1, url_prefix='/book/')
    user.api.register(bp_v1, url_prefix='/user/')
    client.api.register(bp_v1, url_prefix='/client/Enum')
    token.api.register(bp_v1, url_prefix='/token/')
    return bp_v1
