import unittest
from class_definitions.person import Person as t


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.Person = t('Duck', 'Daisy')

    def tearDown(self):
        del self.Person

    def test_initial_value_required_attributes(self):
        self.assertEqual(self.Person.last_name, 'Duck')
        self.assertEqual(self.Person.first_name, 'Daisy')

    def test_initial_all_attributes(self):
        person = t('Duck', 'Daisy', '111-11-1111')
        assert person.last_name == 'Duck'
        assert person.first_name == 'Daisy'
        assert person.ssn == '111-11-1111'

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            p = t('123', 'Daisy')

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            p = t('Duck', '123')

    def test_object_not_created_error_ssn(self):
        with self.assertRaises(ValueError):
            p = t('Duck', 'Daisy', 'abc')

    def test_person_class_display_name(self):
        self.assertEqual(str(self.Person), 'Duck, Daisy:')

    def test_person_class_display_name_snn(self):
        p = t('Duck', 'Daisy', '111-11-1111')
        self.assertEqual(str(p), "Duck, Daisy:111-11-1111")

    def test_person_str(self):
        self.assertEqual(str(self.Person), 'Duck, Daisy:')


# driver
if __name__ == '__main__':
    unittest.main()