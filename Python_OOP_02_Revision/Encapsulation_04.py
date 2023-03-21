'''
Encapsulation:

Packing of data and functions into a single component
Allows us to put restrictions and can prevent the accidental modification of data
Python does not have modifiers like public, protected, private
protected: _
private: __

-getters/== property decorator/ and setters
- getattr() - used to access the attribute of an object
- hasattr() - checks if an attribute exists or not
- setattr() - used to set the value of the attribute
- delattr() - deletes an attribute from the object
'''


class BankAccount:
    def __init__(self, name):
        self.name = name
        self.__number_of_card = 123456789
        self.exp_date = '2021-07-15'
        self.cvv = 698


my_account = BankAccount("Bogomila")


class User:
    def __init__(self, name, is_admin):
        self.name = name
        self.is_admin = True


class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age

    # def info(self, user):
    #     if user.is_admin:
    #         return self.__age
    #
    # def get_age(self):
    #     print(self.__age)
    #
    # def set_age(self, age):
    #     if age < 0:
    #         raise ValueError("Invalid age")
    #     self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 18:
            self.__age = 18
        else:
            self.__age = value

# super_admin = User('Admin', True)
# person = Person('Az', 30)
# person.info(super_admin)


class NewUser:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if 15 < len(value) < 5:
            raise ValueError('The username must be between 5 and 15 characters.')
        self.__username = value


    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if self.is_length_valid(value) and self.contains_uppercase(value) and self.contains_number(value):
            self.__password = value
            return #използваме return, за да излезем
        raise ValueError('The password must be 8 or more characters with at least 1 digit and 1 upper letter.')


    def is_length_valid(self, password):
        return  len(password) >= 8


    def contains_uppercase(self, password):
        upper_letters = [char for char in password if char.isupper()]
        return True if upper_letters else False


    def contains_number(self, password):
        numbers_password = [digit for digit in password if digit.isdigit()]
        return True if numbers_password else False


    def __str___(self):
        return f'You have a profile with username: "{self.username}" and password: "{len(self.password)*"*"}"'

az = NewUser('Bogomila', '324Hawer')
print(az.__str___())
print(getattr(az, 'password', None))

