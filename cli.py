from pricestats import DateReader
from pricestats import PriceAnalyzer
import sys


class CLI:

    def __init__(self):
        self.filePath = None
        self.file = None
        self.firstDate = None
        self.secondDate = None
        self.handle_args()

    def handle_args(self):
        if len(sys.argv) > 4:
            print("You have entered too many arguments. Please look to the Readme for the proper usage of arguments.")
            exit()
        elif len(sys.argv) < 2:
            print("You have entered too few arguments. Please look to the Readme for the proper usage of arguments.")
        self.filePath = sys.argv[1]
        self.open_file()
        self.firstDate = sys.argv[2]
        self.secondDate = sys.argv[3]

    def open_file(self):
        try:
            self.file = open(self.filePath, 'r')
        except FileNotFoundError:
            print('\n' + "You tried to access: '%s' + but something went wrong." % self.filePath)
            self.filePath = input("Please check that the path is correct and type it again, or press enter to end...\n")
            if self.filePath == "":
                exit()
            self.open_file()


def main():
    cli = CLI()
    date_reader = DateReader()

    print(str(cli.file))
    dates = date_reader.read_file(cli.file)
    price_analyzer = PriceAnalyzer(dates)
    input_dates = [date_reader.to_datetime(cli.firstDate), date_reader.to_datetime(cli.secondDate)]

    for date in input_dates:
        price_analyzer.get_price(date)

    price_analyzer.price_range(input_dates[0], input_dates[1])
if __name__ == '__main__':
    main()
