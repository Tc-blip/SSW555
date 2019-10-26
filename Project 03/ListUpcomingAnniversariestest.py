import unittest
from ListUpcomingAnniversaries import convert_to_same_year, check_if_occur_in_30_days, check_if_living_couple, ListUpcomingAnniversaries

class Person_info:
    __slots__ = ["ID", 'BIRT', 'DEAT']

    def __init__(self,id, Birthday, Death):
        self.ID = id
        self.BIRT = Birthday
        self.DEAT = Death
        

class Test_List_Upcoming_Anniversaries(unittest.TestCase):
    """
    def test_ListUpcomingBirthdays(self):
        p1 = Person_info("1", "01 JAN 2000", "NA")
        p2 = Person_info("2", "01 JAN 2005", "NA")
        p3 = Person_info("3", "01 JAN 2012", "01 JAN 2015")
        p4 = Person_info("4", "28 OCT 2019", "NA")
        pi1 = {'1':p1, '2':p2, '3':p3,}
        pi2 = {'1':p1, '2':p2, '3':p3,'4':p4}
        self.assertEqual(ListUpcomingBirthdays(pi1), [])
        self.assertEqual(ListUpcomingBirthdays(pi2), ['4'])
    """
    def convert_to_same_year(self):
        date1 = "01 JAN 2000"
        date2 = "01 JAN 2005"
        date3 = "28 OCT 2018"
        self.assertEqual(convert_to_same_year(date1),'2019-01-01 00:00:00')
        self.assertEqual(convert_to_same_year(date2),'2019-01-01 00:00:00')
        self.assertEqual(convert_to_same_year(date3),'2019-10-28 00:00:00')



    
if __name__ == "__main__":
    unittest.main()