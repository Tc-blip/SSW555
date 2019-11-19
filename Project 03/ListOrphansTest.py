"""
Chih-Yu Lee
US33
list Orphans
List all orphaned children (both parents dead and child < 18 years old) in a GEDCOM file
"""
import unittest
from ListOrphans import listOrphans

class Families:
    def __init__(self,id,HID,WID):
        self.ID = id
        self.Husband_ID = HID#"NA"
        self.Wife_ID = WID#"NA"

class Individuals:
    def __init__(self,id,age,alive,death,spouse):
        self.ID = id
        self.Age = age
        self.Alive = alive#"True"
        self.Death = death#"NA"
        self.Spouse = spouse#[]

I1 = Individuals('I1',17,'True','NA',['F1']) 
I2 = Individuals('I2',19,'False','NA',['F4']) 
I3 = Individuals('I3',20,'False','NA',['F2']) #not orph >18
I4 = Individuals('I4',18,'False','NA',[])
I5 = Individuals('I5',17,'True','NA',['F1'])

F1 = Families('F1','I2','I3') #orph
F2 = Families('F2','I2','I4') #orph
F3 = Families('F3','I2','I5') #not orph
F4 = Families('F4','I4','I5') #not orph


fm = {'F1':F1,'F2':F2,'F3':F3,'F4':F4}
indi = {'I1':I1,'I2':I2,'I3':I3,'I4':I4,'I5':I5}

class Test_listOrphans(unittest.TestCase):
    def test_listOrphans(self):
        self.assertAlmostEqual(listOrphans(fm,indi),['I1','I5'])

if __name__ == "__main__":
    unittest.main()