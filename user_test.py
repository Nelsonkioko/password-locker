import unittest
from user import User


class TestUser(unittest.TestCase):
    """
    Class to test user class;
    """
    def setUp(self):
        """
        This will create a new user before each test;
        """
        self.new_user = User("kioko", "Giz")

    def test_init(self):
        """
        This will test whether the user is created correctly;
        """
        self.assertEqual(self.new_user.login, "kioko")
        self.assertEqual(self.new_user.password, "Giz")

if __name__ == "__main__":
    unittest.main()