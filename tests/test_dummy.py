import unittest

from eternal.main import calculate, main

"""
Run with PYTHONPATH=. python tests/test_dummy.py
"""


class TestDummy(unittest.TestCase):

    def test_fun(self):
        weekday = calculate(2001, 1, 3)
        self.assertEqual(weekday, 2005)

        retcode = main(("--year", "2001", "--month", "1", "--day", "3"))
        self.assertEqual(retcode, 0)

    def test_correct_day(self):
        weekday = calculate(2017, 5, 9)
        self.assertEqual(weekday, 1)

        retcode = main(("--year", "2017", "--month", "5", "--day", "9"))
        self.assertEqual(retcode, 1)

    def test_string_instead_int(self):
        calculate('2017', '5', '9')
        self.assertRaises(TypeError)

    def test_too_big_number_of_day(self):
        calculate(2017, 5, 35)
        self.assertRaises(BaseException)

        main(("--year", "2017", "--month", "5", "--day", "35"))
        self.assertRaises(BaseException)




if __name__ == '__main__':
    unittest.main()
