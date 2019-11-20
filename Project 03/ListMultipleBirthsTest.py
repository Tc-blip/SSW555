"""
Chih-Yu Lee
US32 ListMultipleBirths test
"""
import unittest
from ListMultipleBirths import listMultipleBirths

class Person_info:
    def __init__(self,id, birthday):
        self.ID = id
        self.BIRT = birthday

class Families:
    def __init__(self,id,child):
        self.ID = id
        self.Children = child

f1 = Families('f1',['I1','I2','I3'])
f2 = Families('f2',['I1','I1','I3'])
f3 = Families('f3',['I1','I1','I1'])
f4 = Families('f4',[])
f5 = Families('f5',['I1','I4'])

I1 = Person_info('I1', '2 AUG 2000')
I2 = Person_info('I2', '2 FEB 1910')
I3 = Person_info('I3', '3 MAR 1981')
I4 = Person_info('I4', '2 AUG 2000')

fm1= {'f1':f1,'f2':f2,'f3':f3,'f4':f4}
fm2= {'f1':f1,'f2':f2,'f3':f3,'f4':f4,'f5':f5}
pi = {'I1':I1,'I2':I2,'I3':I3,'I4':I4}

class Test_listMultipleBirths(unittest.TestCase):
    def test_listMultipleBirths(self):
        outputlist = [['2 AUG 2000',['I1','I1']],['2 AUG 2000',['I1','I1','I1']]]
        outputlist2 = [['2 AUG 2000',['I1','I1']],['2 AUG 2000',['I1','I1','I1']],['2 AUG 2000',['I1','I4']]]
        self.assertAlmostEqual(listMultipleBirths(fm1,pi), outputlist)
        self.assertAlmostEqual(listMultipleBirths(fm2,pi), outputlist2)

if __name__ == "__main__":
    unittest.main()