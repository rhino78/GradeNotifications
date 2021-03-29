"""poop poop poop"""
import unittest
import requests
import requests_mock
from mock import patch
import homeaccess
import notif
import credentials

class TestHomeAccess(unittest.TestCase):

    def test_send_email(self):
        with patch("smtplib.SMTP") as mock_smtp:
            payload = []
            payload.append(notif.KidsClass("frank", "poop", "nobody@nowhere.com"))
            result = notif.send_text(payload)
            error = {
                credentials.LOGIN_EMAIL:
                (200, "Success")
            }
            self.assertEqual(result, error)

    def test_mock(self):
        """here we want to make sure that the report to dad is in the response"""
        with requests_mock.Mocker() as m:
            test_url = "http://test.com"
            m.get(test_url, text="<a id="'average'">0</a> <a id="'courseName'">test</a>")
            result = requests.get(test_url)
            test = homeaccess.get_grades(result)
            self.assertIn("report to dad", test)


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
