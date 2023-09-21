import unittest
from stockprice import get_max_profit

class TestStockPrice(unittest.TestCase):
    def test_valid_input(self):
        prices = [10, 7, 5, 8, 11, 9]
        self.assertEqual(get_max_profit(prices), 6)

    def test_invalid_input(self):
        prices = [10, 9, 8, 7, 6, 5]
        with self.assertRaises(ValueError):
            get_max_profit(prices)

    def test_edge_case(self):
        prices = [10, 10, 10, 10, 10, 10]
        self.assertEqual(get_max_profit(prices), 0)

    def test_performance(self):
        prices = [i for i in range(100000)]
        self.assertEqual(get_max_profit(prices), 99999)

    def test_integration(self):
        prices = [10, 7, 5, 8, 11, 9]
        max_profit = get_max_profit(prices)
        self.assertTrue(max_profit >= 0)