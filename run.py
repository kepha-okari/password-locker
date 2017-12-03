#!/usr/bin/env python3.6
'''
THE RUN MODULE
THIS IS THE MAIN MODULE THAT ENABLES THE APPLICATION TO WORK.
IT ACHIEVES THIS BY CALLING VARIUOS METHODS IN THE TWO MODULES
Import User Class from User Module and Credential Class from Credential Module
'''
from user import User
from credential import Credential

def create_user(name, password):
    new_user = User(name,password)

    return new_user

def save_users(user):
    user.save_user()

def check_existing_users(name):
    return User.user_exist(name)

def user_log_in(name, password):
    log_in = User.log_in(name, password)
    if log_in != False:
        return User.log_in(name, password)

def display_users():
    return User.display_user()

def create_credentail(user_password, name, password):
    new_credentail = Credential(user_password,name,password)
    return new_credentail

def save_credentials(credential):
    credential.save_credential()

def check_existing_credentials(name):
    return Credential.credential_exist(name)

def display_credentials(password):
    return Credential.display_credential(password)

def create_generated_password(name):
    password = Credential.generate_password()
    return password

def main():
    print('''WELCOME TO PASSWORD LOCKER!!! \n ''')

    while True:

        print('''SHORT CODES: \n
        (cu) - CREATE PASSWORD LOCKER ACCOUNT \n
        (du) - DISPLAY USERS OF PASSWORD LOCKER \n
        (lg) - LOG INTO YOUR PASSWORD LOCKER ACOUNT \n
        (ex) - EXIT PASSWORD LOCKER ACCOUNT''')

        # Get short codes from the user
        short_code = input().lower()

        if short_code == 'cu':

            print("\n")
            print("New Password Locker Account")
            print("-"*10)

            print("User name ...")
            user_name = input()

            print("Password ...")
            user_password = input()

            # Create and save new user
            save_users( create_user( user_name, user_password) )

            print("\n")
            print(f"{user_name} welcome to Password Locker")
            print("\n")

        elif short_code == 'du':

            if display_users():
                print("\n")
                print("Here are the current users of Password Locker")
                print("-"*10)

                for user in display_users():
                    print(f"{user.user_name}")
                    print("-"*10)
            else:
                print("\n")
                print("Password Locker has no current user.\n    Be the first user :)")
                print("\n")

        elif short_code == 'lg':

            print("\n")
            print("Log into Password Locker Account")
            print("Enter the user name")
            user_name = input()

            print("Enter the password")
            user_password = input()

            if user_log_in(user_name,user_password) == None:
                print("\n")
                print("Please try again or create an account")
                print("\n")

            else:

                user_log_in(user_name,user_password)
                print("\n")
                print(f'''{user_name} welcome to your Credentials\n
                Use these short codes to get around''')

                while True:

                    print('''  Short codes:
                    cc - ADD A CREDENTIAL\n
                    dc - DISPLAY CREDENTIALS \n
                    cg - CREATE CREDENTIAL & LET THE SYSTEM GENERATE A PASSWORD FOR YOU \n
                    ex - EXIT CREDENTIAL''')

                    # Get short code from the user
                    short_code = input().lower()

                    if short_code == 'cc':
                        print("\n")
                        print("New Credential")
                        print("-"*10)

                        print("Name of the credential ...")
                        credential_name = input()

                        print("Password of the credential ...")
                        credential_password = input()

                        # Create and save new user
                        save_credentials( create_credentail( user_password, credential_name, credential_password) )

                        print("\n")
                        print(f"Credentials for {credential_name} have been created and saved")
                        print("\n")

                    elif short_code == 'dc':
                        if display_credentials(user_password):
                            print("\n")
                            print(f"{user_name}\'s credentials")
                            print("-"*10)

                            for credential in display_credentials(user_password):
                                print(f"Account ..... {credential.credential_name}")
                                print(f"Password .... {credential.credential_password}")
                                print("-"*10)

                        else:
                            print("\n")
                            print("You have no credentials")
                            print("\n")

                    elif short_code == 'cg':
                        print("\n")
                        print("New Credential")
                        print("-"*10)

                        print("Name of the credential ...")
                        credential_name = input()

                        # Save new credential with its generated password
                        save_credentials( Credential(user_password, credential_name, (create_generated_password(credential_name)) ) )
                        print("\n")
                        print(f"Credentials for {credential_name} have been created and saved")
                        print("\n")

                    elif short_code == 'ex':
                        print(f"See you later {user_name}")
                        print("\n")
                        break

                    else:
                        print("\n")
                        print(f'''{short_code} does not compute.
                        Please use the short codes''')
                        print("\n")

        elif short_code == 'ex':
            print("\n")
            print("Bye .....")

            break

        else:
            print("\n")
            print(f'''Come again, what's {short_code}?
            Please use the short codes''')
            print("\n")

if __name__ == '__main__':
    main()
