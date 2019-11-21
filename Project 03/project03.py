from AuntAndUncles import check_Aunt_and_Uncles
from CorrespondingEntries import check_Corresponding_Entries
import unittest

class TestUserStory(unittest.TestCase):
    #tests for user story 20 & 26
    
    def test_check_Aunt_and_Uncles(self):
        '''US 20 test '''
        self.assertEqual(check_Aunt_and_Uncles(fm,indi), {'@F9@'})

    def test_check_Corresponding_Entries(self):
        ''' US 26 test'''
        self.assertEqual(check_Corresponding_Entries(fm, indi), {'@I15@', '@I14@'})





    

    # except US40,41


    check_Aunt_and_Uncles(fm,indi)                      #20 --sprint 4
    check_Corresponding_Entries(fm,indi)                #26 --sprint 4
    unittest.main()                                     #20&26 test --sprint 4
