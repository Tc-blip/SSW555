"""
Chih-Yu Lee
US33
list Orphans
List all orphaned children (both parents dead and child < 18 years old) in a GEDCOM file
"""
import unittest
import ListOrphans

class Families:
    def __init__(self,id):
        self.ID = id
        self.Husband_ID = "NA"
        self.Wife_ID = "NA"

class Individuals:
    def __init__(self,id):
        self.ID = id
        self.Age = ""
        self.Alive = "True"
        self.Death = "NA"
        self.Spouse = []

class Test_listOrphans(unittest.TestCase):
    def test_listOrphans(self):
        self.assertAlmostEqual(listOrphans(),)

if __name__ == "__main__":
    unittest.main()