"""
Chih-Yu Lee
sprint 3
List upcoming birthdays:
List all living people in a GEDCOM file whose birthdays occur in the next 30 days
"""
import unittest
from ListUpcomingBirthdays import ListUpcomingBirthdays

class Person_info:
    def __init__(self,id, Birthday, Death):
        self.ID = id
        self.BIRT = Birthday
        self.DEAT = Death

p1 = Person_info("1", "01 JAN 2000", "NA")
p2 = Person_info("2", "01 JAN 2005", "NA")
p3 = Person_info("3", "01 JAN 2012", "01 JAN 2015")
p4 = Person_info("4", "02 DEC 2019", "NA")

pi1 = {'1':p1, '2':p2, '3':p3,}
pi2 = {'1':p1, '2':p2, '3':p3,'4':p4}

class Test_List_upcoming_birthdays(unittest.TestCase):
    def test_ListUpcomingBirthdays(self):
        self.assertEqual(ListUpcomingBirthdays(pi1), [])
        self.assertEqual(ListUpcomingBirthdays(pi2), ['4'])

    
if __name__ == "__main__":
    unittest.main()