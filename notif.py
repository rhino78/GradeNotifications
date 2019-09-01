import smtplib
import credentials
import enum


class kids(enum.Enum):
    oldest = 1
    middle = 2
    youngest = 3


def send_notification(payload, kids):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(credentials.LOGIN_EMAIL, credentials.LOGIN_PASS)
        message = \
            "From: {}\r\nTo: {}\r\nSubject: \r\n{}".format(credentials.LOGIN_EMAIL,
                                                           credentials.SEND_SELF_EMAIL,
                                                           payload)

        server.sendmail(credentials.LOGIN_EMAIL, credentials.SEND_SELF_EMAIL, message)

        message = \
            "From: {}\r\nTo: {}\r\nSubject: \r\n{}".format(credentials.LOGIN_EMAIL,
                                                           credentials.SEND_WIFE_EMAIL,
                                                           payload)

        server.sendmail(credentials.LOGIN_EMAIL, credentials.SEND_WIFE_EMAIL, message)

        if kids == kids.oldest:
            message = \
                "From: {}\r\nTo: {}\r\nSubject: \r\n{}".format(credentials.LOGIN_EMAIL,
                                                               credentials.SEND_WIFE_EMAIL,
                                                               payload)

            server.sendmail(credentials.LOGIN_EMAIL, credentials.SEND_OLDEST_EMAIL, message)

        if kids == kids.middle:
            message = \
                "From: {}\r\nTo: {}\r\nSubject: \r\n{}".format(credentials.LOGIN_EMAIL,
                                                               credentials.SEND_WIFE_EMAIL,
                                                               payload)

            server.sendmail(credentials.LOGIN_EMAIL, credentials.SEND_MIDDLE_EMAIL, message)

        if kids == kids.youngest:
            message = \
                "From: {}\r\nTo: {}\r\nSubject: \r\n{}".format(credentials.LOGIN_EMAIL,
                                                               credentials.SEND_WIFE_EMAIL,
                                                               payload)

            server.sendmail(credentials.LOGIN_EMAIL, credentials.SEND_YOUNGEST_EMAIL, message)

    except Exception as e:
        print(e)


