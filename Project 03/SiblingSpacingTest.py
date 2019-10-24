import unittest
from SiblingSpacing import listSiblings, siblingSpacing

class Families:
    def __init__(self,id,children):
        self.ID = id
        self.Children = children

class Individuals:
    def __init__(self,id,bday,age):
        self.ID = id
        self.Birthday = bday
        self.Age = age

class TestSprint2Methods(unittest.TestCase):

    def testListSibling(self):
        ''' Lists siblings in descending order, i.e. oldest sibling first '''
        child1 = Individuals('1', '1 Jan 2010', 9)
        child2 = Individuals('2', '1 Jan 2011', 8)
        child3 = Individuals('3', '1 Jan 2012', 7)
        child4 = Individuals('4', '1 Jan 2009', 10)
        child5 = Individuals('5', '1 Jan 2000', 19)
        childList1 = [child1, child2, child3]
        childList2 = [child4, child5]
        # Get ages out of sorted list for easy check
        sortList1 = listSiblings(childList1)
        for i in range(len(sortList1)):
            sortList1[i] = sortList1[i].Age
        sortList2 = listSiblings(childList2)
        for i in range(len(sortList2)):
            sortList2[i] = sortList2[i].Age

        self.assertEqual(listSiblings([]), [])
        self.assertEqual(sortList1, [9, 8, 7])
        self.assertEqual(sortList2, [19, 10])

    def testSiblingSpacing(self):
        ''' Siblings should be born more than 8 months or less than 2 days afer each other '''
        child1 = Individuals('1', '1 Jan 2010', 9)
        child2 = Individuals('2', '1 Jan 2015', 4)
        child3 = Individuals('3', '2 Jan 2011', 8)
        child4 = Individuals('4', '5 Jan 2011', 8)
        child5 = Individuals('5', '9 Jan 2011', 8)
        childList1 = [child1, child2, child3]
        childList2 = [child4, child5]

        self.assertTrue(siblingSpacing([]))
        self.assertTrue(siblingSpacing(childList1))
        self.assertFalse(siblingSpacing(childList2))

if __name__ == '__main__':
    unittest.main()