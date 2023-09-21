#Create test script covering all scenarios (min 5 test cases)

import unittest
from test import sortString

class TestSortString(unittest.TestCase):
    def test_sortString(self):
        self.assertEqual(sortString("hello world"), "lllooehwrd")
        self.assertEqual(sortString("hello"), "llheo")
        self.assertEqual(sortString("helloworld"), "lllooehwrd")
        self.assertEqual(sortString("helloworld"), "lllooehwrd")
        self.assertEqual(sortString("helloworld"), "lllooehwrd")

if __name__ == '__main__':
    unittest.main()
