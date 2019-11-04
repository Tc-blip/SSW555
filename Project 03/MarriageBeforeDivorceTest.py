import unittest
import datetime
from MarriageBeforeDivorce import marriage_before_divorce

class Test_MarriageBeforeDivorce(unittest.TestCase):

    def test_marriage_before_divorce(self):
        Lee_birth = datetime.datetime(2015, 1, 1, 0, 0, 0)
        Lee_marr = datetime.datetime(2016, 1, 1, 0, 0, 0)
        Lee_marr2 = datetime.datetime(2017, 1, 1, 0, 0, 0)
        Lee_marr3 = datetime.datetime(1995, 1, 1, 0, 0, 0)
        self.assertTrue(marriage_before_divorce(Lee_birth, Lee_marr))
        self.assertTrue(marriage_before_divorce(Lee_birth,"NA"))
        self.assertFalse(marriage_before_divorce(Lee_marr2,Lee_marr3))
        
if __name__ == '__main__':
    unittest.main()