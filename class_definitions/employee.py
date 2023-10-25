"""
Abigail Boggs
amboggs@dmacc.edu
Last Edited: 10/25/2023
Encapsulation Assignment
"""

import datetime


class Employee:
    """Employee Class"""
    def __init__(self, lname, fname, phone_num, start_date, salary, salaried=False, addy=''):
        self._last_name = lname
        self._first_name = fname
        self._phone_number = phone_num
        self._salaried = salaried
        self._start_date = start_date
        self._salary = salary
        self._address = addy

    def __str__(self):
        return (f"{self._first_name}, {self._last_name}, {self._phone_number}, {self._salaried}, {self._start_date}, "
                f"{self._salary}, {self._address}")

    def __repr__(self):
        return ("Employee(\"" + self._first_name + "\", \"" + self._last_name + "\", \"" + self._phone_number + "\", \""
                + str(self._salaried) + "\", \"" + str(self._start_date) + "\", \"" + str(self._salary) + "\", \"" +
                str(self._address) + ")")


    def display(self):
        if self._salaried is False:
            return (f"{self._first_name} {self._last_name} \n{self._address} \nHourly employee: ${self._salary}/hour "
                    f" \nStart Date: {self._start_date}")
        else:
            return (f"{self._first_name} {self._last_name} \n{self._address} \nSalary employee: ${self._salary}/year "
                    f" \nStart Date: {self._start_date}")


if __name__ == '__main__':
    employee1 = Employee('Sarah', 'Patel', '123-456-7890',
                         datetime.date(2019, 6, 28), 40000.00, True, '123 Main Street \nUrban, Iowa')
    employee2 = Employee('Sarah', 'Patel', '123-456-7890',
                         datetime.date(2019, 6, 28), 7.25, False, '123 Main Street \nUrban, Iowa')

    print(employee1.display())
    print()
    print(employee2.display())
