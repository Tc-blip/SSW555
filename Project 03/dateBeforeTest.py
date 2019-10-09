import unittest
from datetime import timedelta
import datetime
from dateBefore import birth_before_marriage_p,birth_before_death_p

class TestSprint1Methods(unittest.TestCase):

    def test_birth_before_marriage_p(self):
        """date1 is earliest date, date2 is later date, date3 is equal to first date"""
        Lee_birth = datetime.datetime(2015, 1, 1, 0, 0, 0)
        Lee_marr = datetime.datetime(2016, 1, 1, 0, 0, 0)
        Lee_marr2 = datetime.datetime(2017, 1, 1, 0, 0, 0)
        Lee_marr3 = datetime.datetime(1995, 1, 1, 0, 0, 0)
        self.assertTrue(birth_before_marriage_p(Lee_birth, Lee_marr))
        self.assertTrue(birth_before_marriage_p(Lee_birth, Lee_marr2))
        self.assertFalse(birth_before_marriage_p(Lee_birth, Lee_marr3))
        self.assertFalse(birth_before_marriage_p(Lee_birth, Lee_birth))

    def test_birth_before_death_p(self):
        """date1 is 10 years before the current date, date2 is 5 years before the current date, date3 is 1 year before the current date"""
        Lee_birth = datetime.datetime(2015, 1, 1, 0, 0, 0)
        Lee_deth = datetime.datetime(2016, 1, 1, 0, 0, 0)
        Lee_deth2 = datetime.datetime(2017, 1, 1, 0, 0, 0)
        Lee_deth3 = datetime.datetime(1995, 1, 1, 0, 0, 0)

        self.assertTrue(birth_before_death_p(Lee_birth, Lee_deth))
        self.assertTrue(birth_before_death_p(Lee_birth, Lee_deth2))
        self.assertFalse(birth_before_death_p(Lee_birth, Lee_deth3))
        self.assertFalse(birth_before_death_p(Lee_birth, Lee_birth))


if __name__ == '__main__':
    unittest.main()