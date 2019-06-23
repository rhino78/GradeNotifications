HOME_ACCESS_USER = 'carolbraus'
HOME_ACCESS_PASS = 'maxine77'
HOME_ACCESS_POST = \
    "https://accesscenter.roundrockisd.org/HomeAccess/Account/LogOn?ReturnUrl=%2fHomeAccess%2fHome%2fWeekView"
HOME_ACCESS_REQUEST = "https://accesscenter.roundrockisd.org/HomeAccess/Home/WeekView"
HOME_ACCESS_PICKER = "https://accesscenter.roundrockisd.org/HomeAccess/Frame/StudentPicker"
HOME_ACCESS_STUDENT_ID_B = 442271
HOME_ACCESS_STUDENT_ID_T = 124429
LOGIN_EMAIL = 'rshave@gmail.com'
LOGIN_PASS = 'Carolina77!'
SEND_SELF_EMAIL = '5127844398@tmomail.net'
SEND_WIFE_EMAIL = '5126899956@tmomail.net'

INIT_PAYLOAD = {
    'Database': 10,
    'LogOnDetails.UserName': HOME_ACCESS_USER,
    'LogOnDetails.Password': HOME_ACCESS_PASS}

SWITCH_PAYLOAD = {'studentId':  HOME_ACCESS_STUDENT_ID_B,
                  'url': '%2FHomeAccess%2FHome%2FWeekView',
                  'url': '%2FHomeAccess%2FHome%2FWeekView',
                  'url': '%2FHomeAccess%2FHome%2FWeekView'}

FINAL_SWITCH_PAYLOAD = {
    'url': '/HomeAccess/Home/WeekView',
    'url': '/HomeAccess/Home/WeekView',
    'studentId': HOME_ACCESS_STUDENT_ID_T,
    'url': '/HomeAccess/Home/WeekView'}
