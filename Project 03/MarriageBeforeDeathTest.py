import unittest
import datetime
from Marriagebeforedeath import check_if_marriage_before_death


class Test_Mcheck_if_marriage_before_death(unittest.TestCase):

    def test_mcheck_if_marriage_before_death(self):
        # return 1 means wife die before marriage.
        # return 2 means husband die before marriage.
        # return 3 means bot parent die before marriage.
        Lee_marr_date = datetime.datetime(2015, 1, 1, 0, 0, 0)
        Lee_hus_death = datetime.datetime(2016, 1, 1, 0, 0, 0)
        Lee_wife_death = datetime.datetime(2017, 1, 1, 0, 0, 0)

        Dan_marr_date = datetime.datetime(1995, 1, 1, 0, 0, 0)
        Dan_hus_death = datetime.datetime(1994, 1, 1, 0, 0, 0)
        Dan_wife_death = datetime.datetime(1996, 1, 1, 0, 0, 0)

        self.assertTrue(check_if_marriage_before_death(Lee_marr_date, Lee_hus_death, Lee_wife_death))
        self.assertEqual(check_if_marriage_before_death(Dan_marr_date, Dan_hus_death, Dan_wife_death),'3')
        self.assertTrue(check_if_marriage_before_death(Dan_marr_date, "NA", Dan_wife_death))
        self.assertEqual(check_if_marriage_before_death(Dan_marr_date, Dan_hus_death, "NA"),'2')
        self.assertTrue(check_if_marriage_before_death("NA", Dan_hus_death, Dan_wife_death))
    
        
if __name__ == '__main__':
    unittest.main()