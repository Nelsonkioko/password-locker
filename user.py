class User:
    """
    class that contains user details only
    """

    def __init__(self, login, password, email, number):
        """
        This will create unique details for each instance of the User class
        """
        self.login = login
        self.password = password
        self.email = email
        self.number = number



