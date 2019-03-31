#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv

file_cj = '../organized_data/cj_valid_bystu.csv'
file_total = '../organized_data/stu_total_score.csv'

cj = open(file_cj)
stu_total = open(file_total, 'w', newline='')

reader = csv.DictReader(cj)
writer = csv.DictWriter(stu_total, ['cla_id',
                                    'cla_Name',
                                    'exam_number', 
                                    'exam_numname',
                                    'exam_type',
                                    'exam_sdate',
                                    'mes_TestID',
                                    'mes_StudentID',
                                    'mes_Total_Score'])
writer.writeheader()

row = next(reader)
temp_mes_StudentID = row['mes_StudentID']
temp_exam_number = row['exam_number']
sum_Score = float(row['mes_Score'])

for row in reader:
    if row['exam_number'] == temp_exam_number \
            and row['mes_StudentID'] == temp_mes_StudentID:
        sum_Score += float(row['mes_Score'])
    else:
        writer.writerow({'cla_id':row['cla_id'],
                         'cla_Name':row['cla_Name'],
                         'exam_number':row['exam_number'], 
                         'exam_numname':row['exam_numname'],
                         'exam_type':row['exam_type'],
                         'exam_sdate':row['exam_sdate'],
                         'mes_TestID':row['mes_TestID'],
                         'mes_StudentID':row['mes_StudentID'],
                         'mes_Total_Score':sum_Score})
        temp_mes_StudentID = row['mes_StudentID']
        temp_exam_number = row['exam_number']
        sum_Score = float(row['mes_Score'])

cj.close()
stu_total.close()
