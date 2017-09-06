import datetime as dt


class PriceAnalyzer:

    @classmethod
    def __init__(self, date_prices):
        self.datePrices = date_prices
        self.firstDate = None
        self.secondDate = None
        self.dateRange = None
        print("")

    def get_price(self, date):
        dates = dict(self.datePrices)
        indexer = list(dates.keys())
        end = len(dates) - 1
        binary_search = self.__binary_search(indexer, 0, end, date)

        # Handles the cases where there is no data for the date. By default it takes the average
        if type(binary_search) == tuple:

            # For when the date should be the first element
            if binary_search[1] == -1:
                return dates[indexer[binary_search[0]]][0]

            # For when the date should the last element
            elif binary_search[1] == end:
                return dates[indexer[binary_search[1]]][0]

            # For when the date is somewhere in the middle.
            else:
                left_price = dates[indexer[binary_search[0]]][0]
                right_price = dates[indexer[binary_search[1]]][0]
                return "%.2f" % ((float(left_price) + float(right_price))/2)
        else:
            return dates[binary_search][0]

    def __binary_search(self, dates, start, end, date):

        if end >= start:

            mid = int(start + (end - start)/2)

            if dates[mid] == date:
                return dates[mid]

            elif dates[mid] > date:
                return self.__binary_search(dates, start, mid-1, date)

            else:
                return self.__binary_search(dates, mid+1, end, date)

        else:
            return start, end

    @classmethod
    def first_second_order(cls, first_date, second_date):
        if first_date > second_date:
            cls.firstDate = second_date
            cls.secondDate = first_date
        else:
            cls.firstDate = first_date
            cls.secondDate = second_date
        return

    @classmethod
    def dict_cleaner(cls):
        dates = dict(cls.datePrices)
        for date in list(dates.keys()):
            if date < cls.firstDate:
                del dates[date]
            if date > cls.secondDate:
                del dates[date]
        cls.dateRange = dates
        return dates

    @classmethod
    def price_range(cls, first_date, second_date):
        cls.first_second_order(first_date, second_date)
        dates = cls.dict_cleaner()

        if len(dates) == 0:
            return "Your date range has nothing in it."

        max_price, min_price, avg = cls.max_min_average(dates)
        std_dev = cls.price_std_dev(dates, avg)
        median = cls.price_median(dates)

        print("Max Price: " + max_price)
        print("Min Price: " + min_price)
        print("Average Price: " + avg)
        print("Standard Deviation: " + std_dev)
        print("Median Price: " + median)
        print("")

        return max_price, min_price, avg, std_dev, median

    @classmethod
    def max_min_average(cls, dates):
        max_price = str(float("-inf"))
        min_price = str(float("inf"))
        avg_counter = 0
        avg_total = 0

        for date in list(dates.keys()):
            price_units = dates[date]
            # max
            if max_price < price_units[0]:
                max_price = price_units[0]
            # min
            if price_units[0] < min_price:
                min_price = price_units[0]

            avg_total += float(price_units[0])
            avg_counter += 1

        avg_price = avg_total / avg_counter
        avg = "%.2f" % avg_price

        return max_price, min_price, avg

    @classmethod
    def price_std_dev(cls, dates, avg):
        counter = 0
        for date in dates:
            price_units = dates[date]
            std_sum = ((float(price_units[0])) - float(avg))**2
            counter += 1
        std_dev = std_sum / counter

        return "%.2f" % std_dev

    @classmethod
    def price_median(cls, dates):
        indexer = list(dates.keys())
        half_length = len(indexer)/2
        if type(half_length) is not int and half_length > 1:
            half_length = int(half_length)
            median_price = (float(dates[indexer[half_length]][0]) + float(dates[indexer[half_length + 1]][0]))/2
        elif half_length == 1:
            median_price = (float(dates[indexer[0]][0]) + float(dates[indexer[1]][0]))/2
        else:
            half_length = int(half_length)
            median_date = indexer[half_length]
            median_price = float(dates[median_date][0])

        return "%.2f" % median_price


class DateReader:
    def read_file(self, date_file):
        dates = {}
        for line in date_file:
            tokens = line.split()
            tokens[0] = self.to_datetime(tokens[0])
            dates[tokens[0]] = (tokens[1], tokens[2])
        date_file.close()
        return dates

    @staticmethod
    def to_datetime(date):
        return dt.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")