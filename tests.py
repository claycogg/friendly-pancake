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

class TestStatAnalysis(unittest.TestCase):

if __name__ == '__main__':
    unittest.main()
