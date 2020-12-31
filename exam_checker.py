import csv
from collections import namedtuple
import smtplib

Exam = namedtuple('Exam', ['last_name', 'first_name', 'problem1_score', 'problem1_comments',
                           'problem2_score', 'problem2_comments','problem3_score', 'problem3_comments'])

MAIL_SERVER = 'smtp.mail.com'
LOGIN = 'user@mail.com'
PASSWORD = 'XXXXXXXXXX'
MAILFROM = 'user@mail.com'
MESSAGE = 'Mail text'

def get_exams(exam_file):
    with open(exam_file, "r", encoding="utf-8") as data:
        next(data) # skip header
        return {
            line[0] : # email
            Exam(
                last_name=line[1],
                first_name=line[2],
                problem1_score=line[3],
                problem1_comments=line[4],
                problem2_score=line[5],
                problem2_comments=line[6],
                problem3_score=line[7],
                problem3_comments=line[8],
            )
            for line in csv.reader(data)
        }


def send_mail(login, password, mailfrom, mailto, message):
    server = smtplib.SMTP_SSL(MAIL_SERVER, 465)
    server.login(login, password)
    server.sendmail(
        mailfrom,
        mailto,
        message)
    server.quit()


if __name__ == "__main__":
    list_exams=get_exams("exam.csv")
    for k,v in list_exams.items():
        send_mail(login = LOGIN,
                  password = PASSWORD,
                  mailfrom = MAILFROM,
                  mailto = k,
                  message = "Content of message")
        print(f"Sending mail to {k}")

