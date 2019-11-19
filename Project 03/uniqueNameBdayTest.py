import unittest
from uniqueNameBday import uniqueNameBday

class TestSprint3Methods(unittest.TestCase):

    def testUniqueNameBday(self):
        testList1 = [
        'Tom1 Jan 2010',
        'Tom1 Jan 2011',
        'Jerry1 Jan 2011',
        'Will1 Jan 2010']
        testList2 = [
        'Tom1 Jan 2010',
        'Bill1 Jan 2011',
        'Tom1 Jan 2011',
        'Tom1 Jan 2010']

        self.assertTrue(uniqueNameBday(testList1))
        self.assertFalse(uniqueNameBday(testList2))

if __name__ == '__main__':
    unittest.main()