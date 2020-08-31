# ！/usr/bin/env python
# encoding:utf-8
# Created by Andy at 2020/8/30
from flask import Blueprint

from apps.libs.redprint import Redprint
from apps.libs.token_auth import auth

api = Redprint('user')


@api.route("", methods=['GET'])
@auth.login_required
def get_user():
    return "I'm andy"
