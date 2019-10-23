import unittest
from MultipleBirths import check_if_more_than_5_children

class TestMultipleBirth(unittest.TestCase):

    def test_check_if_more_than_5_children(self):

        dict1 = {"5 DEC 2010":1, '18 JUN 2000': 1, '2 AUG 2001': 1}
        dict2 = {"5 DEC 2010":5, '18 JUN 2000': 1, '2 AUG 2001': 1}
        dict3 = {"5 DEC 2010":6, '18 JUN 2000': 1, '2 AUG 2001': 1}
        dict4 = {}

        self.assertTrue(check_if_more_than_5_children(dict1))
        self.assertTrue(check_if_more_than_5_children(dict2))
        self.assertFalse(check_if_more_than_5_children(dict3))
        self.assertTrue(check_if_more_than_5_children(dict4))

if __name__ == "__main__":
    unittest.main()    