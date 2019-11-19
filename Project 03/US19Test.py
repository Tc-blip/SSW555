import unittest
from US19 import noCousinMarriage, findFirstCousins, findSiblings, findChildren

class Families(object):

    def __init__(self,id, Husband_ID, Husband_Name, Wife_ID, Wife_Name, Children):
        self.ID = id
        self.Husband_ID = Husband_ID
        self.Husband_Name = Husband_Name
        self.Wife_ID = Wife_ID
        self.Wife_Name = Wife_Name
        self.Children = Children

class TestUS19(unittest.TestCase):

    fm1 = Families("F1", "I1", "Andrew", "I2", "Betty", ["I3", "I5"])
    fm2 = Families("F2", "I3", "Charlie", "I4", "Dorothy", ["I7"])
    fm3 = Families("F3", "I5", "Edward", "I6", "Francesca", ["I8"])
    fm4 = Families("F4", "I7", "George", "I8", "Harriet", [])
    fm5 = Families("F5", "I9", "Inigo", "I10", "Julia", [])
    fm = {"F1": fm1, "F2": fm2, "F3": fm3, "F4": fm4, "F5": fm5}

    def test_noCousinMarriage(self):
        fm1 = Families("F1", "I1", "Andrew", "I2", "Betty", ["I3", "I5"])
        fm2 = Families("F2", "I3", "Charlie", "I4", "Dorothy", ["I7"])
        fm3 = Families("F3", "I5", "Edward", "I6", "Francesca", ["I8"])
        fm4 = Families("F4", "I7", "George", "I8", "Harriet", [])
        fm5 = Families("F5", "I9", "Inigo", "I10", "Julia", [])
        fm = {"F1": fm1, "F2": fm2, "F3": fm3, "F4": fm4, "F5": fm5}
        self.assertEqual(noCousinMarriage(fm), False)

    def test_findSiblings(self):
        fm1 = Families("F1", "I1", "Andrew", "I2", "Betty", ["I3", "I5"])
        fm2 = Families("F2", "I3", "Charlie", "I4", "Dorothy", ["I7"])
        fm3 = Families("F3", "I5", "Edward", "I6", "Francesca", ["I8"])
        fm4 = Families("F4", "I7", "George", "I8", "Harriet", [])
        fm5 = Families("F5", "I9", "Inigo", "I10", "Julia", [])
        fm = {"F1": fm1, "F2": fm2, "F3": fm3, "F4": fm4, "F5": fm5}
        self.assertEqual(findSiblings("I3", fm), ['I3', 'I5'])

    def test_findFirstCousins(self):
        fm1 = Families("F1", "I1", "Andrew", "I2", "Betty", ["I3", "I5"])
        fm2 = Families("F2", "I3", "Charlie", "I4", "Dorothy", ["I7"])
        fm3 = Families("F3", "I5", "Edward", "I6", "Francesca", ["I8"])
        fm4 = Families("F4", "I7", "George", "I8", "Harriet", [])
        fm5 = Families("F5", "I9", "Inigo", "I10", "Julia", [])
        fm = {"F1": fm1, "F2": fm2, "F3": fm3, "F4": fm4, "F5": fm5}
        self.assertEqual(findFirstCousins("I7", fm), [['I7'], ['I8']])

    def test_findChildren(self):
        fm1 = Families("F1", "I1", "Andrew", "I2", "Betty", ["I3", "I5"])
        fm2 = Families("F2", "I3", "Charlie", "I4", "Dorothy", ["I7"])s
        fm3 = Families("F3", "I5", "Edward", "I6", "Francesca", ["I8"])
        fm4 = Families("F4", "I7", "George", "I8", "Harriet", [])
        fm5 = Families("F5", "I9", "Inigo", "I10", "Julia", [])
        fm = {"F1": fm1, "F2": fm2, "F3": fm3, "F4": fm4, "F5": fm5}
        self.assertEqual(findChildren("I1", fm), ['I3', 'I5'])


if __name__ == '__main__':
    unittest.main()