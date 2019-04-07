#!/usr/bin/env python3.6
from user import User
from credentials import Credential


def new_user(login, password, email, number):
    """
    create a new instance of user everytime they login
    """
    return User(login, password, email, number)


def add_password(site, username, password):
    """
    Function to add a new password to the passwords array
    """
    new_password = Credential(site, username, password)
    new_password.create_password()


def generate_password(length):
    """
    Generates a random password for the user
    """
    return Credential.generate_password(length) 


def view_passwords():
    """
    Function to view all the passwords
    """
    return Credential.display_passwords()


def delete_password(acc):
    """
    This is a function that will delete the password
    """
    Credential.delete_password()


def main():
    '''
    This is where we call all the functions
    '''

    print('----------------------------')
    print('____Create an account___')
    print('----------------------------')

    Name = input("User Name\n")
    password = input('Password:\n')

    print(f"Welcome {Name}\n")

    while True:
         print("Use these codes : create - creates a password of your choice, gp - generates a new password, dp - display passwords, exit -exit the password-locker ") 

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

             print(f"New password for {site} added!\n")

         elif code == 'gp':
             print ("Social site name ....")
             site = input()

             print ("User name ....")
             username = input()

             print ("Email ....")
             email = input()

             print ("preferd password or skip to generate ....")
             password = input()

             print ("length of password to be generated ....")
             username = input()

             print(f"New password for {site} generated\n")

         elif code == 'dp':
             print ("Social site name ....")
             print (f'{site}')

             print ("Email ....")
             print (f'{email}')

             print ("Number ....")
             print (f'{number}')

             print ("User name ....")
             print (f'{username}')

             print ("password ....")
             print (f'{password}')

         elif code == 'exit':
             print ('Good having you!')
             break

if __name__ == "__main__":
    main()




    

