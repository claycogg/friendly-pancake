import nose
import unittest
import sys

class DateReader(object):
    def __init__(self, path):
        self.filePath = path
        print("~Welcome to my DateReader~")


class CLI():
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


aCli = CLI()
aCli.request_path()
aDateReader = DateReader(aCli.filePath)
