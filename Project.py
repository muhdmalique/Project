import shelve
import uuid


class Expenses:
    def __init__(self, table):
        self.__expense_type = ['Food', 'Bills', 'Shopping']
        self.__amount = ''
        self.__name = ''
        self.__table = table

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name