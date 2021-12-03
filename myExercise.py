import sys
student_dic = {}
with open("student.txt") as students:
    for line in students:
        student, records = line.split(":")
        student_dic[student] = records.strip("\n")
students_to_check = sys.argv[1].split(",")
for i in students_to_check:
    try:
        print("Name: {}, University: {}".format(i, student_dic[i]))
    except KeyError:
        print("No record of '{}' found".format(i))