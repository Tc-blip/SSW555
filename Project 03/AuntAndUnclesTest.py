import project03
import unittest
from AuntAndUncles import check_Aunt_and_Uncles

class TestUserStory(unittest.TestCase):

    def test_check_Aunt_and_Uncles(self):
        result = check_Aunt_and_Uncles(project03.fm,project03.indi)
        self.assertEqual(result, {'@F9@'})


if __name__ == "__main__":
    unittest.main()
