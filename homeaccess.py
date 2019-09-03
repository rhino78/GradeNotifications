import requests
import notif
import credentials
from bs4 import BeautifulSoup


def main():

    all_grades = []
    with requests.Session() as s:
        s.post(credentials.HOME_ACCESS_POST, data=credentials.INIT_PAYLOAD)
        r = s.get(credentials.HOME_ACCESS_REQUEST, params=credentials.INIT_PAYLOAD)

        if r.status_code != 200:
            print(r.status_code)
            print(r.reason)
            print('initial get failed')
            sys.exit(1)

        middle = notif.kids_class(notif.kids.middle.value, getGrades(r), credentials.SEND_MIDDLE_EMAIL)
        all_grades.append(middle)

        # switch kid profile
        s.post(credentials.HOME_ACCESS_PICKER, data=credentials.SWITCH_PAYLOAD)
        r = s.get(credentials.HOME_ACCESS_REQUEST)
        if r.status_code != 200:
            print(r.status_code)
            print(r.reason)
            print('first switch failed')
            sys.exit(1)

        oldest = notif.kids_class(notif.kids.oldest.value, getGrades(r), credentials.SEND_OLDEST_EMAIL)
        all_grades.append(oldest)

        # now let's grab the third kid:
        s.post(credentials.HOME_ACCESS_PICKER, data=credentials.FINAL_SWITCH_PAYLOAD)
        r = s.get(credentials.HOME_ACCESS_REQUEST)
        if r.status_code != 200:
            print(r.status_code)
            print(r.reason)
            print('second switch failed')
            sys.exit(1)

        youngest = notif.kids_class(notif.kids.youngest.value, getGrades(r), credentials.SEND_YOUNGEST_EMAIL)
        all_grades.append(youngest)
        notif.send_text(all_grades)


def getGrades(r):
    result = dict()
    all_grades = ""
    soup = BeautifulSoup(r.text, 'html.parser')
    courses = soup.findAll('a', id='courseName')
    grades = soup.findAll('a', id='average')

    for i, (g, c) in enumerate(zip(grades, courses)):
        result[c.text] = g.text
    for l in result.keys():
        all_grades += "{} | {}\r\n".format(l, result[l])
    return all_grades


if __name__ == "__main__":
    import sys
    main()
    sys.exit()
