import unittest
from lessThanFifteen import lessThanFifteen

class TestSprint3Methods(unittest.TestCase):

    def testLessThanFifteen(self):
        ''' Each family should have less than 15 children. '''
        childList1 = [1, 2, 3]
        childList2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        childList3 = []

        self.assertTrue(lessThanFifteen(childList1))
        self.assertFalse(lessThanFifteen(childList2))
        self.assertTrue(lessThanFifteen(childList3))

if __name__ == '__main__':
    unittest.main()