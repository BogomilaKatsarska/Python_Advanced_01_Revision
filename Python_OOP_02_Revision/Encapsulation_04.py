'''
0:37:15
Encapsulation:
Packing of data and functions into a single component
Allows us to put restrictions and can prevent the accidental modification of data
Python does not have modifiers like pubic, protected, private
protected: _
pricate: __
'''


class BankAccount:
    def __init__(self, name):
        self.name = name
        self.__number_of_card = 123456789
        self.exp_date = '2021-07-15'
        self.cvv = 698


my_account = BankAccount("Bogomila")
