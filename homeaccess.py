"""
grade notifications our main class to connect to home access center and
send the grades to kids and parents
"""
import requests
from bs4 import BeautifulSoup
import message
import notif
import credentials


def main():
    """our main to get into home access center"""
    all_grades = []
    with requests.Session() as session:
        site = session.get(credentials.HOME_ACCESS_POST)
        bs_content = BeautifulSoup(site.content, "html.parser")

        token = bs_content.find(
            "input", {"name": "__RequestVerificationToken"}).get('value')

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
                                 message.get_grades(response),
                                 credentials.SEND_MIDDLE_TEXT)

        if len(middle.message) > 0:
            all_grades.append(middle)

        # switch kid profile
        session.post(credentials.HOME_ACCESS_PICKER,
                     data=credentials.FINAL_SWITCH_PAYLOAD)
        response = session.get(credentials.HOME_ACCESS_REQUEST)

        if response.status_code != 200:
            print(response.status_code)
            print(response.reason)
            print('second switch failed')
            sys.exit(1)

        youngest = notif.KidsClass(notif.Kids.youngest.value,
                                   message.get_grades(response),
                                   credentials.SEND_YOUNGEST_TEXT)

        if len(youngest.message) > 0:
            all_grades.append(youngest)

        #adding in a safeguard to prevent periods where there are no grades
        #not to send a message
        if len(all_grades) > 0:
            notif.send_twilio(all_grades)


if __name__ == "__main__":
    import sys
    main()
