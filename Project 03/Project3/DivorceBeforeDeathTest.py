import unittest
import datetime
from DivorceBeforeDeath import divorce_before_death
class TestDivorceBeforeDeath(unittest.TestCase):

    def test_divorce_before_death(self):
        # return 1 means wife died before marriage!
        # return 2 means husband died before marriage!
        # return 3 means husband and wife both died before marriage! 
        a_divorce_date = "NA"
        L2015_date = datetime.datetime(2015, 1, 1, 0, 0, 0)
        NA_death_date = "NA"
        c2014_date = datetime.datetime(2014, 1, 1, 0, 0, 0)
        L2016_death = datetime.datetime(2016, 1, 1, 0, 0, 0)
        L2017_death = datetime.datetime(2017, 1, 1, 0, 0, 0)
        
        self.assertTrue(divorce_before_death(a_divorce_date, NA_death_date, NA_death_date))
        self.assertTrue(divorce_before_death(a_divorce_date, L2016_death, NA_death_date))
        self.assertTrue(divorce_before_death(a_divorce_date, NA_death_date, L2017_death))
        self.assertTrue(divorce_before_death(L2015_date, NA_death_date, NA_death_date))
        self.assertTrue(divorce_before_death(L2015_date, L2016_death, NA_death_date))
        self.assertEqual(divorce_before_death(L2015_date, c2014_date, NA_death_date),2)
        self.assertEqual(divorce_before_death(L2015_date, c2014_date, c2014_date),3)
        self.assertEqual(divorce_before_death(L2015_date, L2016_death, c2014_date),1)
        

if __name__ == "__main__":
     unittest.main()