#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, csv, json

csv_in = '../education_data/shuxue_925.csv'
json_out = '../organized_data/shuxue_925.json'

d = {'exam_numname':[],
     'exam_type':[],
     'mes_sub_id':[],
     'max_score':[],
     'min_score':[]}

with open(csv_in) as cj_csv:
    reader = csv.DictReader(cj_csv)
    for row in reader:
        d['exam_numname'].append(row['exam_numname'])
        d['exam_type'].append(row['exam_type'])
        d['mes_sub_id'].append(row['mes_sub_id'])
        d['max_score'].append(float(row['max_score']))
        d['min_score'].append(float(row['min_score']))

with open(json_out, 'w') as cj_json:
    cj_json.write(json.dumps(d, encoding = 'utf-8', indent=4, separators=(',', ': ')))
