# -*_ encoding: utf-8 -*-

from flask import Flask, render_template, url_for, jsonify, request
import pymysql
import pandas as pd
app = Flask(__name__)


def get_conn():
    conn = pymysql.connect(host='groundzhou.cn',
                           port=33060, user='root',
                           passwd='viswebapp',
                           db='vis',
                           charset='utf8')
    return conn


def get_data():
    conn = get_conn()
    sql = 'SELECT * FROM course3 WHERE id > 100 ORDER BY amount DESC, id'
    df = pd.read_sql(sql=sql, con=conn)
    conn.close()
    return df


@app.route('/get-course3', methods=['GET', 'POST'])
def hello_world():
    df_course3 = get_data()
    course3_json = df_course3.to_json(orient='records')
    return course3_json


@app.route('/')
def index():
    return render_template('dataset-encode0.html')


if __name__ == '__main__':
    app.run(debug=True)
