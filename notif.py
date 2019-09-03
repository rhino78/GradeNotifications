import smtplib
import credentials
import enum


class kids(enum.Enum):
    oldest = "-----Bella-----"
    middle = "-----Luisa-----"
    youngest = "-----Thomas-----"


class kids_class:
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

    except Exception as e:
        print(e)

