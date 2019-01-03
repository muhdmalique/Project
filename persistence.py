# import place here
import sqlite3
  # (random id generator)
import smtplib
# class and stuff


class User:
    def __init__(self, id, username, email, password):
        self.__id = id
        self.__username = username
        self.__email = email
        self.__password = password

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


conn = sqlite3.connect('user.db')

c = conn.cursor()

  #  c.execute("""CREATE TABLE user (
   #             id text,
    #            username text,
      #          email text,
       #         password text
      #          )""")

# emp_1 = Employee('John', 'Doe', 50000)
# emp_2 = Employee('Jane', 'Doe', 90000)


def create_user(id, username, email, password):
    emp_1 = User(id, username, email, password)
    c.execute("INSERT INTO user VALUES(?, ?, ?, ?)", (emp_1.get_id(), emp_1.get_username(), emp_1.get_email(), emp_1.get_password()))
    conn.commit()


def get_user(username, password):
    g = c.execute("SELECT * FROM user WHERE username=? AND password=?", (username, password))
    conn.commit()
    if g is None:
        return None
    else:
        for row in g:
            print(row)
            if username in row[1] and password in row[3]:
                return username
        return None


    #get_all = c.fetchall()
    #for s in get_all:
        #conn.commit()
        #if s[1] == username and s[3] == password:
            #return True

#    u3 = c.execute("SELECT id, username, email, password FROM user WHERE username = '(?)',(u10)")
#    p3 = c.execute("SELECT password FROM user")
# get the id from the username and match password
# use the classes to be the variables of the insert values
# make sure use random id generator as the first column
# run the create table first then hashtag it after


def check_user(username, email):
    k = c.execute("SELECT * FROM user")
    conn.commit()
    for row in k:
        print(row)
        if row[1] == username and row[2] == email:
            return False


# after forget password send email and user got password, add a back button for user to go back


def clear_user():
    c.execute("DELETE FROM user")
    conn.commit()


def forget_passwords(email):
    d = c.execute("SELECT * FROM user")
    conn.commit()
    for row in d:
        print(row)
        if email == row[2]:
            password = row[3]
            return password
