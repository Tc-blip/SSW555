import unittest
from datetime import timedelta
import datetime
from dateFunctions import compareDates, dateBeforeCurrentDate, differenceBetweenDates, lessThan150YearsOld

class Families(object):

    def __init__(self,id, Married, Divorced, Husband_ID, Wife_ID, Husband_Name, Wife_Name):
        self.ID = id
        self.Married = Married
        self.Divorced = Divorced
        self.Husband_ID = Husband_ID
        self.Wife_ID = Wife_ID
        self.Husband_Name = Husband_Name
        self.Wife_Name = Wife_Name

class Person_info:

    def __init__(self,id, birt, deat):
        self.ID = id
        self.Birthday = birt
        self.Death = deat

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
        fm1 = Families("F1", "01 JAN 2000", "01 JAN 2008", "I1", "I2", "Abraham", "Betty")
        fm2 = Families("F2", "01 JAN 2005", "01 JAN 2011", "I1", "I3", "Charlie", "Denise")
        fm3 = Families("F3", "01 JAN 2012", "NA", "I4", "I3", "Eddie", "Francesca")
        fm = {"1": fm1, "2": fm2, "3": fm3}

        p1 = Person_info("I1", "01 JAN 1980", "NA")
        p2 = Person_info("I2", "01 JAN 1990", "NA")
        p3 = Person_info("I3", "01 JAN 1979", "NA")
        p4 = Person_info("I4", "01 JAN 1978", "NA")
        ppl = {"I1": p1, "I2": p2, "I3": p3, "I4": p4}

        self.assertEqual(dateBeforeCurrentDate(fm, ppl), False)

    def test_differenceBetweenDates(self):
        """date1 is 10 years before the current date, date2 is 5 years before the current date, date3 is 1 year before the current date"""
        date1 = datetime.datetime.now() - timedelta(3650)
        date2 = date1 + timedelta(1825)
        date3 = date1 + timedelta(3285)

        self.assertEqual(differenceBetweenDates(date1, date2), 5)
        self.assertEqual(differenceBetweenDates(date1, date3), 9)
        self.assertEqual(differenceBetweenDates(date2, date3), 4)

    def test_lessThan150YearsOld(self):
        p1 = Person_info("I1", "01 JAN 1980", "NA")
        p2 = Person_info("I2", "01 JAN 1990", "NA")
        p3 = Person_info("I3", "01 JAN 1979", "NA")
        p4 = Person_info("I4", "01 JAN 1978", "NA")
        ppl = {"I1": p1, "I2": p2, "I3": p3, "I4": p4}

        self.assertEqual(lessThan150YearsOld(ppl), True)

if __name__ == '__main__':
    unittest.main()