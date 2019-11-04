'''
Created: 2019-10-23 17:10:08
Author : Jia Wen
Email : jwen6@stevens.edu
Description: Unittest for Unique ID
'''
import unittest
from UniqueID import check_unique_id

class TestFunction(unittest.TestCase):

    def test_check_unique_id(self):
        list1 = [1,2,3,4,5,6,6,6]
        list2 = [1,1,1,1,1,3,4]
        self.assertEqual(check_unique_id(list1,list2),[6,1])

if __name__ == "__main__":
    unittest.main()