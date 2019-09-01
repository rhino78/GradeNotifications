import requests
import notif
import credentials
from bs4 import BeautifulSoup


def main():
    t_grades = dict()
    l_grades = dict()
    b_grades = dict()

    with requests.Session() as s:
        s.post(credentials.HOME_ACCESS_POST, data=credentials.INIT_PAYLOAD)
        r = s.get(credentials.HOME_ACCESS_REQUEST, params=credentials.INIT_PAYLOAD)

        if r.status_code != 200:
            print(r.status_code)
            print(r.reason)
            print('initial get failed')
            sys.exit(1)

        courses, grades = getcoursegrades(r)

        for i, (g, c) in enumerate(zip(grades, courses)):
            l_grades[c.text] = g.text

        all_grades = '-----Luisa-----\r\n'
        for l in l_grades.keys():
            all_grades += "{} | {}\r\n".format(l, l_grades[l])

        notif.send_notification(all_grades, notif.kids.middle)

        # switch kid profile
        s.post(credentials.HOME_ACCESS_PICKER, data=credentials.SWITCH_PAYLOAD)
        r = s.get(credentials.HOME_ACCESS_REQUEST)
        if r.status_code != 200:
            print(r.status_code)
            print(r.reason)
            print('first switch failed')
            sys.exit(1)

        courses, grades = getcoursegrades(r)

        for i, (g, c) in enumerate(zip(grades, courses)):
            b_grades[c.text] = g.text

        all_grades = '-----Bella-----\r\n'
        for b in b_grades.keys():
            all_grades += "{} | {}\r\n".format(b, b_grades[b])

        notif.send_notification(all_grades, notif.kids.oldest)

        # now let's grab the third kid:
        s.post(credentials.HOME_ACCESS_PICKER, data=credentials.FINAL_SWITCH_PAYLOAD)
        r = s.get(credentials.HOME_ACCESS_REQUEST)
        if r.status_code != 200:
            print(r.status_code)
            print(r.reason)
            print('second switch failed')
            sys.exit(1)

        courses, grades = getcoursegrades(r)

        for i, (g, c) in enumerate(zip(grades, courses)):
            t_grades[c.text] = g.text

        all_grades = '-----Thomas-----\r\n'
        for t in t_grades.keys():
            all_grades += "{} | {}\r\n".format(t, t_grades[t])

        notif.send_notification(all_grades, notif.kids.youngest)


def getcoursegrades(r):
    soup = BeautifulSoup(r.text, 'html.parser')
    courses = soup.findAll('a', id='courseName')
    grades = soup.findAll('a', id='average')
    return courses, grades


if __name__ == "__main__":
    import sys
    main()
    sys.exit()
