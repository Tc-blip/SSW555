'''
Created: 2019-10-24 18:36:25
Author : Jia Wen
Email : jwen6@stevens.edu
Description: Uniitest for US 30 : list living married
'''
import unittest
from List_living_married import list_living_married

class TestFunction(unittest.TestCase):

    def test_list_living_married(self):
        a = "NA"
        b = "NA"
        c = "11 FEB 1980"
        self.assertNotEqual(list_living_married(a,b),True)
        self.assertTrue(list_living_married(c,b))


if __name__ == "__main__":
    unittest.main()
