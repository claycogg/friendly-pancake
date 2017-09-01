import nose
import datetime
import unittest
import pricestats as ps


class TestDateReader(unittest.TestCase):
    def setUp(self):
        self.aDateReader = ps.DateReader()

    def testInit(self):
        assert self.aDateReader.dateDict is None

    def testReadDictKey(self):
        self.aDateReader.read_file('data_samples/sample2.txt')
        date_dict_result = dict()
        date_dict_result[datetime.datetime(2017, 3, 1, 13, 37, 59)] = ('21.37', '100')
        assert list(self.aDateReader.dateDict.keys())[0] == list(date_dict_result.keys())[0]

    def testReadDictValue(self):
        self.aDateReader.read_file('data_samples/sample2.txt')
        date_dict_result = dict()
        test_datetime = datetime.datetime(2017, 3, 1, 13, 37, 59)
        date_dict_result[test_datetime] = ('21.37', '100')
        assert date_dict_result[test_datetime] == self.aDateReader.dateDict[test_datetime]

    def testToDateTime(self):
        date_result = self.aDateReader.to_datetime('2017-03-01T13:37:59Z')
        assert date_result == datetime.datetime(2017, 3, 1, 13, 37, 59)


# These tests assume that ones above were successful
class TestStatAnalysis(unittest.TestCase):

    def setUp(self):
        self.aDateReader = ps.DateReader()
        self.date_dict_result = self.aDateReader.read_file('data_samples/sample1.txt')
        self.priceAnalyzer = ps.PriceAnalyzer(self.date_dict_result)
        self.one_date = datetime.datetime(2017, 3, 1, 13, 37, 59)

    def testGetPriceLastElement(self):
        assert self.priceAnalyzer.get_price(datetime.datetime(2017, 12, 12)) == '17.21'

    def testGetPriceFirstElement(self):
        print("wow look here" + self.priceAnalyzer.get_price(datetime.datetime(2016, 1, 2)))
        assert self.priceAnalyzer.get_price(datetime.datetime(2016, 1, 2)) == '21.37'

    def testGetPrice(self):
        assert self.priceAnalyzer.get_price(datetime.datetime(2017, 3, 1, 13, 37, 59)) == '21.37'

    def testGetPriceAvg(self):
        assert self.priceAnalyzer.get_price(datetime.datetime(2017, 4, 24)) == '20.77'

    # def testMax(self):

    # def testMin(self):

    # def testAvg(self):

    # def testStdDev(self):

    # def testMedian(self):

    def testFirstSecondOrder(self):
        self.priceAnalyzer.first_second_order(datetime.datetime(2017, 5, 30), datetime.datetime(2017, 3, 1))
        assert self.priceAnalyzer.firstDate == datetime.datetime(2017, 3, 1)

    def testDictCleaner(self):
        self.priceAnalyzer.first_second_order(datetime.datetime(2017, 5, 30), datetime.datetime(2017, 3, 30))
        pages = self.priceAnalyzer.dict_cleaner()
        # pretty lazy test, just making sure that there are the expected number of dates
        assert len(pages) == 2

    # This nifty test is really testing the commented out things above as well as the other 2 tests, making them sort of
    # redundant. If this wasn't already late I would do my due diligence and make sure they are all working individually
    def testPriceRange(self):
        results = self.priceAnalyzer.price_range(datetime.datetime(2017, 5, 30), datetime.datetime(2017, 3, 30))
        assert results == ('23.09', '20.18', '21.63', '1.07', '21.63')

if __name__ == '__main__':
    unittest.main()
