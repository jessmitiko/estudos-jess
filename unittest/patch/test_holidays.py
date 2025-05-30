import unittest
from unittest.mock import patch

from requests.exceptions import Timeout
from holidays import get_holidays

class TestHolydays(unittest.TestCase):
    @patch('holidays.requests')
    def test_get_holydays_timeout(self, mock_requests):
        mock_requests.get.side_effect = Timeout
        
        with self.assertRaises(Timeout):
            get_holidays()
            mock_requests.get.assert_called_once()

if __name__ == '__main__':
    unittest.main()