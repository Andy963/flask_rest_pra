# ！/usr/bin/env python
# encoding:utf-8
# Created by Andy at 2020/8/30
# CREATE DATABASE ginger DEFAULT CHARSET=UTF8 DEFAULT COLLATE utf8_general_ci;
SQLALCHEMY_DATABASE_URI = \
    'mysql+pymysql://root:zjgisadmin@localhost/ginger'

SECRET_KEY = "secreat"
SQLALCHEMY_TRACK_MODIFICATIONS = False