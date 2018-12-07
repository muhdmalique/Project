# import place here
import shelve
import uuid  # (random id generator)
import smtplib
# class and stuff


class User:
    def __init__(self, id):
        self.__id = id
        self.__username = ''
        self.__email = ''
        self.__password = ''

    def get_id(self):
        return self.__id

    def get_username(self):
        return self.__username

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def set_username(self, username):
        self.__username = username

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password


users = shelve.open('user')


def create_user(username, email, password):
    id = str(uuid.uuid4())
    user = User(id)
    user.set_username(username)
    user.set_email(email)
    user.set_password(password)
    users[id] = user


def get_user(username, password):
    key_list = list(users.keys())
    for key in key_list:
        user = users[key]
        print(user.get_username(), username, user.get_password(), password)
        if user.get_username() == username and user.get_password() == password:
            return user
    return None

# after forget password send email and user got password, add a back button for user to go back


def clear_user():
    key_list = list(users.keys())
    for key in key_list:
        del users[key]


def forget_password(email):
    key_list = list(users.keys())
    for key in key_list:
        user = users[key]
        print(user.get_email, email)
        if user.get_email() == email:
            password = user.get_password
            print(password)
