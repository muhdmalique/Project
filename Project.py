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


expenses = shelve.open('expense')


def delete_table():
    e_list = list(expenses.keys())
    for key in e_list:
        del expenses[key]


def create_table(expense_type, amount, name):
    table = str(uuid.uuid4())
    expense = Expenses(table)
    expense.expense_type = expense_type
    expense.amount = amount
    expense.name = name
    expenses[table] = expense
