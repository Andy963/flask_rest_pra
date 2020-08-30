# ！/usr/bin/env python
# encoding:utf-8
# Created by Andy at 2020/8/30
from enum import Enum


class ClientType(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

    USER_MINI = 200
    USER_WX = 201
