import unittest
from datetime import timedelta
import datetime
from BirthBeforeMorD import birth_before_marriage_p,birth_before_death_p

class TestSprint1Methods(unittest.TestCase):

    def test_birth_before_marriage_p(self):
        """date1 is earliest date, date2 is later date, date3 is equal to first date"""
        Lee_birth = '1 JAN 2015'
        Lee_marr = '1 JAN 2016'
        Lee_marr2 = '1 JAN 2017'
        Lee_marr3 = '1 JAN 1995'
        self.assertTrue(birth_before_marriage_p(Lee_birth, Lee_marr))
        self.assertTrue(birth_before_marriage_p(Lee_birth, Lee_marr2))
        self.assertFalse(birth_before_marriage_p(Lee_birth, Lee_marr3))
        self.assertFalse(birth_before_marriage_p(Lee_birth, Lee_birth))

    def test_birth_before_death_p(self):
        """date1 is 10 years before the current date, date2 is 5 years before the current date, date3 is 1 year before the current date"""
        Lee_birth = '1 JAN 2015'
        Lee_deth = '1 JAN 2016'
        Lee_deth2 = '1 JAN 2017'
        Lee_deth3 = '1 JAN 1995'

        self.assertTrue(birth_before_death_p(Lee_birth, Lee_deth))
        self.assertTrue(birth_before_death_p(Lee_birth, Lee_deth2))
        self.assertFalse(birth_before_death_p(Lee_birth, Lee_deth3))
        self.assertFalse(birth_before_death_p(Lee_birth, Lee_birth))


if __name__ == '__main__':
    unittest.main()