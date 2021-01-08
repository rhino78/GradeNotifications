import smtplib
import credentials
import enum
import requests
from bs4 import BeautifulSoup


class Kids(enum.Enum):
    oldest = "-----Bella-----"
    middle = "-----Luisa-----"
    youngest = "-----Thomas-----"


class Error(object):
    def __init__(self, d):
        self.instance_dict = d


class KidsClass:
    def __init__(self, name, message, email):
        self.name = name
        self.message = message
        self.email = email

    def create_message(self, k, email):
        return "From: {}\r\nTo: {}\r\nSubject:{}\r\n{}".format(credentials.LOGIN_EMAIL,
                                                               email,
                                                               k.name,
                                                               k.message)


def send_text(payload):
    # oops, we don't return anything here
    # how do we retun a result on a list?
    result = {}
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(credentials.LOGIN_EMAIL, credentials.LOGIN_PASS)
        for p in payload:
            server.sendmail(credentials.LOGIN_EMAIL,
                            credentials.SEND_SELF_EMAIL,
                            p.create_message(p, credentials.SEND_SELF_EMAIL))

            server.sendmail(credentials.LOGIN_EMAIL,
                            credentials.SEND_WIFE_EMAIL,
                            p.create_message(p, credentials.SEND_WIFE_EMAIL))

            server.sendmail(credentials.LOGIN_EMAIL,
                            p.email,
                            p.create_message(p, p.email))

        result = {
            credentials.LOGIN_EMAIL:
            (200, "Success")
        }
        return (result)

    except Exception as e:
        result = {
            credentials.LOGIN_EMAIL:
            (str(e))
        }
        return(result)

def getGrades(r):
    result = dict()
    all_grades = ""
    soup = BeautifulSoup(r.text, 'html.parser')
    courses = soup.findAll('a', id='courseName')
    grades = soup.findAll('a', id='average')

    for i, (g, c) in enumerate(zip(grades, courses)):
        result[c.text] = g.text
    for l in result.keys():
        if l not in credentials.DONT_CARE_LIST:
            all_grades += "{} | {}\r\n".format(l, result[l])
    return all_grades
