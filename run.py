#!/usr/bin/env python3.6
from user import User
from credentials import Credential
from random import randint #this will allow us to use the randint method
from string import printable #String of characters which are considered printable. This is a combination of digits, letters, punctuation, and whitespace.
# BDD
# As a user, I want to create a password locker account with my details, a login username and password.
# As a user, I want to store my already existing account credentials in the application. Assuming I already have a twitter account, I want to store my already existing twitter username and password in the application.
# As a user, I want to create new account credentials in the application. For example, if I have not yet signed up for Instagram, I would want to create a credentials account for Instagram in the application and the application generates a password for me to use when I sign up for Instagram.
# As a user, I want to have the option of putting in a password that I want to use for the new credential account. For example, when creating my Instagram credential account, I want to have an option of putting in the password I want to use instead of having the application generate a password for me.
# As a user, I also want to view my various account credentials and their passwords in the application.
# As a user, I want to delete a credentials account that I no longer need in the application.


def new_user(login, password,):
    """
    create a new instance of user everytime they login
    """
    return User(login, password)

def create_passwords(site, username, password, email, number):
    '''
    Function to create a new password
    '''
    new_password = Credential(site, username, password, email, number)
    return new_password

def save_password(cridential):
    '''
    Function to save password
    '''
    cridential.create_password ()

def generate_Password(number):
   generated_pwd = ''

   for n in range(number):
       x = randint(0,50)
       generated_pwd = generated_pwd + printable[x]

   return generated_pwd



def display_passwords():
    """
    Function to view all the passwords
    """
    return Credential.display_passwords()


# def delete_password(acc):
#     """
#     This is a function that will delete the password
#     """
#     acc.delete_password()

def check_existing_accnt(accounts):
    '''
    this a function that finds user by account and returns boolean
    '''
    return Credential.acc_exist(accounts)
    
def find_accnt(acc):
    '''
    Function that finds an account by social site name and returns the account
    '''
    return Credential.find_by_accnt(acc)


def main():
    '''
    This is where we call all the functions
    '''

    print('----------------------------')
    print('____Password Locker App___')
    print('----------------------------')

    print('----------------------------')
    print('____Create an account___')
    print('----------------------------')

    Name = input("User Name\n")
    password = input('Password:\n')

    print(f"Welcome {Name}\n")

    while True:
         print ("Use these codes to make requests:")
         print("search - search for accounts")
         print("create - creates a password of your choice")  
         print("gp - generates a new password")
         print("dp - display passwords")
         print("close -exit the password-locker")
        #  print("del - delete passwords")
         code = input().lower()

         if code == 'create':
             print ("Please enter the social media site name of your account i.e Instagram, twitter etc....")
             site = input()

             print ("please enter your account user name ....")
             username = input()

             print ("Please enter your Email ....")
             email = input()

             print ("Please enter your phone number ....")
             number = input()

             print ("Please enter your password ....")
             password = input()

             save_password(create_passwords(site, username, password, email, number)) # create and save new account
             print(f"New password for {site} added!\n")

         elif code == 'gp':
             print ("Social site name ....")
             site = input()

             print ("User name ....")
             username = input()

             print ("Email ....")
             email = input()

             print ("Please enter your phone number ....")
             number = input()

             print ("A random password has been generated ....")
             generated_pwd= generate_Password(10)
             password=  generated_pwd
            
             save_password(create_passwords(site, username, password, email, number))
             print(f"New password for {site} generated\n")

         elif code == 'dp':
             if display_passwords():
                    print("Here is a list of all your account details")
                    print('\n')

                    for pwd in display_passwords():
                            print(f"Account:...{pwd.site}")
                            print(f"Email:... {pwd.email}")
                            print(f"Phone number:...{pwd.number}")
                            print(f"Username:...{pwd.username}")
                            print(f"Password:...{pwd.password}\n")
                            print("[][][][][][][][][][][][][][][][]\n")

                    print('\n')
                    print('\n')
             else:
                    print('\n')
                    print("You dont seem to have any passwords saved yet")
                    print('\n')
        
         elif code == 'search':

                    print("Enter the account you want to search for")

                    search_accnt = input()
                    if check_existing_accnt(search_accnt):
                            search_accnt = find_accnt(search_accnt)
                            for pwd in display_passwords():
                                print(f"Account:...{pwd.site}")
                                print(f"Email:... {pwd.email}")
                                print(f"Phone number:...{pwd.number}")
                                print(f"Username:...{pwd.username}")
                                print(f"Password:...{pwd.password}\n")
                    else:
                            print("That account does not exist \n")
        # elif code == 'del':

            # print("Enter the name of the account you want to delete")

            # number = input()

            # delete_number = find_contact(number)

            # del_contact(delete_number)                       
         elif code == 'close':
             print ('Adios! Adios! Adios!')
             break
         else:
             print ('please use a valid code')

if __name__ == "__main__":
    main()




    

