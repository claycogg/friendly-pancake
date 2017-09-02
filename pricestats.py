import datetime as dt


class PriceAnalyzer:

    @classmethod
    def __init__(self, date_prices):
        self.datePrices = date_prices
        self.firstDate = None
        self.secondDate = None

    def get_price(self, date):
        dates = dict(self.datePrices)
        indexer = list(dates.keys())

        if date in indexer:
            price_units = dates[date]
            print('\n' + "Price: " + price_units[0])
            return price_units[0]

        else:
            dates[date] = '0'
            indexer = list(dates.keys())
            indexer.sort()

            for i in range(0, len(indexer)):
                if indexer[i] == date:
                    if i == 0:
                        next_price = dates[indexer[i+1]]
                        print("Price from the next item: " + next_price[0])
                        return next_price[0]

                    elif i == len(indexer) - 1:
                        last_price = dates[indexer[i-1]]
                        print("Price from the last item: " + last_price[0])
                        return last_price[0]

                    else:
                        last_price = dates[indexer[i-1]]
                        next_price = dates[indexer[i+1]]
                        avg_price = (float(last_price[0]) + float(next_price[0])) / 2
                        print("Price from the adjacent items: %.2f" % avg_price)
                        return "%.2f" % avg_price

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
        return dates

    @classmethod
    def price_range(cls, first_date, second_date):
        cls.first_second_order(first_date, second_date)
        dates = cls.dict_cleaner()
        if len(dates) == 0:
            return "Your date range has nothing in it."

        p_max = cls.price_max(dates)
        p_min = cls.price_min(dates)
        avg = cls.price_avg(dates)
        std_dev = cls.price_std_dev(dates, avg)
        median = cls.price_median(dates)

        return p_max, p_min, avg, std_dev, median

    @classmethod
    def price_max(cls, dates):
        max_price = str(float("-inf"))
        for date in list(dates.keys()):
            price_units = dates[date]
            if max_price < price_units[0]:
                max_price = price_units[0]
        print("MAX : " + max_price)
        return max_price

    @classmethod
    def price_min(cls, dates):
        min_price = str(float("inf"))
        for date in list(dates.keys()):
            price_units = dates[date]
            if price_units[0] < min_price:
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
        return "%.2f" % avg_price

    @classmethod
    def price_std_dev(cls, dates, avg):
        counter = 0
        for date in dates:
            price_units = dates[date]
            std_sum = ((float(price_units[0])) - float(avg))**2
            counter += 1
        std_dev = std_sum / counter
        print("STD_DEV : %.2f" % std_dev)

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

        print("MEDIAN : %.2f" % median_price)
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