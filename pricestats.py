import nose
import unittest
import sys
import datetime as dt


#it has to take a datetime.datetime object
global ghi

class DateReader:

    def __init__(self):
        self.dateDict = None

    def read_file(self, path):
        #check the path to make sure its not something weird
        date_file = open(path, 'r')
        temp_dict = {}

        for line in date_file:
            tokens = line.split()
            tokens[0] = self.to_datetime(tokens[0])
            temp_dict[tokens[0]] = (tokens[1], tokens[2])
        self.dateDict = temp_dict
        return temp_dict

    @classmethod
    def to_datetime(self, date):
        temp_date = date
        #this does not use ISO_8601 style as is (not for formating)
        temp_date = dt.datetime.strptime(temp_date, "%Y-%m-%dT%H:%M:%SZ")
        global ghi
        ghi = temp_date
        return temp_date

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
            response = input('Is this the correct file? Y/N\n')
            self.handle_response(response)

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


