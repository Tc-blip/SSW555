import unittest
from datetime import timedelta
import datetime
from BirthBeforeMorDofParents import birthAfterMarriageOfParents, birthBeforeDeathOfParents

class TestSprint1Methods(unittest.TestCase):

    def testBirthAfterMarriageOfParents(self):
        ''' Child must be born after the parents' wedding or before 9 months after their divorce '''
        child_bday_1 = '1 Jan 2019'
        child_bday_2 = '1 Jan 1990'
        wedding_date_1 = '1 Jan 2018'
        wedding_date_2 = '1 Jan 1985'
        divorce_date = '2 Jan 2018'
        self.assertTrue(birthAfterMarriageOfParents(child_bday_1, wedding_date_1, 'NA'))
        self.assertTrue(birthAfterMarriageOfParents(child_bday_1, wedding_date_2, 'NA'))
        self.assertFalse(birthAfterMarriageOfParents(child_bday_1, wedding_date_1, divorce_date))
        self.assertFalse(birthAfterMarriageOfParents(child_bday_2, wedding_date_1, 'NA'))
        self.assertTrue(birthAfterMarriageOfParents(child_bday_2, wedding_date_2, 'NA'))
        self.assertFalse(birthAfterMarriageOfParents(child_bday_2, wedding_date_1, divorce_date))

    def testBirthBeforeDeathOfParents(self):
        ''' Child must be born before the death of their mother and before 9 months after the father's death '''
        child_bday_1 = '5 Jan 2015'
        child_bday_2 = '1 Jan 2019'
        wife_death_1 = '1 Jan 2018'
        wife_death_2 = '1 Jan 2014'
        husband_death_1 = '1 Jan 2018'
        husband_death_2 = '1 Jan 2015'
        self.assertTrue(birthBeforeDeathOfParents(child_bday_1, wife_death_1, husband_death_1))
        self.assertFalse(birthBeforeDeathOfParents(child_bday_1, wife_death_2, husband_death_1))
        self.assertTrue(birthBeforeDeathOfParents(child_bday_1, wife_death_1, husband_death_2))
        self.assertFalse(birthBeforeDeathOfParents(child_bday_2, wife_death_1, husband_death_2))

if __name__ == '__main__':
    unittest.main()