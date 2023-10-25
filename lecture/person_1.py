

class Person:
    """Person class"""

    def __init__(self, lname, fname, addy=''):
        self.last_name = lname
        self.first_name = fname
        self.address = addy


    def __str__(self):
        if self.address == '':
            return 'Person with last name ' + str(self.last_name) + ', first name ' + str(self.first_name)
        else:
            return 'Person with last name ' + str(self.last_name) + ', first name ' + str(self.first_name) + ' ' + str(self.address)


if __name__ == '__main__':
    person1 = Person("Duck", "Donald", "123 Fake Street \n Urban, Iowa")
    print(str(person1))

    person2 = Person("Duck", "Donald")
    print(str(person2))