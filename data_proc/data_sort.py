import csv

file_stu = '../education_data/2_student_info.csv'

out_stu_925 = '../organized_data/out_stu_925.csv'

headers_stu_925 = ['cla_id', 'cla_Name', 'bf_StudentID']
datas_stu_925 = []

with open(file_stu) as stu_csv:
    reader = csv.DictReader(stu_csv)
    for row in reader:
        if row['cla_id']=='925':
            datas_stu_925.append({'cla_id':'925', 'cla_Name':row['cla_Name'], 'bf_StudentID':row['\ufeffbf_StudentID']})

with open(out_stu_925, 'w', newline='') as out_csv:
    writer = csv.DictWriter(out_csv, headers_stu_925)
    writer.writeheader()
    for row in datas_stu_925:
        writer.writerow(row)



