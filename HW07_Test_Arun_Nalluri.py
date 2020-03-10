import unittest
from HW07_Arun_Nalluri import anagram_lst,anagrams_cntr,anagrams_dd,covers_alphabet,book_index


class TestContainer(unittest.TestCase):
    """Contains the test cases for HW07 functions"""

    def test_anagram_lst(self):
        """Contains the test cases for anagram_lst function"""
        self.assertTrue(anagram_lst("Elbow", "Below"))
        self.assertTrue(anagram_lst("", ""))
        self.assertTrue(anagram_lst("Dormitory ", "Dirty room"))
        self.assertFalse(anagram_lst("Elbow", "Bssow"))

    def test_anagrams_cntr(self):
        """Contains the test cases for anagram_cntr function"""
        self.assertTrue(anagrams_cntr("Elbow", "Below"))
        self.assertTrue(anagrams_cntr("", ""))
        self.assertTrue(anagrams_cntr("Dormitory ", "Dirty room"))
        self.assertFalse(anagrams_cntr("Elbow", "Bssow"))

    def test_anagrams_dd(self):
        """Contains the test cases for anagram_dd function"""
        self.assertTrue(anagrams_dd("Elbow", "Below"))
        self.assertTrue(anagrams_dd("", ""))
        self.assertTrue(anagrams_dd("Dormitory ", "Dirty room"))
        self.assertFalse(anagrams_dd("Elbow", "Bssow"))

    def test_covers_alphabet(self):
        """Contains the test cases for covers_alphabet function"""
        self.assertTrue(covers_alphabet("AbCdefghiJklomnopqrStuvwxyz"))
        self.assertTrue(covers_alphabet("We promptly judged antique ivory buckles for the next prize"))
        self.assertFalse(covers_alphabet("xyz"))
        self.assertFalse(covers_alphabet(""))
        self.assertFalse(covers_alphabet("AbCdefghiJklomnopqrStu!@#$z"))
        self.assertFalse(covers_alphabet("AbCdefghi1234mnopqrStu!@#$z"))
        self.assertTrue(covers_alphabet("The quick, brown, fox; jumps over the lazy dog!"))

    def test_book_index(self):
        """Contains the test cases for book_index function"""
        woodchucks = [('how', 3), ('much', 3), ('wood', 3), ('would', 2), ('a', 1), ('woodchuck', 1), ('chuck', 3), ('if', 1), ('a', 1), ('woodchuck', 2), ('could', 2), ('chuck', 1), ('wood', 1)]
        expectedresult = [['a', [1]], ['chuck', [1, 3]], ['could', [2]], ['how', [3]], ['if', [1]], ['much', [3]], ['wood', [1, 3]], ['woodchuck', [1, 2]], ['would', [2]]]
        self.assertEqual(book_index(woodchucks), expectedresult)
        self.assertNotEqual(book_index([('much', 3), ('would', 2), ('a', 1), ('woodchuck', 1), ('chuck', 3), ('if', 1), ('a', 1), ('woodchuck', 2), ('could', 2), ('chuck', 1), ('wood', 1)]), [ ('much', 3),('how', 3), ('would', 2),  ('woodchuck', 1), ('chuck', 3),  ('a', 1), ('woodchuck', 2), ('could', 2), ('chuck', 1), ('wood', 1)])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
