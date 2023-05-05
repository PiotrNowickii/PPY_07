import smtplib
from email.mime.text import MIMEText

import MyLinkedList
import Student


def save_changes(student_list):
    save_path = 'data_saved.txt'
    with open(save_path, "w") as file_object_saver:
        for curr_student in student_list:
            tmp = curr_student.email + ',' + curr_student.name + ',' + curr_student.surname + ',' + str(curr_student.all_grade.get('project')) + ',' + str(curr_student.all_grade.get('l_1')) + ',' + str(curr_student.all_grade.get('l_2')) + ',' + str(curr_student.all_grade.get('l_3')) + ',' + str(curr_student.all_grade.get('h_1')) + ',' + str(curr_student.all_grade.get('h_2')) + ',' + str(curr_student.all_grade.get('h_3')) + ',' + str(curr_student.all_grade.get('h_4')) + ',' + str(curr_student.all_grade.get('h_5')) + ',' + str(curr_student.all_grade.get('h_6')) + ',' + str(curr_student.all_grade.get('h_7')) + ',' + str(curr_student.all_grade.get('h_8')) + ',' + str(curr_student.all_grade.get('h_9')) + ',' + str(curr_student.all_grade.get('h_10')) + ',' + str(curr_student.all_grade.get('grade'))

            file_object_saver.write(tmp + '\n')


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipients
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()


def grade_students(student_list):
    for studentt in student_list:
        if 'GRADED' not in studentt.status and 'MAILED' not in studentt.status:
            for k, v in studentt.all_grade.items():
                if v == '-1':
                    studentt.all_grade[k] = 0
            h_average = (int(studentt.all_grade.get('h_1')) + int(studentt.all_grade.get(
                'h_2')) + int(studentt.all_grade.get('h_3')) + int(studentt.all_grade.get(
                'h_4')) + int(studentt.all_grade.get('h_5')) + int(studentt.all_grade.get(
                'h_6')) + int(studentt.all_grade.get('h_7')) + int(studentt.all_grade.get(
                'h_8')) + int(studentt.all_grade.get('h_9')) + int(studentt.all_grade.get('h_10'))) / 10
            if h_average >= 60:
                studentt.all_grade['l_1'] = 20
            if h_average >= 70:
                studentt.all_grade['l_2'] = 20
            if h_average >= 80:
                studentt.all_grade['l_3'] = 20
            grade = int(studentt.all_grade.get('project')) + int(studentt.all_grade.get(
                'l_1')) + int(studentt.all_grade.get('l_1')) + int(studentt.all_grade.get('l_1'))
            if grade >= 91:
                studentt.all_grade['grade'] = str(5)
            elif 91 > grade >= 81:
                studentt.all_grade['grade'] = str(4.5)
            elif 81 > grade >= 71:
                studentt.all_grade['grade'] = str(4)
            elif 71 > grade >= 61:
                studentt.all_grade['grade'] = str(3.5)
            elif 61 > grade >= 51:
                studentt.all_grade['grade'] = str(3)
            else:
                studentt.all_grade['grade'] = str(2)
            studentt.status = 'GRADED'


def student_remover(student_list, email):
    for student_check in student_list:
        if student_check.email == email:
            print(student_check)
            student_list.delete(student_check)
            print('Student removed')
            return
    print('Student doesnt exist')


def student_adder(student_list, curr_line):
    curr_line = curr_line.rstrip().rsplit(',')
    for student_check in student_list:
        if curr_line[0] in student_check.email:
            print('Student already exists')
            return
    if len(curr_line) >= 18:
        grade_list = {
            "project": curr_line[3],
            "l_1": curr_line[4],
            "l_2": curr_line[5],
            "l_3": curr_line[6],
            "h_1": curr_line[7],
            "h_2": curr_line[8],
            "h_3": curr_line[9],
            "h_4": curr_line[10],
            "h_5": curr_line[11],
            "h_6": curr_line[12],
            "h_7": curr_line[13],
            "h_8": curr_line[14],
            "h_9": curr_line[15],
            "h_10": curr_line[16],
            "grade": curr_line[17],
        }
    if len(curr_line) <= 17:
        student = Student.Student(curr_line[0], curr_line[1], curr_line[2])
        student_list.append(student)
    elif len(curr_line) == 18:
        student = Student.Student(curr_line[0], curr_line[1], curr_line[2], grade_list)
        student_list.append(student)
    elif len(curr_line) == 19:
        student = Student.Student(curr_line[0], curr_line[1], curr_line[2], grade_list, curr_line[18])
        student_list.append(student)




filepath = "ocenystudenci.txt"
students = MyLinkedList.MyLinkedList()
with open(filepath) as file_object:
    for line in file_object:
        student_adder(student_list=students, curr_line=line)
file_object.close()
while True:
    checker = input('Do you want to input more students? y - yes, anything else - no\n')
    if checker == 'y':
        line = input('Please input data seperated by commas (e.g. asd@gmail.com,mark,johnson,41)\n')
        student_adder(student_list=students, curr_line=line)
    else:
        break
while True:
    checker = input('Do you want to delete students? y - yes, anything else - no\n')
    if checker == 'y':
        mail = input('Please input email of student you want to delete\n')
        student_remover(student_list=students, email=mail)
    else:
        break
grade_students(student_list=students)
save_changes(student_list=students)
for student in students:
    if 'MAILED' not in student.status:
        subject = 'Python email'
        body = 'You got a grade based on the amount of points you got. Your grade: ' + \
               student.all_grade['grade']
        sender = "sender"
        recipients = student.email
        password = "password"
        send_email(subject, body, sender, recipients, password)
        student.status = 'MAILED'
