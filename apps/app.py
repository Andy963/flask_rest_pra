# ！/usr/bin/env python
# encoding:utf-8
# Created by Andy at 2020/8/30
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object("apps.config.secure")
    app.config.from_object("apps.config.setting")

    return app
