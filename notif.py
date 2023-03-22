"""
this module does all the heavy lifting to the text messages
create a kids class to create a kid and wire  up the grades
"""
import enum
import credentials
from twilio.rest import Client


class Kids(enum.Enum):
    """ an enum to hold the kids headers """
    middle = "-----Luisa-----\r\n"
    youngest = "-----Thomas-----\r\n"


class KidsClass:
    """a class to contain all the kids info """

    def __init__(self, name, message, phone):
        self.name = name
        self.message = message
        self.phone = phone

    @staticmethod
    def create_message(k, phone):
        """ create the message for the text message"""
        if not k:
            return ""
        return "{}{}".format(k.name, k.message)


def send_twilio(payload):
    """ sending the acutal text to the phone """
    account_sid = credentials.ACCOUNT_SID
    auth_token = credentials.AUTH_TOKEN
    client = Client(account_sid, auth_token)
    for pay in payload:
        client.messages.create(to=credentials.SEND_SELF_TEXT,
                               from_=credentials.TWILIO_PHONE,
                               body=pay.create_message(pay, credentials.SEND_SELF_TEXT))

        client.messages.create(to=credentials.SEND_WIFE_TEXT,
                               from_=credentials.TWILIO_PHONE,
                               body=pay.create_message(pay, credentials.SEND_WIFE_TEXT))

        client.messages.create(to=pay.phone,
                               from_=credentials.TWILIO_PHONE,
                               body=pay.create_message(pay, pay.phone))


def print_only(payload):
    """a method to print the message text for testing"""
    for p in payload:
        print(p.create_message(p, p.phone))
