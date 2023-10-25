class PersonTitles:
    TITLES = ('Dr', 'Mr', "Mrs", "Ms")

    def __init__(self, title, name, surname, allowed_titles=TITLES):
        if title not in allowed_titles:
            raise ValueError("%s is not a valid title. " % title)

        self.title = title
        self._name = name
        self.surname = surname

    def getName(self):
        return self._name

    def setName(self, new_name):
        # validate the input...
        self._name = new_name

    def __str__(self):
        return f"{self.title} {self._name}"


if __name__ == '__main__':
    try:
        error = PersonTitles("Sir", "John", "Smith")
    except Exception as err:
        print(err)
    person = PersonTitles("Dr", "john", "Smith")
    print(person)
    person.setName("John")
    print(person)