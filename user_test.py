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
        self.new_user = User("kioko", "Giz", "kiokonelson2@gmail.com", "0777770089")

    def test_init(self):
        """
        This will test whether the user is created correctly;
        """
        self.assertEqual(self.new_user.login, "kioko")
        self.assertEqual(self.new_user.password, "Giz")
        self.assertEqual(self.new_user.password, "kiokonelson2@gmail.com")
        self.assertEqual(self.new_user.password, "0777770089")

if __name__ == "__main__":
    unittest.main()