import unittest
from US37 import List_recent_survivors


class Families:
    def __init__(self,id,husID,husName,wifeID,wifeName,child):
        self.ID = id
        self.Husband_ID = husID
        self.Husband_Name = husName
        self.Wife_ID = wifeID
        self.Wife_Name = wifeName
        self.Children = child

class Individuals:
    def __init__(self,id,name,gen,alive,death,spou):
        self.ID = id
        self.Name = name
        self.Gender = gen
        self.Alive = alive
        self.Death = death
        self.Spouse = spou

class TestFunction(unittest.TestCase):
    def test_check_unique_fm_by_spouses(self):
        indi1 = Individuals("I01","Joe /Smith/","M","False","30 Oct 2019",["F1"])
        indi2 = Individuals("I02","Jennifer /Smith/","F","True","NA",["F1"])
        indi3 = Individuals("I03","Dick /Smith/","F","True","NA","")
        indi4 = Individuals("I04","Jane /Smith/","M","True","NA","")

        fm_F1 = Families("F1","I01","Joe /Smith/","I02","Jennifer /Smith/",["I03","I04"])
        fm1 = {"F1":fm_F1} 
        indi = {"I01":indi1,"I02":indi2,"I03":indi3,"I04":indi4}
        self.assertEqual(List_recent_survivors(fm1,indi),"Joe /Smith/ died in the last 30 days, living spouse Jennifer /Smith/, living children ['Dick /Smith/', 'Jane /Smith/']")

if __name__ == "__main__":
    unittest.main()