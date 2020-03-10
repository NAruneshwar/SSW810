from prettytable import PrettyTable
from collections import defaultdict
import os
from HW08_Arun_Nalluri import file_reading_gen


class Student:
    """
        Need to know:
        -CWID
        -name
        -major
        -courses
    """
    
    def __init__(self, cwid, name, major):
        self._cwid = cwid
        self._name = name
        self._major = major
        self._courses = dict()
             
    def add_course(self, course, grade):
        if grade in  ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C']:
            self._courses[course] = grade
        elif grade == 'F':
            print(f"The student with CWID {self._cwid} has failed the course")
        else:
            print(f"The student with CWID {self._cwid} has no grade in record")


class Instructor:
    """Contains all the information about the Instructor"""
    def __init__(self, cwid, name, dept):
        self._cwid = cwid
        self._name = name
        self._dept = dept
        self._courses = defaultdict(int)
    
    def get_student_no(self, course):
        self._courses[course] += 1


class Major:
    """Contains all the information about the Majors being offerd"""
    def __init__(self, dept, r_e, course):
        self._dept = dept
        self._required = set()
        self._elective = set()


class Repository:
    """Contains all the data required for the program its the whole repository of the program"""
    def __init__(self, path, ptable=False):
        self._students = dict()
        self._instructors = dict()
        self._majors = dict()
        try:
            self._get_students(os.path.join(path, "students.txt"))
            self._get_instructors(os.path.join(path, "instructors.txt"))
            self._get_grades(os.path.join(path, "grades.txt"))
            self._get_majors(os.path.join(path, "majors.txt"))
        except FileNotFoundError:
            print("please check the path passed in the function")

        if ptable:
            self.major_prettytable()
            self.student_prettytable()
            self.instructor_prettytable()

    def _get_students(self, path):
        """Reads the students file and adds the data to the program"""
        try:
            for cwid, name, major in file_reading_gen(path, 3, sep=';', header=True):
                self._students[cwid] = Student(cwid, name, major)

        except FileNotFoundError as err1:
            print(f"there was an error {err1} trying to get student details at {cwid}")
        except ValueError as ve:
            print(f"there was an error {ve} trying to get student details please check the number of fields")
       
    def _get_instructors(self, path):
        """Reads the instructors file and adds the data to the program"""
        try:
            for cwid, name, dept in file_reading_gen(path, 3, sep='|', header=True):
                self._instructors[cwid] = Instructor(cwid, name, dept)

        except FileNotFoundError as err1:
            print(f"there was an error {err1} trying to get Instructor details at {cwid}")
        except ValueError as ve:
            print(f"there was an error {ve} trying to get Instructor details please check the number of fields")
            
    def _get_grades(self, path):
        """Reads the grades file and adds the data to the program"""
        try:
            for cwid, course, grade, instructor_cwid in file_reading_gen(path, 4, sep='|', header=True):
                if cwid in self._students.keys():
                    self._students[cwid].add_course(course, grade)
                else:
                    print(f"didnt find student {cwid} whose grade was mentioned")
                if instructor_cwid in self._instructors.keys():
                    self._instructors[instructor_cwid].get_student_no(course)
                else:
                    print(f"didnt find prof with cwid = {cwid} whose course was mentioned")
        except ValueError as ve:
            print(f"exception {ve} occured")

   
   
    def _get_majors(self, path):
        """Reads the Majors file and adds the data to the program"""
        try:
            for dept, r_e, course in file_reading_gen(path, 3, sep='\t', header=True):
                if dept not in self._majors.keys():         
                   self._majors[dept] = Major(dept, r_e, course)
                
                if r_e.upper() == 'R':
                    self._majors[dept]._required.add(course)
                elif r_e.upper() == 'E':
                    self._majors[dept]._elective.add(course)
        except FileNotFoundError as err1:
            print(f"there was an error {err1} trying to get Instructor details at {course}")
        except ValueError as ve:
            print(f"there was an error {ve} trying to get Instructor details")
             
   
    def major_prettytable(self):
        """Sends the Major data to the pretty table and prints it"""
        pretty_table3 = PrettyTable(field_names=['Dept', 'Required', 'Electives'])
        for maj2 in self._majors.values():
            pretty_table3.add_row([maj2._dept, sorted(maj2._required), sorted(maj2._elective)])

        print(pretty_table3)
    
    def student_prettytable(self):
        """Sends the student data to the pretty table and prints it"""
        pretty_table = PrettyTable(field_names=['CWID', 'Name', 'Major', 'Completed Courses', 'Remaining Courses', 'Remaining Electives'])
        for student in self._students.values():            
            pretty_table.add_row([student._cwid, student._name, student._major, sorted(student._courses.keys()), sorted(self._majors[student._major]._required-student._courses.keys()), (self._majors[student._major]._elective-student._courses.keys() if len(self._majors[student._major]._elective-student._courses.keys())==3 else None)])

        print(pretty_table)
 
    def instructor_prettytable(self):
        """Sends the instructors data to the pretty table and prints it"""
        pretty_table2 = PrettyTable(field_names=['CWID', 'Name', 'Dept', 'Course', 'Students'])
        for Instructor in self._instructors.values():
            for cour in Instructor._courses:
                pretty_table2.add_row([Instructor._cwid, Instructor._name, Instructor._dept, cour, Instructor._courses[cour]])

        print(pretty_table2)
     

Stevens = Repository("C:\\Users\\arunn\\Desktop\\Masters!\\810 Python", ptable=True)
