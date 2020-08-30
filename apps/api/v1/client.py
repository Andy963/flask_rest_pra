# ！/usr/bin/env python
# encoding:utf-8
# Created by Andy at 2020/8/30
from flask import request

from apps.libs.enums import ClientType
from apps.libs.redprint import Redprint
from apps.models.user import User
from apps.validators.forms import ClientForm, UserEmailForm

api = Redprint('client')


@api.route('/register/', methods=['POST', ])
def create_client():
    data = request.json
    client_form = ClientForm(data=data)
    if client_form.validate():
        promise = {
            ClientType.USER_EMAIL: __register_user_by_email
        }
        promise[client_form.type.data]()
    return 'success'


def __register_user_by_email():
    form = UserEmailForm().validate_for_api()
    User.register_by_email(form.nickname.data,
                           form.account.data,
                           form.secret.data)
