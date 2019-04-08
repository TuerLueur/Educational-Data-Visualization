# -*- coding: utf-8 -*-
# 当前项目相关的模型文件 实体类
from . import db

# 学生
class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    stu_name = db.Column(db.String(20), nullable=False)


# 老师




# 科目


# 班级


