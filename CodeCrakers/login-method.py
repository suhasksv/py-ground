import time
import os
import random

usernames = []
passwds = []
assigned_salt = []
user_salt = {}

def creating_user():
    # Getting username and appending it to 'usernames' list
    username = input("Enter your username:")
    usernames.append(username)

    # Getting password and appending it to 'passwds' list
    passwd = input("Enter your password:")
    passwds.append(passwd)

# Assigning salt to username and password
def salt_assign(passwd, username):
    salt = random.randrange(1, 100)
    s = str(salt) + passwd
    user_salt[username] = salt
    return s


# def get_salt_user(username):
#     if username in usernames:
