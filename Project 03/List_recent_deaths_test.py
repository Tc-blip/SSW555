import unittest
import datetime 
from List_recent_deaths import check__died_in_30


class Test_check__died_in_30(unittest.TestCase):

    def test_check__died_in_30(self):
        # return 1 means wife die before marriage.
        # return 2 means husband die before marriage.
        # return 3 means bot parent die before marriage.
        dt_now = datetime.datetime(2019, 10, 17, 1, 0, 0)
        dt1 = datetime.datetime(2019, 10, 16, 0, 0, 0)

        dt2 = datetime.datetime(2019, 9, 17, 0, 0, 0)
        dt3 = datetime.datetime(2019, 9, 18, 0, 0, 0)
        dt4 = datetime.datetime(1996, 9, 15, 0, 0, 0)

        dt5 = datetime.datetime(2019, 11, 16, 0, 0, 0)
        dt6 = datetime.datetime(2019, 11, 15, 0, 0, 0)
        dt7 = datetime.datetime(2019, 11, 17, 0, 0, 0)
        dt8 = datetime.datetime(2019, 11, 18, 0, 0, 0)

        self.assertEqual(check__died_in_30(dt1,dt_now,'LEE'),'LEE were died in last 30 days, death 1 days')
        self.assertEqual(check__died_in_30(dt2,dt_now,'BB'),None)
        self.assertEqual(check__died_in_30(dt3,dt_now,'AA'),'AA were died in last 30 days, death 29 days')
        self.assertEqual(check__died_in_30(dt4,dt_now,'CC'),None)
        self.assertEqual(check__died_in_30(dt5,dt_now,'DD'),'DD were died in last 30 days, death 29 days')
        self.assertEqual(check__died_in_30(dt6,dt_now, 'EE'),'EE were died in last 30 days, death 28 days')
        self.assertEqual(check__died_in_30(dt7,dt_now, 'FF'),None)
        self.assertEqual(check__died_in_30(dt8,dt_now, 'GG'),None)
    
        
if __name__ == '__main__':
    unittest.main()