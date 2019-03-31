#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv

# input file
file_cj = '../organized_data/cj_valid.csv'

# output file
file_cj_average = '../organized_data/cj_average.csv'

cj = open(file_cj)
cj_average = open(file_cj_average, 'w', newline='')

reader_cj = csv.DictReader(cj)
writer = csv.DictWriter(cj_average, ['cla_id',
                                     'cla_Name',
                                     'mes_sub_id', 
                                     'mes_sub_name',
                                     'exam_number',
                                     'exam_numname', 
                                     'exam_type',
                                     'exam_sdate',
                                     'mes_TestID',
                                     'sum_Student',
                                     'avg_Score',
                                     'max_Score',
                                     'min_Score'])
writer.writeheader()

row_cj = next(reader_cj)
temp_cla_id = row_cj['cla_id']
temp_exam_number = row_cj['exam_number']
sum_Score = float(row_cj['mes_Score'])
n = 1
max_Score = float(row_cj['mes_Score'])
min_Score = float(row_cj['mes_Score'])

for row_cj in reader_cj:
    if row_cj['cla_id'] == temp_cla_id and row_cj['exam_number'] == temp_exam_number:
        sum_Score += float(row_cj['mes_Score'])
        n += 1
        if float(row_cj['mes_Score']) > max_Score:
            max_Score = float(row_cj['mes_Score'])
        if float(row_cj['mes_Score']) < min_Score:
            min_Score = float(row_cj['mes_Score'])
    else:
        avg_Score = sum_Score / n
        writer.writerow({'cla_id':row_cj['cla_id'],
                         'cla_Name':row_cj['cla_Name'],
                         'mes_sub_id':row_cj['mes_sub_id'],
                         'mes_sub_name':row_cj['mes_sub_name'],
                         'exam_number':row_cj['exam_number'],           
                         'exam_numname':row_cj['exam_numname'], 
                         'exam_type':row_cj['exam_type'],
                         'exam_sdate':row_cj['exam_sdate'],
                         'mes_TestID':row_cj['mes_TestID'],
                         'sum_Student':n,
                         'avg_Score':avg_Score,
                         'max_Score':max_Score,
                         'min_Score':min_Score})

        temp_cla_id = row_cj['cla_id']
        temp_exam_number = row_cj['exam_number']
        sum_Score = float(row_cj['mes_Score'])
        n = 1
        max_Score = float(row_cj['mes_Score'])
        min_Score = float(row_cj['mes_Score'])

cj.close()
cj_average.close()
