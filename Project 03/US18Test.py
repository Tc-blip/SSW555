import unittest
from US18 import noSiblingMarriage

class Families(object):

    def __init__(self,id, Husband_ID, Husband_Name, Wife_ID, Wife_Name, Children):
        self.ID = id
        self.Husband_ID = Husband_ID
        self.Husband_Name = Husband_Name
        self.Wife_ID = Wife_ID
        self.Wife_Name = Wife_Name
        self.Children = Children

class TestUS18(unittest.TestCase):

    def test_noSiblingMarriage(self):
        fm1 = Families("F1", "I1", "Andrew", "I2", "Betty", ["I3", "I5", "I4"])
        fm2 = Families("F2", "I3", "Charlie", "I4", "Dorothy", ["I6"])
        fm3 = Families("F3", "I5", "Edward", "I6", "Francesca", [])
        fm = {"F1": fm1, "F2": fm2, "F3": fm3}
        self.assertEqual(noSiblingMarriage(fm), ["I3", "I4"])

if __name__ == '__main__':
    unittest.main()