import csv

# input file
file_cj = '../education_data/5_chengji.csv'
file_stu = '../education_data/2_student_info.csv'

# output file
cj_valid = '../organized_data/cj_valid.csv'
cj_invalid = '../organized_data/cj_invalid.csv'

stu_dict = {}
with open(file_stu) as stu_in:
    reader_stu = csv.DictReader(stu_in)
    for row in reader_stu:
        stu_dict[row['\ufeffbf_StudentID']] = {'cla_id':row['cla_id'], 'cla_Name':row['cla_Name']}

header_cj_valid = ['cla_id', 'cla_Name',
                   'mes_sub_id', 'mes_sub_name',
                   'exam_number', 'exam_numname', 'exam_type', 'exam_sdate', 'mes_TestID',
                   'mes_StudentID', 'mes_Score','mes_Z_Score', 'mes_T_Score', 'mes_dengdi']
list_cj_valid = []

header_cj_invalid =['cla_id', 'cla_Name',
                   'mes_sub_id', 'mes_sub_name',
                   'exam_number', 'exam_numname', 'exam_type', 'exam_sdate', 'mes_TestID',
                   'mes_StudentID', 'mes_Score']
list_cj_invalid = []

cj_in = open(file_cj)
cj_out_v = open(cj_valid, 'w', newline = '')
cj_out_i = open(cj_invalid, 'w', newline='')

reader_cj = csv.DictReader(cj_in)
header_cj_in = reader_cj.fieldnames

# write header
writer_v = csv.DictWriter(cj_out_v, header_cj_valid)
writer_v.writeheader()
writer_i = csv.DictWriter(cj_out_i, header_cj_invalid)
writer_i.writeheader()

for row_in in reader_cj: 
    if row_in['mes_StudentID'] in stu_dict.keys():
        if float(row_in['mes_Score']) >= 0:
            writer_v.writerow({'cla_id':stu_dict[row_in['mes_StudentID']]['cla_id'],
                               'cla_Name':stu_dict[row_in['mes_StudentID']]['cla_Name'],
                               'mes_sub_id':row_in['mes_sub_id'],
                               'mes_sub_name':row_in['mes_sub_name'],
                               'exam_number':row_in['exam_number'],
                               'exam_numname':row_in['exam_numname'],
                               'exam_type':row_in['exam_type'],
                               'exam_sdate':row_in['exam_sdate'],
                               'mes_TestID':row_in[header_cj_in[0]],
                               'mes_StudentID':row_in['mes_StudentID'],
                               'mes_Score':row_in['mes_Score'],
                               'mes_Z_Score':row_in['mes_Z_Score'],
                               'mes_T_Score':row_in['mes_T_Score'],
                               'mes_dengdi':row_in['mes_dengdi']})
        else:
            writer_i.writerow({'cla_id':stu_dict[row_in['mes_StudentID']]['cla_id'],
                               'cla_Name':stu_dict[row_in['mes_StudentID']]['cla_Name'],
                               'mes_sub_id':row_in['mes_sub_id'],
                               'mes_sub_name':row_in['mes_sub_name'],
                               'exam_number':row_in['exam_number'],
                               'exam_numname':row_in['exam_numname'],
                               'exam_type':row_in['exam_type'],
                               'exam_sdate':row_in['exam_sdate'],
                               'mes_TestID':row_in[header_cj_in[0]],
                               'mes_StudentID':row_in['mes_StudentID'],
                               'mes_Score':row_in['mes_Score']})

cj_in.close()
cj_out_v.close()
cj_out_i.close()

