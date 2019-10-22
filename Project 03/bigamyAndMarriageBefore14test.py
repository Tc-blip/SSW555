import unittest
import datetime as dt
from bigamyAndMarriageBefore14 import noBigamy, marriageAfter14

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

    def __init__(self,id, birt):
        self.ID = id
        self.BIRT = birt

class TestUS11US10(unittest.TestCase):

    def test_noBigamy(self):
        fm1 = Families("F1", "01 JAN 2000", "01 JAN 2008", "I1", "I2", "Abraham", "Betty")
        fm2 = Families("F2", "01 JAN 2005", "01 JAN 2011", "I1", "I3", "Charlie", "Denise")
        fm3 = Families("F3", "01 JAN 2012", "NA", "I4", "I3", "Eddie", "Francesca")
        fm = {"1": fm1, "2": fm2, "3": fm3}
        self.assertEqual(noBigamy(fm), False)

    def test_marriageAfter14(self):
        fm1 = Families("F1", "01 JAN 2000", "01 JAN 2008", "I1", "I2", "Abraham", "Betty")
        fm2 = Families("F2", "01 JAN 2005", "01 JAN 2011", "I1", "I3", "Charlie", "Denise")
        fm3 = Families("F3", "01 JAN 2012", "NA", "I4", "I3", "Eddie", "Francesca")
        fm = {"1": fm1, "2": fm2, "3": fm3}

        p1 = Person_info("I1", "01 JAN 1980")
        p2 = Person_info("I2", "01 JAN 1990")
        p3 = Person_info("I3", "01 JAN 1979")
        p4 = Person_info("I4", "01 JAN 1978")
        ppl = {"I1": p1, "I2": p2, "I3": p3, "I4": p4}
        self.assertEqual(marriageAfter14(fm, ppl), False)



if __name__ == '__main__':
    unittest.main()