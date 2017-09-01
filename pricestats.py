import nose
import unittest
import sys


class DateReader:

    def __init__(self):
        self.filePath = None
        self.dateDict = None

    def read_file(self, path):
        #check the path to make sure its not something weird
        date_file = open(path, 'r')
        temp_dict = {}

        for line in date_file:
            tokens = line.split()
            temp_dict[tokens[0]] = (tokens[1], tokens[2])
        self.dateDict = temp_dict
        return temp_dict



class CLI:

    def __init__(self):
        self.filePath = None
        self.again = None
        self.response = None
        print("--Welcome to my PricingStatistics Implementation--\n")

    def handle_response(self, response):
        response = str(response)
        if response.upper() == 'Y':
            return self.filePath

        elif response.upper() == 'N':
            self.request_path()

        else:
            print("Pleas enter Y or N\n")
            self.request_path()

    def request_path(self):
        file_path = input("Please provide a file path ...\n")
        self.filePath = file_path

        print("You have selected: " + file_path + '\n')

        response = input('Is this the correct file? Y/N\n')

        return self.handle_response(response)


#init our classes
aCli = CLI()
aDateReader = DateReader()

#do a little work
aCli.request_path()
aDateReader.read_file(aCli.filePath)

