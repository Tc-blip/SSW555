import unittest
from ListUpcomingAnniversaries import convert_to_same_year, check_if_occur_in_30_days, check_if_living_couple, ListUpcomingAnniversaries
import datetime as dt
from datetime import timedelta

class Person_info:
    __slots__ = ["ID", 'BIRT', 'DEAT']

    def __init__(self,id, Birthday, Death):
        self.ID = id
        self.BIRT = Birthday
        self.DEAT = Death
        

class Test_List_Upcoming_Anniversaries(unittest.TestCase):
        
    def test_convert_to_same_year(self):
        date1 = "01 JAN 2000"
        date2 = "01 JAN 2005"
        date3 = "29 OCT 2018"
        date1 = dt.datetime.strptime(date1,"%d %b %Y")
        date2 = dt.datetime.strptime(date2,"%d %b %Y")
        date3 = dt.datetime.strptime(date3,"%d %b %Y")
        test_date1 = dt.datetime.strptime("01 JAN 2019","%d %b %Y")
        test_date2 = dt.datetime.strptime("01 JAN 2019","%d %b %Y")
        test_date3 = dt.datetime.strptime("29 OCT 2019","%d %b %Y")
        self.assertEqual(convert_to_same_year(date1),test_date1)
        self.assertEqual(convert_to_same_year(date2),test_date2)
        self.assertEqual(convert_to_same_year(date3),test_date3)
    
    def test_check_if_occur_in_30_days(self):
        date1 = "01 JAN 2000"
        date2 = "01 JAN 2005"
        date1 = dt.datetime.strptime(date1,"%d %b %Y")
        date2 = dt.datetime.strptime(date2,"%d %b %Y")
        date3 = dt.datetime.now()
        date3 += timedelta(days = 1)
        date1 = convert_to_same_year(date1)
        date2 = convert_to_same_year(date2)
        date3 = convert_to_same_year(date3)
        self.assertEqual(check_if_occur_in_30_days(date1),False)
        self.assertEqual(check_if_occur_in_30_days(date2),False)
        self.assertEqual(check_if_occur_in_30_days(date3),True)

    
if __name__ == "__main__":
    unittest.main()