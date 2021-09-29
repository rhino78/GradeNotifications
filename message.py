"""a message class to handle all things mesage related"""
from datetime import datetime
import random
from bs4 import BeautifulSoup
import credentials

def get_grades(response):
    """return a useful message from the response"""
    result = dict()
    all_grades = ""
    failcount = 0
    soup = BeautifulSoup(response.text, 'html.parser')
    courses = soup.findAll('a', id='courseName')
    grades = soup.findAll('a', id='average')

    for _, (grade, course) in enumerate(zip(grades, courses)):
        if grade.text:
            print(grade.text)
            #in one case we had a 'P' for passing
            #we need to account for that
            if 'P' in grade.text:
                intgrade = 100
            else:
                intgrade = int(grade.text.strip())

            if intgrade < 70:
                failcount += 1
        result[course.text] = grade.text
    for formatted_courses in result:
        if formatted_courses not in credentials.DONT_CARE_LIST:
            all_grades += "{} | {}\r\n".format(formatted_courses, result[formatted_courses])

    if failcount > 0:
        all_grades += "--------------------\r\n"
        if failcount ==1 :
            all_grades += "You are failing {} class\r\n".format(failcount)
        else:
            all_grades += "You are failing {} classes\r\n".format(failcount)

        all_grades += \
                "There are {} days until the end of the grading period\r\n"\
                .format(get_delta(get_end_of_grading()))
    else:
        all_grades += "--------------------\r\n"
        all_grades += "Your grades are {}".format(get_rand_compliment())

    return all_grades

def get_rand_compliment():
    """get a random compliment for the kiddo"""
    return credentials.COMPLIMENTS[random.randint(0, len(credentials.COMPLIMENTS)-1)]


def get_end_of_grading():
    """get the current grading periiod end date"""
    for g_grades in credentials.GRADING_PERIOD:
        if datetime.now() < g_grades:
            return g_grades
    return None

def get_delta(d_date):
    """returns the difference in days between today and d_date"""
    return (d_date - datetime.now()).days
