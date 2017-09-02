from pricestats import DateReader
from pricestats import PriceAnalyzer

class CLI:

    def __init__(self):
        self.filePath = None
        self.again = None
        self.response = None
        self.file = None
        self.options = None
        self.dates = None
        print("\n--Welcome to my PricingStatistics Implementation--\n")
        self.request_path()

    def display_options(self):

        print("Select which calculation(s) you would like performed for your date(s). You can input as many of the "
              + "options as you'd like, separated by a ','.\n")

        return input("    1 : Price at Each Date\n"
                     + "    2 : All Time-Range Calculations\n"
                     + "    3 : Min\n"
                     + "    4 : Max\n"
                     + "    5 : Average\n"
                     + "    6 : Standard Deviation\n"
                     + "    7 : Median\n\n").split(',')


    def select_options(self, dates):
        self.options = []

        print("\nDisplaying dates, price and units as found in " + self.filePath + '\n')
        for date in dates:
            print(str(date) + " : " + dates[date][0] + ', ' + dates[date][1] + '\n')
        test_dates = input("\nPlease enter a datetime or pair of datetimes. This can be done in a couple of formats: \n"
                           + "yyyy-mm-dd-hh-mm-ss\n" + "yyyy-mm-ddThh:mm:ssZ\n\n")

        self.options = self.display_options()

    def handle_response(self, response):
        loaded = False
        while not loaded:
            if response.upper() == 'Y':

                try:
                    self.file = open(self.filePath, 'r')
                    loaded = True
                except ValueError:
                    print("Please check the entered file path.")
                    self.request_path()

            elif response.upper() == 'N':
                self.request_path()

            else:
                print("Pleas enter Y or N\n")
                response = input('Is this the correct file? Y/N\n')
                self.handle_response(response)

    def request_path(self):
        file_path = input("Please provide a file path ...\n\n")
        self.filePath = file_path

        print("\nYou have selected: " + file_path + '\n')

        response = input('Is this the correct file? Y/N\n')

        return self.handle_response(response)


def main():
    cli = CLI()
    date_reader = DateReader()

    dates = date_reader.read_file(cli.file)
    price_analyzer = PriceAnalyzer(dates)

    cli.select_options(dates)

    for option in cli.options:

        if option == '1':
            for date in cli.dates:
                price_analyzer.get_price(date)

        if option == '2':
            price_analyzer.dict_cleaner(cli.dates[0], cli.dates[1])

        if option == '3':

        if option == '4':

        if option == '5':

        if option == '6':

        if option == '7':

if __name__ == '__main__':
    main()