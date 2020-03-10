import unittest
from HW09_Arun_Nalluri import Student, Instructor, Repository, Major


class StudentTest(unittest.TestCase):
    def test_student(self):
        """ Test Student summary table """
        student = Student("11111", "Arun Eshwar", "Software Engineering")
        self.assertEqual(student._major, "Software Engineering")
        self.assertEqual(student._cwid, "11111")
        self.assertEqual(student._name, "Arun Eshwar")
        
       
class InstructorTest(unittest.TestCase):
    def test_instructor(self):
        instructor = Instructor("11234", "James Rowland", "Software Engineering")
        self.assertEqual(instructor._name, "James Rowland")
        self.assertEqual(instructor._dept, "Software Engineering")
        self.assertEqual(instructor._courses, {})

class RepositoryTest(unittest.TestCase):
    """# Class test for Repository 
    """
    def test_repository(self):
        repository = Repository("C:\\Users\\arunn\\Desktop\\Masters!\\810 Python")
        expected = ['SFEN', ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545']],['SYEN', ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810']]
        output = []
        for student in repository._majors.values():            
            output.append(student.values)

        #self.assertEqual(expected, output)



if __name__ == "__main__":
    unittest.main(exit = False, verbosity = 2)  