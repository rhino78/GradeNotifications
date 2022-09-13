"""our fancy unit testing suite"""
import unittest

from mock import patch
import requests
import requests_mock

import message
import notif
import credentials


class TestHomeAccess(unittest.TestCase):

    def test_actual_message(self):
        """we need a test to just print out the actual grades"""

        test_list = []
        with requests_mock.Mocker() as m:
            test_url = "http://test.com"
            m.get(test_url, text="<a id="'average'">0</a> <a id="'courseName'">test subject</a>\
                        <a id="'average'">0</a> <a id="'courseName'">test subject2</a>")

            response = requests.get(test_url)
            middle = notif.KidsClass(notif.Kids.middle.value,
                                     message.get_grades(response),
                                     credentials.SEND_MIDDLE_TEXT)

            test_list.append(middle)

            notif.print_only(test_list)
            self.assertIsNotNone(middle)

    def test_eog(self):
        test = message.get_end_of_grading()
        print("the end of the grading would be: {}\r\n".format(test))

    def test_message_fail_result(self):
        """here we want to make sure that the special text is in fail the response """
        with requests_mock.Mocker() as m:
            test_url = "http://test.com"
            m.get(test_url, text="<a id="'average'">0</a> <a id="'courseName'">test subject</a>\
                    <a id="'average'">0</a> <a id="'courseName'">test subject2</a>")
            result = requests.get(test_url)
            test = message.get_grades(result)
            print(test)
            self.assertIn("failing", test)

    def test_message_pass_result(self):
        """here we want to make sure that the special text is in pass the response """
        with requests_mock.Mocker() as m:
            test_url = "http://test.com"
            m.get(test_url, text="<a id="'average'">100</a> <a id="'courseName'">test subject</a>"
                  "<a id="'average'">P</a> <a id="'courseName'">test subject2</a>")
            result = requests.get(test_url)
            test = message.get_grades(result)
            print(notif.Kids.youngest.value + test)
            self.assertIn("grades", test)

    def test_init(self):
        middle = notif.KidsClass("frank", "poop", "nobody@nowhere.com")
        self.assertIsNotNone(middle)

    def test_createMessage(self):
        middle = notif.KidsClass("frank", "poop", "nobody@nowhere.com")
        result = middle.create_message(middle, "test@email")
        self.assertIsNotNone(result)

    @patch("smtplib.SMTP")
    def test_refused(self, mock_smtp):
        to_addresses = ["nobody@nowhere.com", "nobody@nowhere.com"]

        error = {
            to_addresses[0]:
            (450, "Requested mail action not taken: mailbox unavailable")
        }
        instance = mock_smtp.return_value
        instance.notif.send_text.return_value = error
        payload = []
        payload.append(notif.KidsClass("frank", "poop", "nobody@nowhere.com"))
        # currently not returning anything here
        result = instance.notif.send_text(payload)
        self.assertIsInstance(result, dict)
        self.assertEqual(result, error)


if __name__ == '__main__':
    unittest.main()
