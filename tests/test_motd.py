import unittest
from src.utils import load_items, get_random_item

class TestMOTD(unittest.TestCase):

    def test_load_items(self):
        items = load_items('test_quotes.txt')
        self.assertIsInstance(items, list)
        self.assertGreater(len(items), 0)

    def test_get_random_item(self):
        items = ['item1', 'item2', 'item3']
        random_item = get_random_item(items)
        self.assertIn(random_item, items)

if __name__ == '__main__':
    unittest.main()

