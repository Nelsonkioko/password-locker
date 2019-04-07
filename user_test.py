import unittest
from user import User


class TestUser(unittest.TestCase):
    """
    Class that will contain all the tests for the user class;
    """
    def setUp(self):
        """
        This will create a new user before each test;
        """
        self.new_user = User("Buyukah", "0505")

    def test_init(self):
        """
        This will test whether the user is created correctly;
        """
        self.assertEqual(self.new_user.login, "Buyukah")
        self.assertEqual(self.new_user.password, "0505")

if __name__ == "__main__":
    unittest.main()