import nose
import unittest
import sys
import datetime as dt

# for quick dirty testing
global ghi


class PriceAnalyzer:

    def __init__(self, date_prices):
        self.datePrices = date_prices

    def get_price(self, date):
        search_dict = self.datePrices
        indexer = list(search_dict.keys())

        if date in indexer:
            price_units = search_dict[date]
            print("Price: " + price_units[0])
            return price_units[0]

        else:
            # quick and dirty solution to finding neighbors is to create an empty key in the dict
            search_dict[date] = '0'
            indexer = list(search_dict.keys())
            indexer.sort()

            for i in range(0, len(indexer)):
                curr_date = search_dict[indexer[i]]
                if indexer[i] == date:
                    if i == 0:
                        next_price = search_dict[indexer[i+1]]
                        print("Price from the next item: " + next_price[0])
                        return next_price[0]

                    elif i == len(indexer) - 1:
                        last_price = search_dict[indexer[i-1]]
                        print("Price from the last item: " + last_price[0])
                        return last_price[0]

                    else:
                        last_price = search_dict[indexer[i-1]]
                        next_price = search_dict[indexer[i+1]]

                        avg_price = (float(last_price[0]) + float(next_price[0]) / 2)
                        print("Price from the adjacent items: %.2f" % avg_price)
                        return avg_price


class DateReader:

    def __init__(self):
        self.dateDict = None

    def read_file(self, path):
        # check the path to make sure its not something weird
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
        # this does not use ISO_8601 style as is (not for formating)
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

aPriceAnalyzer = PriceAnalyzer(aDateReader.dateDict)

aPriceAnalyzer.get_price(dt.datetime(2016, 1, 2))
aPriceAnalyzer.get_price(ghi)
aPriceAnalyzer.get_price(dt.datetime(2017, 4, 27))
aPriceAnalyzer.get_price(dt.datetime(2017, 12, 12))

