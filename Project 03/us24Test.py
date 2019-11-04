import unittest
from US24 import check_unique_fm_by_spouses

class Families:
    def __init__(self,mar,hus_name,wifi_name):
        self.Married = mar
        self.Husband_Name = hus_name
        self.Wife_Name = wifi_name


class TestFunction(unittest.TestCase):
    def test_check_unique_fm_by_spouses(self):
        fm1 = Families("14 FEB 1980","Joe /Smith/","Jennifer /Smith/")
        fm2 = Families("14 FEB 1980","Joe /Smith/","Jennifer /Smith/")
        fm3 = Families("14 FEB 2000","Joe /Smith/","Jennifer /Smith/")
        fm4 = Families("14 FEB 1980","Other","Jennifer /Smith/")
        fm5 = Families("14 FEB 1980","Joe /Smith/","wife")

        fm = {1:fm1,2:fm2,3:fm3,4:fm4,5:fm5} 
        
        self.assertEqual(check_unique_fm_by_spouses(fm),"Error, same has already in GEDCOM ('14 FEB 1980', 'Joe /Smith/', 'Jennifer /Smith/')")

if __name__ == "__main__":
    unittest.main()