import project03
from CorrespondingEntries import check_Corresponding_Entries
import unittest

class TestUS26(unittest.TestCase):

    def test_check_Corresponding_Entries(self):
        self.assertEqual(check_Corresponding_Entries(project03.fm, project03.indi), {'@I15@', '@I14@'})

if __name__ == "__main__":
    unittest.main()