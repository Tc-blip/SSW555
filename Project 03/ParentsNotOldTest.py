import unittest
import datetime

from ParentsNotOld import parents_not_old


class TestMethod(unittest.TestCase):

    def test_parents_not_old(self):
        date1 = datetime.datetime(1970,3,2,0,0,0)
        date2 = datetime.datetime(1980,4,22,0,0,0)
        date3 = datetime.datetime(2000,2,2,0,0,0)
        self.assertEqual(parents_not_old(date1,date2,date3),2)

if __name__ == "__main__":
    unittest.main()