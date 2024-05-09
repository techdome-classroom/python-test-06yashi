import unittest
from program2 import decode_message

class TestDecoder(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(decode_message("aa", "a"), False)

    def test_case2(self):
        self.assertEqual(decode_message("aa", "*"), True)

    def test_case3(self):
        self.assertEqual(decode_message("cb", "?a"), False)

    def test_case4(self):
        self.assertEqual(decode_message("abc", "?b?"), True)

if __name__ == '__main__':
    unittest.main()

