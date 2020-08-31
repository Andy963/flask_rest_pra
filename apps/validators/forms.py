# ！/usr/bin/env python
# encoding:utf-8
# Created by Andy at 2020/8/30
from wtforms import StringField, IntegerField
from wtforms.validators import Length, InputRequired, Email, Regexp, length, ValidationError, DataRequired

from apps.libs.enums import ClientType
from apps.models.user import User
from apps.validators.base import BaseForm as Form


class ClientForm(Form):
    account = StringField(validators=[DataRequired(message="account不允许为空"), Length(min=5, max=32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        try:
            client_value = ClientType(value.data)
        except ValueError as e:
            raise e

        self.type.data = client_value


class UserEmailForm(ClientForm):
    account = StringField(validators=[
        Email(message='invalidate email')
    ])
    secret = StringField(validators=[
        InputRequired(),
        # password can only include letters , numbers and "_"
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
    ])
    nickname = StringField(validators=[DataRequired(),
                                       length(min=2, max=22)])

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError()
