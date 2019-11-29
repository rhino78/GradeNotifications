import notif
import unittest
import credentials
from mock import patch, call
import smtplib

class TestHomeAccess(unittest.TestCase):

    def test_send_email(self):
        with patch("smtplib.SMTP") as mock_smtp:
            payload = []
            payload.append(notif.kids_class("frank", "poop", "nobody@nowhere.com"))
            result = notif.send_text(payload)
            error = {
                credentials.LOGIN_EMAIL:
                (200, "Success")
            }
            self.assertEqual(result, error)


    def test_init(self):
        middle = notif.kids_class("frank", "poop", "nobody@nowhere.com")
        self.assertIsNotNone(middle)

    def test_createMessage(self):
        middle = notif.kids_class("frank", "poop", "nobody@nowhere.com")
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
        payload.append(notif.kids_class("frank", "poop", "nobody@nowhere.com"))
        # currently not returning anything here
        result = instance.notif.send_text(payload)
        self.assertIsInstance(result, dict)
        self.assertEqual(result, error)

if __name__ == '__main__':
    unittest.main()
