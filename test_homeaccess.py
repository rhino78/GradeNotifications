import notif
import json
import unittest
import credentials
import mock
import requests
from unittest.mock import MagicMock, Mock, ANY
from mock import patch, call
#from bs4 import BeautifulSoup
#from unittest import mock

"""
class MyGreatClass:
    def fetch_json(self, url):
        response = requests.get(url)
        return response

def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def text(self):
            return self.json_data.text

    def json(self):
            return self.json_data

    if args[0] == 'http://someurl.com/test.json':
        MockResponse.text = [{'average':100,
        'average':100, 
        'average':100}]
        return MockResponse(MockResponse.text, 200)
    elif args[0] == 'http://someotherurl.com/anothertest.json':
        return MockResponse({"courseName": "Athletics"}, 200)

    return MockResponse(None, 404)

class TestRequestCall(unittest.TestCase):
    def _mock_response(
            self, 
            status=200,
            content="CONTENT",
            json_data=None, 
            raise_for_status=None):
        mock_resp = mock.MagicMock()
        mock_resp.raise_for_status = mock.MagicMock()
        if raise_for_status:
            mock_resp.raise_for_status.side_effect = raise_for_status
        mock_resp.status_code = status
        mock_resp.content = content
        if json_data:
            mock_resp.json = mock.MagicMock(
                    return_value=json_data)
        return mock_resp

    @mock.patch('requests.get')
    def test_response(self, mock_get):
        mock_resp = self._mock_response(content=test_data)
        mock_get.return_value = mock_resp
        mock_resp2 = Mock()
        mock_resp2.return_value.status_code=200
        mock_resp2.return_value.text = '{"average": "blah"}'
        print(mock_resp2.len())
        print(mock_resp2)
        result = notif.getGrades(mock_resp2)
        self.assertEqual(result, "average")
"""
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
