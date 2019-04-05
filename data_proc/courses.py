#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
from itertools import combinations

file_cj = '../organized_data/cj_valid_bystu.csv'
file_course_g3 = '../organized_data/stu_course.csv' # 高三同学选课分布
file_stu_g3 = '../organized_data/stu_g3.csv' # 高三同学选课名单

course_list = ['']

stu_g3_header = ['cla_id',
                 'cla_Name',
                 'mes_StudentID',
                 'course_id',
                 'sub_1',
                 'sub_2',
                 'sub_3']
    
'''
mes_sub_id % 8 + 1
1 地理
2 政治
4 技术
5 物理
6 化学
7 生物
8 历史
'''
course = ['', '地理', '政治', '', '技术', '物理', '化学', '生物', '历史']

course_g3_header = ['course_id',
                    'sub_1',
                    'sub_2',
                    'sub_3',
                    'count']

cj = open(file_cj)
course_g3 = open(file_course_g3, 'w', newline='')
stu_g3 = open(file_stu_g3, 'w', newline='')

# 单科人数统计
course1_count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
course2_count = {1:{2:0, 4:0, 5:0, 6:0, 7:0, 8:0},
                 2:{4:0, 5:0, 6:0, 7:0, 8:0},
                 4:{5:0, 6:0, 7:0, 8:0}, 
                 5:{6:0, 7:0, 8:0}, 
                 6:{7:0, 8:0},
                 7:{8:0}}
course3_count = {1:{2:{4:0, 5:0, 6:0, 7:0, 8:0},
                    4:{5:0, 6:0, 7:0, 8:0},
                    5:{6:0, 7:0, 8:0}, 
                    6:{7:0, 8:0}, 
                    7:{8:0}},
                 2:{4:{5:0, 6:0, 7:0, 8:0},
                    5:{6:0, 7:0, 8:0}, 
                    6:{7:0, 8:0}, 
                    7:{8:0}},
                 4:{5:{6:0, 7:0, 8:0}, 
                    6:{7:0, 8:0}, 
                    7:{8:0}},
                 5:{6:{7:0, 8:0}, 
                    7:{8:0}},
                 6:{7:{8:0}}}

reader = csv.DictReader(cj)
writer_stu = csv.DictWriter(stu_g3, stu_g3_header)
writer_stu.writeheader()

for row_cj in reader:
    if (row_cj['exam_type'] == '6' or row_cj['exam_type'] == '7') \
            and row_cj['mes_sub_name'] in course:
        temp_course = []
        temp_stu_id = row_cj['mes_StudentID']
        temp_cla_id = row_cj['cla_id']
        temp_cla_name = row_cj['cla_Name']
        temp_sub_id = int(row_cj['mes_sub_id']) % 8 + 1
        temp_course.append(temp_sub_id)
        course1_count[temp_sub_id] =  course1_count[temp_sub_id] + 1 
        
        for row_cj in reader:        
            if row_cj['mes_StudentID'] != temp_stu_id:
                temp_course.sort()
                if len(temp_course) == 3:
                    course3_count[temp_course[0]][temp_course[1]][temp_course[2]] \
                        = course3_count[temp_course[0]][temp_course[1]][temp_course[2]] + 1
                    course2_count[temp_course[0]][temp_course[1]] \
                        = course2_count[temp_course[0]][temp_course[1]] + 1
                    course2_count[temp_course[0]][temp_course[2]] \
                        = course2_count[temp_course[0]][temp_course[2]] + 1
                    course2_count[temp_course[1]][temp_course[2]] \
                        = course2_count[temp_course[1]][temp_course[2]] + 1
                elif len(temp_course) == 2:
                    course2_count[temp_course[0]][temp_course[1]] \
                        = course2_count[temp_course[0]][temp_course[1]] + 1
                    temp_course.append(0)

                writer_stu.writerow({'cla_id':temp_cla_id,
                                     'cla_Name':temp_cla_name,
                                     'mes_StudentID':temp_stu_id,
                                     'course_id':str(temp_course[0])+str(temp_course[1])+str(temp_course[2]),
                                     'sub_1':course[temp_course[0]],
                                     'sub_2':course[temp_course[1]],
                                     'sub_3':course[temp_course[2]]}) 
                break;
            if (row_cj['exam_type'] == '6' or row_cj['exam_type'] == '7') \
                    and row_cj['mes_sub_name'] in course \
                    and (int(row_cj['mes_sub_id']) % 8 + 1) not in temp_course:
                temp_sub_id = int(row_cj['mes_sub_id']) % 8 + 1
                temp_course.append(temp_sub_id)
                course1_count[temp_sub_id] =  course1_count[temp_sub_id] + 1 
stu_g3.close()
cj.close()

# 写入分科人数统计文件
writer_course = csv.DictWriter(course_g3, course_g3_header)
writer_course.writeheader()

for i in [1, 2, 4, 5, 6, 7, 8]:
    writer_course.writerow({'course_id':i,
                            'sub_1':course[i],
                            'count':course1_count[i]})
for i in course2_count.keys():
    for j in course2_count[i].keys():
        writer_course.writerow({'course_id':str(i)+str(j),
                                'sub_1':course[i],
                                'sub_2':course[j],
                                'count':course2_count[i][j]})
for i in course3_count.keys():
    for j in course3_count[i].keys():
        for k in course3_count[i][j].keys():
            writer_course.writerow({'course_id':str(i)+str(j)+str(k),
                                    'sub_1':course[i],
                                    'sub_2':course[j],
                                    'sub_3':course[k],
                                    'count':course3_count[i][j][k]})

course_g3.close()
cj.close()
