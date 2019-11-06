import unittest
from US29 import listDeceased

class Individuals:
    def __init__(self,id, Alive):
        self.ID = id
        self.Alive = Alive

class TestUS29(unittest.TestCase):

    def test_listDeceased(self):
        indi1 = Individuals("I1", "True")
        indi2 = Individuals("I2", "True")
        indi3 = Individuals("I3", "False")
        indi4 = Individuals("I4", "True")
        indi5 = Individuals("I5", "False")
        indi = {"1": indi1, "2": indi2, "3": indi3, "4": indi4, "5": indi5}
        self.assertEqual(listDeceased(indi), ["I3", "I5"])



if __name__ == '__main__':
    unittest.main()