#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv


file_cj = '../education_data/5_chengji.csv'
out_stu_925 = '../organized_data/out_stu_925.csv'

out_yuwen_925 = '../organized_data/yuwen_925.csv'

headers_yuwen_925 = ['exam_number','exam_numname', 'exam_type', 'mes_sub_id', 'mes_sub_name', 'max_score', 'min_score']
datas_yuwen_925 = []
data_stu_id = []

with open(out_stu_925) as stu_csv:
    reader = csv.DictReader(stu_csv)
    for row in reader:
        data_stu_id.append(row['bf_StudentID'])

with open(file_cj) as cj_csv:
    reader = csv.DictReader(cj_csv)
    i = 0
    exam = {}
    for row in reader:
        if row['mes_sub_id'] == '1' and row['mes_StudentID'] in data_stu_id:
            if row['exam_number'] in exam:
                if float(row['mes_Score']) > float(datas_yuwen_925[exam[row['exam_number']]]['max_score']):
                     datas_yuwen_925[exam[row['exam_number']]]['max_score'] = row['mes_Score']
                if float(row['mes_Score']) < float(datas_yuwen_925[exam[row['exam_number']]]['min_score']) and float(row['mes_Score']) >= 0:
                     datas_yuwen_925[exam[row['exam_number']]]['min_score'] = row['mes_Score']

            else:
                exam[row['exam_number']] = i
                i = i + 1
                datas_yuwen_925.append({'exam_number':row['exam_number'],
                                        'exam_numname':row['exam_numname'],
                                        'exam_type':row['exam_type'],
                                        'mes_sub_id':row['mes_sub_id'],
                                        'mes_sub_name':row['mes_sub_name'],
                                        'min_score':row['mes_Score'],
                                        'max_score':row['mes_Score']})


with open(out_yuwen_925,'w',newline='') as cj_csv:
    writer = csv.DictWriter(cj_csv, headers_yuwen_925)
    writer.writeheader()
    writer.writerows(datas_yuwen_925)




