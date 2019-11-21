import unittest
import project03
from AuntAndUncles import check_Aunt_and_Uncles

class Test(unittest.TestCase):
    
    def check_aunt_and_uncles(self):
        self.assertEqual(check_Aunt_and_Uncles,{})

if __name__ == "__main__":
    unittest.main()