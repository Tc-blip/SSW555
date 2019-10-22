import unittest

from MaleLastName import male_last_name

class TestMethod(unittest.TestCase):

    def test_male_last_name(self):
        name1 = 'SNOW'
        name2 = 'Jackson'
        name3 = 'Wang'
        name4 = 'Wang'
        self.assertTrue(male_last_name(name3,name4))
        self.assertFalse(male_last_name(name1,name2))


if __name__ == "__main__":
    unittest.main()