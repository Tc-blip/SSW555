import unittest
import datetime

from Use12 import parents_not_old, male_last_name

class TestMethod(unittest.TestCase):

    def test_parents_not_old(self):
        date1 = datetime.datetime(1970,3,2,0,0,0)
        date2 = datetime.datetime(1980,4,22,0,0,0)
        date3 = datetime.datetime(2000,2,2,0,0,0)
        self.assertEqual(parents_not_old(date1,date2,date3),2)

    def test_male_last_name(self):
        name1 = 'SNOW'
        name2 = 'Jackson'
        name3 = 'Wang'
        name4 = 'Wang'
        self.assertTrue(male_last_name(name3,name4))
        self.assertFalse(male_last_name(name1,name2))


if __name__ == "__main__":
    unittest.main()
