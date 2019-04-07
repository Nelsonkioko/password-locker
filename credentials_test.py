import unittest
from credentials import Credential


class TestCredentials(unittest.TestCase):
    """
    Class to perform credentials test
    """
    def setUp(self):
        """
        This function will create a new instance of Password before each test
        """
        self.new_password = Credential("twitter", "kioko", "Giz")

    def test_new_password(self):
        """
        Test whether a new password is instantiated correctly
        """
        self.assertEqual(self.new_password.site, "twitter")
        self.assertEqual(self.new_password.username, "kioko")
        self.assertEqual(self.new_password.password, "Giz")

    def test_save_new_passssword(self): 
        """
        Check whether the new password is added to the passwords array
        """
        self.new_password.create_password()
        self.assertEqual(len(Credential.passwords), 1)

if __name__ == "__main__":
    unittest.main()