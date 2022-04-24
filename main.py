#!/usr/bin/env python3.10


from user import User
from credentials import Cred
import random


def create_user(username, password):
    new_user = User(username, password)
    return new_user


def save_user(user):
    user.save_user()


def create_cred(account, account_username, account_pasword):
    new_cred = Cred(account, account_username, account_pasword)
    return new_cred


def save_cred(credentials):
    credentials.save_cred()


# def del_cred(credentials):
#     credentials.delete_cred()


# def display_cred():
#     return Cred.display_cred()


# def find_cred(account):
#     return Cred.find_cred(account)


# def check_existing_cred(account):
#     return Cred.accounts_list(account)


# chars = 'abcdefghijklmnoprstuvwyzABCDEFGHIKLMNOPRSTUVWYZ1234567890~`!@#$%^&*()?/[]'


# def main():
#     print("Hello! I hope you've been good. \n Welcome to your Password Locker. \n Please Enter your details below:")

#     print('\n')
#     print('user Name:')
#     username = input()

#     while True:
#         print('use short code: \n mp - enter your own password, gp - generate a password')
#         short_code = input().lower()
#         if short_code == 'mp':
#             print('Password:')
#             password = input()

#         elif short_code == 'gp':
#             # passwordGen.chars
#             while True:
#                 password_len = int(
#                     input('password length:'))
#                 password = ''
#                 for x in range(0, password_len):
#                     password_char = random.choice(chars)
#                     password = password + password_char

#                 print('Hello here is your password:', password)
#                 break
#             print('Password:')
#             password = input()

#         break

#     print(f'Hi {username}!, What would you like to do?')
#     print('\n')

#     while True:
#         print('Use these short: \n ca -create credentials account, dc - display credentials, fc - find credentials, dac- delete account credentials')

#         short_code = input().lower()

#         if short_code == 'ca':
#             print('New Account')
#             print('-'*10)

#             print('Account...')
#             account = input()

#             print('Username...')
#             account_name = input()

#             while True:
#                 print(
#                     'use short code: \n mp - enter your own password, gp - generate a password')
#                 short_code = input().lower()
#                 if short_code == 'mp':
#                     print('Password:')
#                     account_password = input()

#                 elif short_code == 'gp':
#                     # passwordGen.chars
#                     while True:
#                         password_len = int(
#                             input('password length:'))
#                         password = ''
#                         for x in range(0, password_len):
#                             password_char = random.choice(chars)
#                             password = password + password_char

#                         print('Hello here is your password:', password)
#                         break
#                     print('Password:')
#                     account_password = input()

#                 break
#             save_cred(create_cred(account, account_name, account_password))
#             print('\n')
#             print(f'')

#         # elif short_code == 'dc':
#         #     if display_cred():
#         #         print('Here is a list of your accounts.')
#         #         print('\n')
#         #         for cred in display_cred():
#         #             print(
#         #                 f'{} {} {}')


# if __name__ == '__main__':
#     main()
