from List_living_single import check_living_single
import unittest

class TestFunction(unittest.TestCase):


    def test_check_living_single(self):

        death1 = "23 FEB 1992"
        death2 = "NA"
        spouse1 = ["A","B"]
        spouse2 = []
        self.assertEqual(check_living_single(death2,spouse2),True)
        self.assertFalse(check_living_single(death1,spouse1))

if __name__ == "__main__":
    unittest.main()