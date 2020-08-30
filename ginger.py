# ！/usr/bin/env python
# encoding:utf-8
# Created by Andy at 2020/8/30
from apps.app import create_app

app = create_app()


@app.route("/v1/user/get/")
def get_user():
    return "I'm andy"


@app.route("/v1/book/get/")
def get_book():
    return "Book"


if __name__ == '__main__':
    app.run(debug=True)
