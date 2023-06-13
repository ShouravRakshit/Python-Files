import unittest

import main


class TestMain(unittest.TestCase):

    def test_do_stuff(self):
        num = 10
        result = main.do_stuff(num)
        self.assertEqual(result, .5)

    def test_do_stuff2(self):
        num = "sad"
        result = main.do_stuff(num)
        self.assertTrue(result, ValueError)

    def test_do_stuff3(self):
        num = 0
        result = main.do_stuff(num)
        self.assertTrue(result, ZeroDivisionError)


if __name__ == '__main__':
    unittest.main()
