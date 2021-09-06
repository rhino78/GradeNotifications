"""
grade notifications our main class to connect to home access center and
send the grades to kids and parents
"""
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import notif
import credentials


def main():
    """our main to get into home access center"""
    all_grades = []
    with requests.Session() as session:
        site = session.get(credentials.HOME_ACCESS_POST)
        bs_content = BeautifulSoup(site.content, "html.parser")
        token = bs_content.find("input", {"name": "__RequestVerificationToken"})["value"]
        login_data = {"__RequestVerificationToken": token,
                      "Database": 10,
                      "LogOnDetails.UserName": credentials.USERNAME,
                      "LogOnDetails.Password": credentials.PASSWORD
                      }

        session.post(credentials.HOME_ACCESS_POST, login_data)
        response = session.get(credentials.HOME_ACCESS_WEEK_VIEW)

        if response.status_code != 200:
            print(response.status_code)
            print(response.reason)
            print('initial get failed')
            sys.exit(1)

        middle = notif.KidsClass(notif.Kids.middle.value,
                get_grades(response),
                credentials.SEND_MIDDLE_EMAIL)

        all_grades.append(middle)

        # switch kid profile
        session.post(credentials.HOME_ACCESS_PICKER, data=credentials.SWITCH_PAYLOAD)
        response = session.get(credentials.HOME_ACCESS_REQUEST)
        if response.status_code != 200:
            print(response.status_code)
            print(response.reason)
            print('first switch failed')
            sys.exit(1)

        oldest = notif.KidsClass(notif.Kids.oldest.value,
                get_grades(response),
                credentials.SEND_OLDEST_EMAIL)

        all_grades.append(oldest)

        # now let's grab the third kid:
        session.post(credentials.HOME_ACCESS_PICKER, data=credentials.FINAL_SWITCH_PAYLOAD)
        response = session.get(credentials.HOME_ACCESS_REQUEST)
        if response.status_code != 200:
            print(response.status_code)
            print(response.reason)
            print('second switch failed')
            sys.exit(1)

        youngest = notif.KidsClass(notif.Kids.youngest.value,
                get_grades(response),
                credentials.SEND_YOUNGEST_EMAIL)

        all_grades.append(youngest)
        notif.send_text(all_grades)


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
        all_grades += "Your grades are BUSSIN"


    return all_grades

def get_end_of_grading():
    """get the current grading periiod end date"""
    for g_grades in credentials.GRADING_PERIOD:
        if datetime.now() < g_grades:
            return g_grades
    return None

def get_delta(d_date):
    """returns the difference in days between today and d_date"""
    return (d_date - datetime.now()).days

if __name__ == "__main__":
    import sys
    main()
