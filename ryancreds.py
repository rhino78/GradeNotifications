"""placeholder for all things private"""
import datetime
# -----REQUEST INFO-----
HOME_ACCESS_POST = "https://accesscenter.roundrockisd.org/HomeAccess/Account/LogOn?ReturnUrl=%2fHomeAccess%2f"

HOME_ACCESS_REQUEST = "https://accesscenter.roundrockisd.org/HomeAccess/Account/LogOn?ReturnUrl=%2fhomeaccess%2f"

HOME_ACCESS_WEEK_VIEW = "https://accesscenter.roundrockisd.org/HomeAccess/Home/WeekView"
USERNAME = "carolbraus"
PASSWORD = "maxine77"

SWITCH_PAYLOAD = {'studentId': 442271,
                  'url': '/HomeAccess/Home/WeekView',
                  'url': '/HomeAccess/Home/WeekView',
                  'url': '/HomeAccess/Home/WeekView'}

FINAL_SWITCH_PAYLOAD = {
    'url': '/HomeAccess/Home/WeekView',
    'url': '/HomeAccess/Home/WeekView',
    'studentId': 124429,
    'url': '/HomeAccess/Home/WeekView'}

HOME_ACCESS_PICKER = "https://accesscenter.roundrockisd.org/HomeAccess/Frame/StudentPicker"
DONT_CARE_LIST = ["ADA Funding",  "Advisory/Lunch", "Off Campus"]

# -----LOGIN INFO-----
# note that I had to create a special PW in my google account
TWILIO_PHONE = "+14454474574"
LOGIN_EMAIL = "rshave@gmail.com"
LOGIN_PASS = "mekcdeikvrrfzlbc"
SEND_SELF_TEXT = "+15127844398"
SEND_WIFE_TEXT = "+15126899956"
SEND_YOUNGEST_TEXT = "+15124008783"
SEND_MIDDLE_TEXT = "+15129861327"
# SEND_OLDEST_TEXT = "+15122254619"
SEND_SELF_EMAIL = "5127844398@tmomail.net"
SEND_WIFE_EMAIL = "5126899956@tmomail.net"
SEND_YOUNGEST_EMAIL = "5124008783@tmomail.net"
SEND_MIDDLE_EMAIL = "5129861327@tmomail.net"
# SEND_OLDEST_EMAIL = "5122254619@tmomail.net"

# -----GRADING PERIOD INFO-----
GRADING_PERIOD = [
    datetime.datetime(2022, 10, 14),
    datetime.datetime(2022, 12, 15),
    datetime.datetime(2023, 3, 10),
    datetime.datetime(2023, 5, 25)
]

ACCOUNT_SID = "ACde86a2fb487cef3ec452719abcd8552a"
AUTH_TOKEN = "e91f1967405177f056210b20e3e97f3e"

COMPLIMENTS = ["BUSSIN",
               "admirable",
               "brilliant",
               "distinguished",
               "exceptional",
               "exquisite",
               "fantastic",
               "glorious",
               "gorgeous",
               "grand",
               "great",
               "heroic",
               "impressive",
               "magnificent",
               "marvelous",
               "outstanding",
               "remarkable",
               "sublime",
               "superb",
               "superlative",
               "wonderful",
               "celebrated",
               "divine",
               "eminent",
               "fine",
               "first-class",
               "matchless",
               "peerless",
               "premium",
               "proud",
               "rare",
               "renowned",
               "resplendent",
               "royal",
               "splendiferous",
               "splendorous",
               "sterling",
               "supreme",
               "transcendent",
               "unparalleled",
               "unsurpassed",
               ]
