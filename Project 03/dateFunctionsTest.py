import unittest
from datetime import timedelta
import datetime
from dateFunctions import compareDates, dateBeforeCurrentDate, differenceBetweenDates, lessThan150YearsOld

class TestSprint1Methods(unittest.TestCase):

    def test_compareDates(self):
        """date1 is earliest date, date2 is later date, date3 is equal to first date"""
        date1 = datetime.datetime(2015, 1, 1, 0, 0, 0)
        date2 = datetime.datetime(2016, 1, 1, 0, 0, 0)
        date3 = datetime.datetime(2015, 1, 1, 0, 0, 0)
        self.assertEqual(compareDates(date1, date2), -1)
        self.assertEqual(compareDates(date2, date3), 1)
        self.assertEqual(compareDates(date3, date1), 0)


    def test_dateBeforeCurrentDate(self):
        """date1 is a date in the past"""
        date1 = datetime.datetime(2015, 1, 1, 0, 0, 0)
        date2 = datetime.datetime.now()

        self.assertEqual(dateBeforeCurrentDate(date1), True)
        self.assertEqual(dateBeforeCurrentDate(date2 + timedelta(21)), False)
        self.assertEqual(dateBeforeCurrentDate(date2), True)

    def test_differenceBetweenDates(self):
        """date1 is 10 years before the current date, date2 is 5 years before the current date, date3 is 1 year before the current date"""
        date1 = datetime.datetime.now() - timedelta(3650)
        date2 = date1 + timedelta(1825)
        date3 = date1 + timedelta(3285)

        self.assertEqual(differenceBetweenDates(date1, date2), 5)
        self.assertEqual(differenceBetweenDates(date1, date3), 9)
        self.assertEqual(differenceBetweenDates(date2, date3), 4)

    def test_lessThan150YearsOld(self):
        """date1 is 200 years ago, date2 is 150 years ago, date3 is 10 years ago"""
        date1 = datetime.datetime.now() - timedelta(73000)
        date2 = date1 + timedelta(18250)
        date3 = date1 + timedelta(69350)

        self.assertEqual(lessThan150YearsOld(date1), False)
        self.assertEqual(lessThan150YearsOld(date2), False)
        self.assertEqual(lessThan150YearsOld(date3), True)

if __name__ == '__main__':
    unittest.main()