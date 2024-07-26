import unittest
from unittest.mock import mock_open, patch
from src.utils import load_items, get_random_item, get_random_quote, get_header, get_device_info, get_battery_status, get_storage_usage

class TestMOTD(unittest.TestCase):
    """
    Unit tests for the Termux RAD MOTD package.
    """

    def setUp(self):
        """
        Set up common test data and mocks.
        """
        self.items_data = 'item1\nitem2\nitem3\n'
        self.header_data = 'Welcome to Termux!\nYour daily dose of motivation:\n'
        self.quote_data = '"Success is not final, failure is not fatal: It is the courage to continue that counts." - Winston Churchill\n'
        self.mock_command_output = 'Mocked Output'

    def _mock_open(self, data):
        """
        Helper function to mock file opening.

        Args:
            data (str): Data to be returned by the mock file.

        Returns:
            mock_open: Mocked open function.
        """
        return mock_open(read_data=data)

    def _patch_subprocess(self, mock_run):
        """
        Helper function to patch subprocess.run.

        Args:
            mock_run (Mock): Mock object for subprocess.run.

        Returns:
            Mock: Patched subprocess.run.
        """
        mock_run.return_value.stdout = self.mock_command_output

    @patch('builtins.open', new_callable=_mock_open, data='item1\nitem2\nitem3\n')
    def test_load_items(self, mock_file):
        """
        Test loading items from a file.

        TODO: Add more test cases for different file contents.
        """
        items = load_items('test_quotes.txt')
        self.assertIsInstance(items, list)
        self.assertGreater(len(items), 0)

    def test_get_random_item(self):
        """
        Test getting a random item from a list.

        TODO: Add edge cases for empty and single-item lists.
        """
        items = ['item1', 'item2', 'item3']
        random_item = get_random_item(items)
        self.assertIn(random_item, items)

    @patch('builtins.open', new_callable=_mock_open, data='Welcome to Termux!\nYour daily dose of motivation:\n')
    def test_get_header(self, mock_file):
        """
        Test getting the header from the headers file.

        TODO: Add test cases for empty and malformed headers files.
        """
        header = get_header()
        self.assertEqual(header, 'Welcome to Termux!')

    @patch('builtins.open', new_callable=_mock_open, data='"Success is not final, failure is not fatal: It is the courage to continue that counts." - Winston Churchill\n')
    def test_get_random_quote(self, mock_file):
        """
        Test getting a random quote from the quotes file.

        TODO: Add test cases for files with multiple quotes.
        """
        quote = get_random_quote()
        self.assertIn('Success is not final', quote)

    @patch('subprocess.run')
    def test_get_device_info(self, mock_run):
        """
        Test getting device information using Termux-API commands.

        TODO: Add test cases for different command outputs.
        """
        self._patch_subprocess(mock_run)
        device_info = get_device_info()
        self.assertIn('Mocked Output', device_info)

    @patch('subprocess.run')
    def test_get_battery_status(self, mock_run):
        """
        Test getting battery status using Termux-API commands.

        TODO: Add test cases for different battery statuses.
        """
        self._patch_subprocess(mock_run)
        battery_status = get_battery_status()
        self.assertIn('Mocked Output', battery_status)

    @patch('subprocess.run')
    def test_get_storage_usage(self, mock_run):
        """
        Test getting storage usage information.

        TODO: Add test cases for different storage usage outputs.
        """
        self._patch_subprocess(mock_run)
        storage_usage = get_storage_usage()
        self.assertIn('Mocked Output', storage_usage)

if __name__ == '__main__':
    unittest.main()

