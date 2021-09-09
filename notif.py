"""
this module does all the heavy lifting to the text messages
create a kids class to create a kid and wire  up the grades
"""
import smtplib
import enum
import credentials

class Kids(enum.Enum):
    """ an enum to hold the kids headers """
    oldest = "-----Bella-----\r\n"
    middle = "-----Luisa-----\r\n"
    youngest = "-----Thomas-----\r\n"

class KidsClass:
    """a class to contain all the kids info """
    def __init__(self, name, message, email):
        self.name = name
        self.message = message
        self.email = email

    @staticmethod
    def delete_message(msg):
        """delete message"""
        msg = None
        return msg

    @staticmethod
    def create_message(k, email):
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
