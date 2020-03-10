import os
import datetime
from prettytable import PrettyTable


def date_arithmetic():
    """ This function performs date Operations""" 

    date1 = "Feb 27, 2000" 
    dt1 = datetime.datetime.strptime(date1,"%b %d, %Y") #changing the date format into python date
    dt2 = dt1 + datetime.timedelta(days=3)

    date2 = "Feb 27, 2017"
    dm1 = datetime.datetime.strptime(date2,"%b %d, %Y")
    dm2 = dm1 + datetime.timedelta(days=3)
    
    date3 = "Jan 1, 2017"
    date4 = "Oct 31, 2017"
    dm3 = datetime.datetime.strptime(date3, "%b %d, %Y")
    dm4 = datetime.datetime.strptime(date4, "%b %d, %Y")
    delta = dm4 - dm3

    #Returning the tuple
    return dt2, dm2, delta.days


def file_reading_gen(path, fields, sep=',', header=False):
    """ Generator to read columns in the given file """
    try:
        fp = open(path,"r")
    except FileNotFoundError:
        raise FileNotFoundError
    else:
        with fp:
            if header is True:
                next(fp)    
            for offset, line in enumerate(fp):
                current = line.strip().split(sep)
                if len(current) != fields:
                    raise ValueError(f" {fp} has {len(current)} on line {offset+1} and {fields} ")
                else:
                    yield tuple(line.strip().split(sep))


class FileAnalyzer:
    """ Class to implement analyze_filers, pretty_print functions """

    def __init__(self, directory):
        """ Function to initalizes variable directory """
        self.directory = directory
        self.files_summary = self.analyze_files()

    def analyze_files(self):
        """ Function to count number of lines, characters, functions and classes in a file """
        self.list_d = dict()
        try:
            list_files = os.listdir(self.directory)
        except FileExistsError:
            raise FileExistsError("not found")
        else:
            for file in list_files:
                if file.endswith(".py"):
                    try:
                        fp = open(os.path.join(self.directory, file), "r")
                    except FileNotFoundError:
                        raise FileNotFoundError("Cant find file pls")
                    else:
                        with fp: 
                            num_lines, num_char, num_func, num_class = 0,0,0,0
                            file_name = file 
                            for line in fp:                 
                                line = line.strip()
                                num_lines += 1
                                num_char = num_char + len(line)
                                if line.startswith("def ") and line.endswith(":"): 
                                    num_func += 1
                                elif line.startswith("class ") and line.endswith(":"):
                                    num_class += 1
                        self.list_d[file_name] = {"class": num_class, "function": num_func, "line": num_lines, "char": num_char}
        return self.list_d
            
    def pretty_print(self):
        """ To print the file summary in a pretty table"""
        pretty_table = PrettyTable(field_names = ["File Name", "Classes", "Functions", "Lines", "Characters"])

        for file_name in self.list_d:
            pretty_table.add_row([file_name, self.list_d[file_name]["class"], self.list_d[file_name]["function"], self.list_d[file_name]["line"], self.list_d[file_name]["char"]])

        return pretty_table
