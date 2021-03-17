"""
import random
import time
import getpass

print("Welcome to Quantum Tricks Accounts")
time.sleep(1.5)
print("For more information visit https://accounts.quantumtricks.in/user_support/index.html")
time.sleep(2.0)
print("Let's get started")
time.sleep(1.0)

usernames = []
# passwords = []
passwds = {}
assigned_salt = []
user_salt = {}


# Creating a user
def creating_user_sign_up():
    # Getting username and appending it to 'usernames' list

    while True:
        username = input("Enter your username:")
        if username not in usernames:
            usernames.append(username)

            # Getting password and appending it to 'passwds' list
            print("Enter your password:")
            passwd = getpass.getpass()
            # passwords.append(passwd)
            while True:
                print("Re-enter password:")
                re_passwd = getpass.getpass()
                if passwd == re_passwd:
                    # print("Your password is saved successfully...!")
                    print("Congratulations your Quantum Tricks Account has been created successfully")
                    time.sleep(1.5)
                    print("Please sign in to start working with your QT Account\n")
                    salt_assign(passwd, username)
                    ask_sign()
                    break
                print("Password is not matching please try again..!\n")
                continue
        print("Username is already taken, please try another username...\n")
        continue


# def xor_str(a, b):
#     xored = []
#     for i in range(max(len(a), len(b))):
#         xored_value = ord(a[i % len(a)]) ^ ord(b[i % len(b)])
#         xored.append(hex(xored_value)[2:])
#     return ''.join(xored)


# Assigning salt to username and password
def salt_assign(passwd, username):
    while True:
        salt = random.randrange(1, 10000)
        if salt not in assigned_salt:
            s = str(salt) + passwd
            # sa = xor_str(s, salt)
            assigned_salt.append(salt)
            user_salt[username] = salt
            # passwords.append(s)
            # passwds[username] = sa
        break


# finding salt of the user
def finding_salt_of_user(user):
    salt = user_salt[str(user)]
    return salt


# Re-encrypting entered password
def encrypt_passwd(salt, passwd):
    new_passwd = str(salt) + passwd
    # new_passw = xor_str(new_passwd, salt)
    return new_passwd


# Checking encrypted password with entered password
def password_chk(username):
    ask_passwd = input("Enter your password:")
    salt = finding_salt_of_user(username)
    passwd = encrypt_passwd(salt, ask_passwd)
    passw = passwds[username]
    if passw == passwd:
        return True
    return False


# User sign in
def user_sign_in():
    username = input("Enter your username:")
    if username in usernames:
        chk = password_chk(username)
        if chk:
            return "\nlogin success\n"
        elif chk == False:
            return "\nIncorrect Password\nLogin Failed\n"
    else:
        return "Could not find user\n"


def ask_sign():
    ask = input("Do you want to signup or signin? ").lower()
    if ask == "signup" or ask == "sign up":
        creating_user_sign_up()
    elif ask == "signin" or ask == "sign in":
        print(user_sign_in())
        ask_sign()
    else:
        ask_sign()


ask_sign()
"""
import random
import time
import getpass

print("Welcome to Quantum Tricks Accounts")
time.sleep(1.5)
print("For more information visit https://accounts.quantumtricks.in/user_support/index.html")
time.sleep(2.0)
print("Let's get started")
time.sleep(1.0)

"""
usernames = [""]
# passwords = [""]
passwds = {"": ""}
assigned_salt = [""]
user_salt = {"": ""}
"""

usernames = []
# passwords = []
passwds = {}
assigned_salt = []
user_salt = {}


# Creating a user
def creating_user_sign_up():
    # Getting username and appending it to 'usernames' list

    while True:
        username = input("Enter your username:")
        if username not in usernames:
            usernames.append(username)

            # Getting password and appending it to 'passwds' list
            print("Enter your password:")
            passwd = getpass.getpass()
            # passwords.append(passwd)
            while True:
                print("Re-enter password:")
                re_passwd = getpass.getpass()
                if passwd == re_passwd:
                    # print("Your password is saved successfully...!")
                    print("Congratulations your Quantum Tricks Account has been created successfully")
                    time.sleep(1.5)
                    print("Please sign in to start working with your QT Account\n")
                    salt_assign(passwd, username)
                    ask_sign()
                    break
                print("Password is not matching please try again..!\n")
                continue
        print("Username is already taken, please try another username...\n")
        continue


# Assigning salt to username and password
def salt_assign(passwd, username):
    while True:
        salt = random.randrange(1, 10000)
        if salt not in assigned_salt:
            s = str(salt) + passwd
            assigned_salt.append(salt)
            user_salt[username] = salt
            # passwords.append(s)
            passwds[username] = s
        break


# finding salt of the user
def finding_salt_of_user(user):
    salt = user_salt[str(user)]
    return salt


# Re-encrypting entered password
def encrypt_passwd(salt, passwd):
    new_passwd = str(salt) + passwd
    return new_passwd


# Checking encrypted password with entered password
def password_chk(username):
    ask_passwd = input("Enter your password:")
    salt = finding_salt_of_user(username)
    passwd = encrypt_passwd(salt, ask_passwd)
    passw = passwds[username]
    if passw == passwd:
        return True
    return False


# User sign in
def user_sign_in():
    username = input("Enter your username:")
    if username in usernames:
        chk = password_chk(username)
        if chk:
            return "\nlogin success\n"
        elif chk == False:
            return "\nIncorrect Password\nLogin Failed\n"
    else:
        return "Could not find user\n"


def ask_sign():
    ask = input("Do you want to signup or signin? ").lower().strip()
    if ask == "signup" or ask == "sign up":
        creating_user_sign_up()
    elif ask == "signin" or ask == "sign in":
        print(user_sign_in())
        ask_sign()
    else:
        ask_sign()


ask_sign()
