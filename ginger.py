# ！/usr/bin/env python
# encoding:utf-8
# Created by Andy at 2020/8/30
from http.client import HTTPException

from apps import create_app
from apps.libs.error import APIException
from apps.libs.error_code import ServerError

app = create_app()


@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        # 调试模式
        # log
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True, port=8000)
