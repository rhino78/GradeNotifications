import smtplib
import credentials


def send_notification(payload):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(credentials.LOGIN_EMAIL, credentials.LOGIN_PASS)
    message = \
        "From: {}\r\nTo: {}\r\nSubject: \r\n{}".format(credentials.LOGIN_EMAIL, credentials.SEND_SELF_EMAIL, payload)
    server.sendmail(credentials.LOGIN_EMAIL, credentials.SEND_SELF_EMAIL, message)
    message = \
        "From: {}\r\nTo: {}\r\nSubject: \r\n{}".format(credentials.LOGIN_EMAIL, credentials.SEND_WIFE_EMAIL, payload)
    server.sendmail(credentials.LOGIN_EMAIL, credentials.SEND_WIFE_EMAIL, message)
