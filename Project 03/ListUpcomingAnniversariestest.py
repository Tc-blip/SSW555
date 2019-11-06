import unittest
from ListUpcomingAnniversaries import convert_to_same_year, check_if_occur_in_30_days, check_if_living_couple, ListUpcomingAnniversaries
import datetime as dt
from datetime import timedelta

class Person_info:
    def __init__(self,id, Birthday, Death):
        self.ID = id
        self.BIRT = Birthday
        self.DEAT = Death

class Families:
    def __init__(self,id, married, husband_ID, wife_ID):
        self.ID = id
        self.Married = married
        self.Husband_ID = husband_ID
        self.Wife_ID = wife_ID


f1 = Families('F1','11 FEB 1980','I1','I6')
f2 = Families('F2','31 JAN 2010','I2','I7')
f3 = Families('F3','7 FEB 1999','I2','I8')
f4 = Families('F4','NA',' I1','NA')
f5 = Families('F5','01 DEC 2000','I9','I8')

class Individuals:
    def __init__(self,id, alive):
        self.ID = id
        self.Alive = alive #"True"

I1 = Individuals('I1','False')
I2 = Individuals('I2','False')
I6 = Individuals('I6','True')
I7 = Individuals('I7','True')
I8 = Individuals('I8','True')
I9 = Individuals('I9','True')

fm = {'F1':f1,'F2':f2,'F3':f3,'F4':f4}
fm2 = {'F1':f1,'F2':f2,'F3':f3,'F4':f4,'F5':f5}
indi = {'I1':I1,'I2':I2,'I6':I6,'I7':I7,'I8':I8}
indi2 = {'I1':I1,'I2':I2,'I6':I6,'I7':I7,'I8':I8,'I9':I9}

class Test_List_Upcoming_Anniversaries(unittest.TestCase):

    def test_ListUpcomingAnniversaries(self):
        fm = {'F1':f1, 'F2':f2,'F3':f3,'F4':f4}
        indi = {'I1':I1,'I2':I2,'I6':I6,'I7':I7,'I8':I8}
        self.assertEqual(ListUpcomingAnniversaries(fm,indi),[])
        self.assertEqual(ListUpcomingAnniversaries(fm2,indi2),['F5'])

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