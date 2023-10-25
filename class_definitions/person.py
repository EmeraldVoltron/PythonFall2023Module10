class Person:
    """Person class"""
    def __init__(self, lname, fname, ssn=''):         # Constructor sets all to no value
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        ssn_characters = set("1234567890-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        if ssn and not ssn_characters.issuperset(ssn):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.ssn = ssn           # Social Security Number

    def change_last_name(self, name):
        self.last_name = name

    def change_first_name(self, name):
        self.first_name = name

    def display(self):
        return self.last_name + ", " + self.first_name + ":" + self.ssn

    def __str__(self):
        return self.last_name + ", " + self.first_name + ":" + self.ssn



