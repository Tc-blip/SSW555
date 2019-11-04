import unittest
from US34 import listLargeAgeDifferences

class Families(object):

    def __init__(self,id, Married, Husband_ID, Wife_ID):
        self.ID = id
        self.Married = Married
        self.Husband_ID = Husband_ID
        self.Wife_ID = Wife_ID

class Individuals:
    def __init__(self,id, Birthday):
        self.ID = id
        self.Birthday = Birthday

class TestUS34(unittest.TestCase):

    def test_listLargeAgeDifferences(self):
        fm1 = Families("F1", "01 JAN 2000", "I1", "I2")
        fm2 = Families("F2", "01 JAN 2005", "I3", "I4")
        fm3 = Families("F3", "01 JAN 2007", "I5", "I6")
        fm = {"F1": fm1, "F2": fm2, "F3": fm3}
        indi1 = Individuals("I1", "01 JAN 1980")
        indi2 = Individuals("I2", "01 JAN 1960")
        indi3 = Individuals("I3", "01 JAN 1980")
        indi4 = Individuals("I4", "01 JAN 1960")
        indi5 = Individuals("I5", "01 JAN 1980")
        indi6 = Individuals("I6", "01 JAN 1980")
        indi = {"I1": indi1, "I2": indi2, "I3": indi3, "I4": indi4, "I5": indi5, "I6": indi6}
        self.assertEqual(listLargeAgeDifferences(fm, indi), [["I1", "I2"]])

if __name__ == '__main__':
    unittest.main()