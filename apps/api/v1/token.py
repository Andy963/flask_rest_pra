# ！/usr/bin/env python
# encoding:utf-8
# Created by Andy at 2020/8/31
from flask import current_app, jsonify

from apps.libs.enums import ClientType
from apps.libs.redprint import Redprint
from apps.models.user import User
from apps.validators.forms import ClientForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature

api = Redprint('token')


@api.route('', methods=['POST'])
def get_token():
    client_form = ClientForm().validate_for_api()
    promise = {
        ClientType.USER_EMAIL: User.verify,
    }
    identity = promise[ClientType(client_form.type.data)](
        client_form.account.data,
        client_form.secret.data
    )
    # Token
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auth_token(identity['uid'],
                                client_form.type.data,
                                # identity['scope'],
                                expiration)
    t = {
        'token': token.decode('ascii')
    }
    return jsonify(t), 201


def generate_auth_token(uid, ac_type, scope=None,
                        expiration=7200):
    """生成令牌"""
    s = Serializer(current_app.config['SECRET_KEY'],
                   expires_in=expiration)
    return s.dumps({
        'uid': uid,
        'type': ac_type.value,
        'scope': scope
    })
