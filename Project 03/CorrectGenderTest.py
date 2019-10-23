import unittest
from CorrectGender import correct_gender

class TestFunction(unittest.TestCase):

    def test_correct_gender(self):
        gender1 = "M"
        gender2 = "F"
        gender3 = "M"
        self.assertTrue(correct_gender(gender1,gender2))
        self.assertFalse(correct_gender(gender1,gender3))
        self.assertEqual(correct_gender(gender1,gender2),True)

if __name__ == "__main__":
    unittest.main()