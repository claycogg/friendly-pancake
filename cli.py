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
        print(sys.argv)
        if len(sys.argv) > 4:
            print("Please follow the instructions found in the Readme and double-check your arguments.")
            exit()
        try:
            self.filePath = sys.argv[1]
            self.file = open(self.filePath, 'r')
            self.firstDate = sys.argv[2]
            self.secondDate = sys.argv[3]
        except FileNotFoundError:
            print("Please check the entered file path.\n")
            exit()


def main():
    cli = CLI()
    date_reader = DateReader()

    dates = date_reader.read_file(cli.file)
    price_analyzer = PriceAnalyzer(dates)
    input_dates = [date_reader.to_datetime(cli.firstDate), date_reader.to_datetime(cli.secondDate)]

    for date in input_dates:
        price_analyzer.get_price(date)

    price_analyzer.price_range(input_dates[0], input_dates[1])
if __name__ == '__main__':
    main()