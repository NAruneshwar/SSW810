import unittest
from HW09_Pranay_Singh import Respository, Student, Instructor
import os, sys
from prettytable import PrettyTable


class TestHW09(unittest.TestCase):
    """ Class to perform unit test   """
    def test_class_student(self):
        """ Test of computed values against actual values for student summary . Prof Rowland i have tested values from pretty table this time """
        ob = Respository("/Users/pranaysingh/dummy/Stevens/")
        erty = ob.University_Students_data_repository()
        sdfg = ob.University_Grades_repository()
        x = Student(sdfg, erty)
        foo = x.pretty_print_student_summary()
        cwid = list()
        name = list()
        completed_courses = list()
        for row in foo:
            row.border = False
            row.header = False
            cwid.append(row.get_string(fields = ["CWID"]).strip())
            name.append(row.get_string(fields = ["Name"]).strip())
            completed_courses.append(row.get_string(fields = ["Completed Courses"]).strip())
        test_cwid = ["10103","10115", "10172","10175", "10183","11399","11461", "11658", "11714", "11788"]
        test_name = ["Baldwin, C", "Wyatt, X","Forbes, I", "Erickson, D", "Chapman, O", "Cordova, I", "Wright, U", "Kelly, P", "Morton, A", "Fuller, E"]
        test_completed = ["['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']", "['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']","['SSW 555', 'SSW 567']","['SSW 564', 'SSW 567', 'SSW 687']","['SSW 689']","['SSW 540']","['SYS 611', 'SYS 750', 'SYS 800']","['SSW 540']","['SYS 611', 'SYS 645']","['SSW 540']"]
        self.assertEqual(cwid, test_cwid)
        self.assertEqual(name, test_name)
        self.assertEqual(completed_courses, test_completed)

    def test_university_directory_exists_or_is_it_empty(self):
        """ Test whether the directory exists or not and whether the directory contains the neccesaary data files """
        jfn = Respository("/Users/pranaysingh/dummy/Stns/")
        with self.assertRaises(FileNotFoundError) as context:
            jfn.University_Students_data_repository()
        self.assertEqual(str(context.exception),"Can't open the file!")
        jfn = Respository("/Users/pranaysingh/dummy/Stns/")
        with self.assertRaises(FileNotFoundError) as context:
            jfn.University_Instructors_repository()
        self.assertEqual(str(context.exception),"Can't open the file!")
        jfn = Respository("/Users/pranaysingh/dummy/Stns/")
        with self.assertRaises(FileNotFoundError) as context:
            jfn.University_Grades_repository()
        self.assertEqual(str(context.exception),"Can't open the file!")
        
    def test_if_grades_are_missing_for_any_student(self):
        """ Check whether grade of a student is missing or not """
        dff = Respository("/Users/pranaysingh/dummy/columbia/")
        with self.assertRaises(ValueError) as context:
            dff.University_Grades_repository()
        self.assertEqual(str(context.exception),"Student Grade/s is/are missing!")

    def test_class_instructor(self):
        """ Test of computed values against actual values for instructor summary .Prof Rowland i have tested values from pretty table this time """
        ob = Respository("/Users/pranaysingh/dummy/Stevens/")
        yuiop = ob.University_Instructors_repository()
        sdfg = ob.University_Grades_repository()
        fw = Instructor(sdfg, yuiop)
        bar = fw.pretty_print_instructor_summary()
        cwid = list()
        name = list()
        dept = list()
        course = list()
        students = list()
        for row in bar:
            row.border = False
            row.header = False
            cwid.append(row.get_string(fields = ["CWID"]).strip())
            name.append(row.get_string(fields = ["Name"]).strip())
            dept.append(row.get_string(fields = ["Dept"]).strip())
            course.append(row.get_string(fields = ["Course"]).strip())
            students.append(row.get_string(fields = ["Students"]).strip())
        test_cwid = ['98765', '98764', '98764', '98764', '98764', '98763', '98763', '98765', '98760', '98760', '98760', '98760']
        test_name = ['Einstein, A', 'Feynman, R', 'Feynman, R', 'Feynman, R', 'Feynman, R', 'Newton, I', 'Newton, I', 'Einstein, A', 'Darwin, C', 'Darwin, C', 'Darwin, C', 'Darwin, C']
        test_dept = ['SFEN', 'SFEN', 'SFEN', 'SFEN', 'SFEN', 'SFEN', 'SFEN', 'SFEN', 'SYEN', 'SYEN', 'SYEN', 'SYEN']
        test_course = ['SSW 567', 'SSW 564', 'SSW 687', 'CS 501', 'CS 545', 'SSW 555', 'SSW 689', 'SSW 540', 'SYS 800', 'SYS 750', 'SYS 611', 'SYS 645']
        test_students = ['4', '3', '3', '1', '1', '1', '1', '3', '1', '1', '2', '1']
        self.assertEqual(cwid, test_cwid)
        self.assertEqual(name, test_name)
        self.assertEqual(dept, test_dept)
        self.assertEqual(course, test_course)
        self.assertEqual(students, test_students)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

