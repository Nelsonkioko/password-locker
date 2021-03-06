


class Credential: 
    """
    Class which we will use to create the passwords
    """
    passwords = []  # array to store passwords

    def __init__(self, site, username, password, email, number):
        """
        This is a function that will allow us to create new instances of sites
        username and password for different users
        """
        self.site = site
        self.username = username
        self.password = password
        self.email = email
        self.number = number

    def create_password(self):
        """
        Function will add the password into the passwords array
        """
        Credential.passwords.append(self)#goes to the Credential class and adds a new password to the array
        
   

    @classmethod
    def display_passwords(cls):
        """
        Function to return all the passwords in the array
        """
        return cls.passwords
     
    @classmethod
    def delete_password(cls, site):
        """
        Function to delete user password from the passwords array
        it loops throgh the array by assigning each password a new variable
        called 'password' and if the site passed in the function matches the site
        in the array, that password is removed
        """
        for password in cls.passwords:
            if password.site.lower() == site.lower():
                cls.passwords.remove(password)
    @classmethod
    def acc_exist(cls,accounts):
        '''
        Method to check if an account exists
        '''
        for account in cls.passwords:
            if account.site == accounts:
                return True

            return False 
    @classmethod
    def find_by_accnt(cls,acc):
        '''
        Method that takes in a number and returns an account that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Account that matches the number.
        '''

        for sites in cls.passwords:
            if sites.site == acc:
                return acc
