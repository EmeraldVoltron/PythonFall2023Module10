"""
Abigail Boggs
amboggs@dmacc.edu
last Edited: 10/25/23
Unit Tests for a Class Assignment
"""


import unittest
from class_definitions.student import Student as s


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.Student = s('Boggs', 'Abby', 'CIS', 3.97)

    def tearDown(self):
        del self.Student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.Student.last_name, 'Boggs')
        self.assertEqual(self.Student.first_name, 'Abby')
        self.assertEqual(self.Student.major, 'CIS')

    def test_object_created_all_attributes(self):
        student = s('Boggs', 'Abby', 'CIS', 3.97)
        assert student.last_name == 'Boggs'
        assert student.first_name == 'Abby'
        assert student.major == 'CIS'
        assert student.gpa == 3.97

    def test_student_str(self):
        self.assertEqual(str(self.Student), 'Boggs, Abby has major CIS with gpa: 3.97')

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            student = s('123', 'Abby', 'CIS')

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            student = s('Boggs', '123', 'CIS')

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            student = s('Boggs', 'Abby', '123')

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            student = s('Boggs', 'Abby', 'CIS', 5)
        with self.assertRaises(ValueError):
            student = s('Boggs', 'Abby', 'CIS', 4.5)


if __name__ == '__main__':
    unittest.main()
    student1 = s('Boggs', 'Abby', 'CIS', 3.97)
    print(student1)
    student2 = s('Boggs', 'Sharaden', 'Nursing')
    print(student2)
    unittest.main()
