import unittest
import datetime
from HW08_Arun_Nalluri import date_arithmetic, file_reading_gen, FileAnalyzer


class TestModuleGeneratorFile(unittest.TestCase):
    """ To check for ModuleGeneratorFile """

    def test_date_arithmetic(self):
        """ test cases for date arithmetic """
        self.assertTupleEqual(date_arithmetic(), (datetime.datetime(2000, 3, 1, 0, 0), datetime.datetime(2017, 3, 2, 0, 0), 303))
        self.assertNotEqual(date_arithmetic(), (datetime.datetime(2000, 4, 1, 0, 0), datetime.datetime(2017, 3, 2, 0, 0), 303))
        self.assertNotEqual(date_arithmetic(), '')
 
    def test_file_reading_gen(self):
        """ check for file reading with header and seperated by | """
        self.assertEqual([a for a in file_reading_gen("C:\\Users\\arunn\\Desktop\\Masters!\\810 Python\\arun.txt", 3, "|", True)], [("CWID", "Name", "Major"), ("123", "Jin He", "Computer Science"), ("234", "Nanda Koka", "Software Engineering"), ("345", "Benji Cai", "Software Engineering")])
        self.assertEqual([a for a in file_reading_gen("C:\\Users\\arunn\\Desktop\\Masters!\\810 Python\\arun.txt", 3, "|", False)], [("123", "Jin He", "Computer Science"), ("234", "Nanda Koka", "Software Engineering"), ("345", "Benji Cai", "Software Engineering")])

    def test_file_analyzer(self):
        """Test cases for file analyser"""
        file_analyzer = FileAnalyzer("D:\\New")
        self.assertEqual({'HW01ArunNalluri.py': {'class': 1, 'function': 1, 'line': 33, 'char': 1014}, 'HW02ArunNalluri.py': {'class': 1, 'function': 9, 'line': 156, 'char': 5091}}, file_analyzer.files_summary)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)  
