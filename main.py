#!/usr/bin/env python3.10


from user import User
from credentials import Cred
import random

chars = 'abcdefghijklmnoprstuvwyzABCDEFGHIKLMNOPRSTUVWYZ1234567890~`!@#$%^&*()?/[]'


def create_user(username, password):
    '''
    function to create a new user
    '''
    new_user = User(username, password)
    return new_user


def save_user(user):
    '''
    function to save new user
    '''
    user.save_user()


def user_exist(username):
    '''
    function to check if user exists
    '''
    return User.user_exist(username)


def display_users():
    '''
    function to display users
    '''
    return User.display_users()


def create_cred(account, account_username, account_pasword):
    '''
    function to create a new credential
    '''
    new_cred = Cred(account, account_username, account_pasword)
    return new_cred


def save_cred(credentials):
    '''
    function to save credentials
    '''
    credentials.save_cred()


def del_cred(credentials):
    '''
    function to delete credentials
    '''
    credentials.delete_cred()


def find_cred(account):
    '''
    function to find credentials
    '''
    return Cred.find_cred(account)


def check_existing_cred(account):
    '''
    function to check for existing credentials
    '''
    return Cred.cred_exist(account)


def display_cred():
    '''
    function to display credentials
    '''
    return Cred.display_cred()


def main():
    print("Hello! I hope you've been good. \n Welcome to your Password Locker.")

    # short_code = input().lower()
    # if short_code == 'li':
    #     print('\n')
    #     print('user Name:')
    #     username = input()

    #     print('Password:')
    #     password = input()

    # elif short_code == 'su':
    #     print('New Account')
    #     print('-'*10)

    #     print('Username...')
    #     account = input()

    #     while True:
    #         print(
    #             'use short code: \n mp - enter your own password, gp - generate a password')
    #         short_code = input().lower()
    #         if short_code == 'mp':
    #             print('Password...')
    #             password = input()

    #         elif short_code == 'gp':

    #             while True:
    #                 password_len = int(
    #                     input('Password length:'))
    #                 password = ''
    #                 for x in range(0, password_len):
    #                     password_char = random.choice(chars)
    #                     password = password + password_char

    #                 print('\n')
    #                 print('Hello here is your password:', password)
    #                 break
    #             print('Password...')
    #             password = input()

    #         break
    #     print('\n')
    #     print('User Name:')
    #     username = input()

    #     print('Password:')
    #     password = input()

    print('Create an Account:')
    print('\n')
    print('-'*10)

    print('Username...')
    username = input()
    while True:
        print(
            'use short code: \n mp - enter your own password, gp - generate a password')
        short_code = input().lower()
        if short_code == 'mp':
            print('Password...')
            password = input()

        elif short_code == 'gp':

            while True:
                password_len = int(
                    input('Password length:'))
                password = ''
                for x in range(0, password_len):
                    password_char = random.choice(chars)
                    password = password + password_char

                print('\n')
                print('Hello here is your password:', password)
                break
            print('Password...')
            password = input()

        break
    save_user(create_user(username, password))
    print(f'Hello {username}, your account has been created successfully')

    print('\n')
    print('Now Login:')
    print('Username...')
    username = input()
    print('password...')
    password = input()
    while True:
        for user in display_users():
            if user_exist(password):
                print('\n')
                print(f'Hi {username}!, What would you like to do?')
                print('\n')

                while True:
                    print('Use these short: \n ca -create credentials account, dc - display credentials, fc - find credentials, d - delete account credentials')

                    short_code = input().lower()

                    if short_code == 'ca':
                        print('New Account')
                        print('-'*10)

                        print('Account...')
                        account = input()

                        print('Username...')
                        account_name = input()

                        while True:
                            print(
                                'use short code: \n mp - enter your own password, gp - generate a password')
                            short_code = input().lower()
                            if short_code == 'mp':
                                print('Password:')
                                account_password = input()

                            elif short_code == 'gp':

                                while True:
                                    password_len = int(
                                        input('password length:'))
                                    password = ''
                                    for x in range(0, password_len):
                                        password_char = random.choice(chars)
                                        password = password + password_char

                                    print(
                                        'Hello here is your password:', password)
                                    break
                                print('Password:')
                                account_password = input()

                            break
                        save_cred(create_cred(
                            account, account_name, account_password))
                        print('\n')
                        print(f'')

                    elif short_code == 'dc':
                        if display_cred():
                            print(
                                'Hey!! A list of your accounts and their details. ????')
                            print('\n')
                            for credentials in display_cred():
                                print(
                                    f'Account: {credentials.account}\n UserName: {credentials.account_username}\n Password: {credentials.account_password}')
                                print('\n')

                        else:
                            print('\n')
                            print(
                                'Sorry!???? You do not seem to have any account details stored yet.')

                            print('\n')

                    elif short_code == 'fc':
                        print('Please Enter Account to Search:')
                        search_account = input()
                        if check_existing_cred(search_account):
                            search_cred = find_cred(search_account)
                            print('\n')
                            print(
                                f'Yes you have {search_cred.account} in your storage.')

                        else:
                            print('Ooops!! That account does not exist!!')

                    elif short_code == 'd':
                        print('Please Enter Account to Delete:')
                        search_account = input()
                        if find_cred(search_account):
                            search_cred = find_cred(search_account)
                            search_cred.delete_cred()
                            print('\n')
                            print(
                                f'Your {search_cred.account} credentials were deleted successfully! ')
                        else:
                            print('Ooops!! That account does not exist!!')
            else:
                print('User does not exist')

        break


if __name__ == '__main__':
    main()
