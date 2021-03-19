"""
this module does all the heavy lifting to the text messages
create a kids class to create a kid and wire  up the grades
"""
import smtplib
import enum
from bs4 import BeautifulSoup
import credentials


class Kids(enum.Enum):
    """ an enum to hold the kids headers """
    oldest = "-----Bella-----"
    middle = "-----Luisa-----"
    youngest = "-----Thomas-----"


class KidsClass:
    """a class to contain all the kids info """
    @classmethod
    def __init__(cls, name, message, email):
        cls.name = name
        cls.message = message
        cls.email = email

    @classmethod
    def create_message(cls, k, email):
        """ create the message for the text message"""
        if not k:
            return ""
        return "From: {}\r\nTo: {}\r\nSubject:{}\r\n{}".format(credentials.LOGIN_EMAIL,
                                                               email,
                                                               k.name,
                                                               k.message)

def send_text(payload):
    """ sending the acutal text to the phone """
    result = {}
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(credentials.LOGIN_EMAIL, credentials.LOGIN_PASS)
    for pay in payload:
        server.sendmail(credentials.LOGIN_EMAIL,
                        credentials.SEND_SELF_EMAIL,
                        pay.create_message(pay, credentials.SEND_SELF_EMAIL))

        server.sendmail(credentials.LOGIN_EMAIL,
                        credentials.SEND_WIFE_EMAIL,
                        pay.create_message(pay, credentials.SEND_WIFE_EMAIL))

        server.sendmail(credentials.LOGIN_EMAIL,
                        pay.email,
                        pay.create_message(pay, pay.email))

    result = {
        credentials.LOGIN_EMAIL:
        (200, "Success")
    }
    return result


def get_grades(response):
    """ rip through the response to create a useful message """
    result = dict()
    all_grades = ""
    soup = BeautifulSoup(response.text, 'html.parser')
    courses = soup.findAll('a', id='courseName')
    grades = soup.findAll('a', id='average')

    for _, (grade, course) in enumerate(zip(grades, courses)):
        result[course.text] = grade.text
    for formatted_courses in result:
        if formatted_courses not in credentials.DONT_CARE_LIST:
            all_grades += "{} | {}\r\n".format(formatted_courses,result[formatted_courses])
    return all_grades
