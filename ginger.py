# ！/usr/bin/env python
# encoding:utf-8
# Created by Andy at 2020/8/30
from apps.app import create_app

app = create_app()






if __name__ == '__main__':
    app.run(debug=True,port=8000)
