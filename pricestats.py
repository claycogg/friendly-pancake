import datetime as dt

# for quick dirty testing
global ghi


class PriceAnalyzer:

    @classmethod
    def __init__(self, date_prices):
        self.datePrices = date_prices
        self.firstDate = None
        self.secondDate = None

    def get_price(self, date):
        search_dict = dict(self.datePrices)
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

    @classmethod
    def price_range(cls, first_date, second_date):
        if first_date > second_date:
            cls.firstDate = second_date
            cls.secondDate = first_date
        else:
            cls.firstDate = first_date
            cls.secondDate = second_date

        dates = dict(cls.datePrices)
        for date in list(dates.keys()):
            if date < cls.firstDate:
                del dates[date]
            if date > cls.secondDate:
                del dates[date]

        max = cls.price_max(dates)
        min = cls.price_min(dates)
        avg = cls.price_avg(dates)
        std_dev = cls.price_std_dev(dates, avg)
        median = cls.price_median(dates)

    @classmethod
    def price_max(cls, dates):
        max_date = None
        max_price = str(float("-inf"))
        for date in list(dates.keys()):
            price_units = dates[date]
            if max_price < price_units[0]:
                max_date = date
                max_price = price_units[0]
        print("MAX : " + max_price)
        return max_price

    @classmethod
    def price_min(cls, dates):
        min_date = None
        min_price = str(float("inf"))
        for date in list(dates.keys()):
            price_units = dates[date]
            if price_units[0] < min_price:
                min_date = date
                min_price = price_units[0]
        print("MIN : " + min_price)
        return min_price

    @classmethod
    def price_avg(cls, dates):
        counter = 0
        total = 0
        avg_price = 0
        for date in dates:
            price_units = dates[date]
            total += float(price_units[0])
            counter += 1

        if counter is not 0:
            avg_price = total/counter
        print("AVG : %.2f" % avg_price)
        return avg_price

    @classmethod
    def price_std_dev(cls, dates, avg):

        counter = 0
        for date in dates:
            price_units = dates[date]
            std_sum = ((float(price_units[0])) - avg)**2
            counter += 1
        std_dev = std_sum / counter
        print("STD_DEV : %.2f" % std_dev)

        return std_dev
    @classmethod
    def price_median(cls, dates):
        median_price = None
        # It takes the average of prices from around it for an even amount of dates
        indexer = list(dates.keys())
        half_length = len(indexer)/2
        if type(half_length) is not int:
            half_length = int(half_length)
            median_price = (float(dates[indexer[half_length]][0]) + float(dates[indexer[half_length + 1]][0]))/2
        else:
            median_date = indexer[half_length]
            median_price = dates[median_date][0]

        print("MEDIAN : %.2f" % median_price)


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

def dev_tests():

    aDateReader.read_file(aCli.filePath)

    aPriceAnalyzer = PriceAnalyzer(aDateReader.dateDict)

    aPriceAnalyzer.get_price(dt.datetime(2016, 1, 2))
    aPriceAnalyzer.get_price(ghi)
    aPriceAnalyzer.get_price(dt.datetime(2017, 4, 27))
    aPriceAnalyzer.get_price(dt.datetime(2017, 12, 12))
    aPriceAnalyzer.price_range(dt.datetime(2017, 1, 1), dt.datetime(2017, 5, 20))