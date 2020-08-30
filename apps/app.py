# ！/usr/bin/env python
# encoding:utf-8
# Created by Andy at 2020/8/30
from flask import Flask


def register_blueprints(app):
    from apps.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1/')


def create_app():
    app = Flask(__name__)
    app.config.from_object("apps.config.secure")
    app.config.from_object("apps.config.setting")

    register_blueprints(app)
    return app
