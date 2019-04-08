# -*- coding: utf-8 -*-
# 主目录 manage.py
# 启动和管理项目
from webapp import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
