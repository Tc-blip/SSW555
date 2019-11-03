import unittest
import datetime
from ParentsNotOld import father_not_old,mother_not_old


class TestMethod(unittest.TestCase):


    def test_father_not_old(self):
        date1 = datetime.datetime(1970,3,2,0,0,0)
        date2 = datetime.datetime(1900,4,22,0,0,0)
        date3 = datetime.datetime(2000,2,2,0,0,0)
        self.assertEqual(father_not_old(date1,date3),False)
        self.assertTrue(father_not_old(date2,date3))

    def test_mother_not_old(self):
        date1 = datetime.datetime(1970,3,2,0,0,0)
        date2 = datetime.datetime(1900,4,22,0,0,0)
        date3 = datetime.datetime(2000,2,2,0,0,0)
        self.assertEqual(mother_not_old(date1,date3),False)
        self.assertTrue(mother_not_old(date2,date3))

if __name__ == "__main__":
    unittest.main()