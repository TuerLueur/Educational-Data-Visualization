# -*- coding: utf-8 -*-

import pymysql
import csv
import codecs


def get_conn():
    conn = pymysql.connect(host='localhost',\
                           port=3306, user='root',\
                           passwd='ground',\
                           db='vis',\
                           charset='utf8')
    return conn


def insert(cur, sql, args):
    cur.execute(sql, args)


def read_csv_to_mysql(filename):
    with codecs.open(filename=filename, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        conn = get_conn()
        cur = conn.cursor()
        sql = 'INSERT INTO `course3` VALUES(%s,%s,%s,%s,%s)'
        for item in reader:
            if item[1] is None or item[1] == '':
                continue
            args = tuple(item)
            print(args)
            insert(cur, sql=sql, args=args)

        conn.commit()
        cur.close()
        conn.close()


if __name__ == '__main__':
    read_csv_to_mysql('../organized_data/stu_course.csv')
