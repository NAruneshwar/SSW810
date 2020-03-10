import unittest
from HW05_Arun_Nalluri import find_second, reverse, rev_enumerate, get_lines


class TestString(unittest.TestCase):
    """Class is used to test all the functions"""

    def test_reverse(self):
        """contains the test cases for reverseing of string"""

        self.assertEqual(reverse("Hello world"), "dlrow olleH")
        self.assertEqual(reverse(" "), " ")
        self.assertEqual(reverse("good day to you!"), "!uoy ot yad doog")

    def test_rev_enumerate(self):
        """contains the test cases for rev_enumerate()"""
        testcaseresult = list([(11, '!'), (10, 'i'), (9, 'j'), (8, 'n'), (7, 'e'), (6, 'B'), (5, ' '), (4, 'o'), (3, 'l'), (2, 'l'), (1, 'e'), (0, 'H')])
        self.assertEqual(list(rev_enumerate("Hello Benji!")), testcaseresult)
        self.assertEqual(list(rev_enumerate("1996")), list([(3, '6'), (2, '9'), (1, '9'), (0, '1')]))
        self.assertEqual(list(rev_enumerate("")), list(""))

    def test_find_second(self):
        """contains the test cases for rev_enumerate()"""

        self.assertEqual(find_second('iss', 'Mississippi'), 4)
        self.assertEqual(find_second('abba', 'abbabba'), 3)
        self.assertEqual(find_second('zzz', 'abbabba'), -1)
        self.assertEqual(find_second(' ', 'abbabba'), -1)
        self.assertEqual(find_second('abc', ' '), -1)
        self.assertEqual(find_second('zzz', 'abczzzdefzzzaga'), 9)


class GetLinesTest(unittest.TestCase):

    def test_get_lines(self):
        """contains the test cases for get_lines()"""

        file_name = 'C:\\Users\\arunn\\Desktop\\Masters!\\810 Python\\test.txt'
        expect = ['<line0>', '<line1>', '<line2>', '<line3.1 line3.2 line3.3>', '<line4.1 line4.2>', '<line5>', '<line6>']
        result = list(get_lines(file_name))
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
