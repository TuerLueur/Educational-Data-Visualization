# -*- coding: utf-8 -*-

# 将整个应用初始化
# 主要工作
#     1：构建flask应用以及各种配置
#     2：构建SQLAlchemy的应用

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    # 配置启动模式为调试模式
    app.config["DEBUG"] = True
    # 配置数据库的连接
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:ground@127.0.0.1:3306/vis"
    # 配置数据库内容在更新时自动提交
    app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
    # 配置session所需要的秘钥
    app.config["SECRET_KEY"] = "viskey"
    # 数据库的初始化
    db.init_app(app)
    return app
