"""Test module for validator"""
import unittest
from microsoft_fixed import Validator

class TestValidator(unittest.TestCase):
    def setUp(self):
        self.valid = Validator()

    def test_validate_name_surname(self):
        self.assertTrue(self.valid.validate_name_surname("John Doe"))
        self.assertFalse(self.valid.validate_name_surname("JohnDoe"))
        self.assertFalse(self.valid.validate_name_surname("John Doe Smith"))
        self.assertFalse(self.valid.validate_name_surname("john Doe"))
        self.assertFalse(self.valid.validate_name_surname("John doe"))
        self.assertFalse(self.valid.validate_name_surname("John DOe"))
        self.assertFalse(self.valid.validate_name_surname("John Doe" + "q"*31))
        self.assertFalse(self.valid.validate_name_surname("John D"))
        self.assertFalse(self.valid.validate_name_surname("John D,oe"))
        self.assertFalse(self.valid.validate_name_surname("Joh1n Doe"))

    def test_validate_age(self):
        self.assertTrue(self.valid.validate_age("25"))
        self.assertFalse(self.valid.validate_age("10"))
        self.assertFalse(self.valid.validate_age("101"))
        self.assertFalse(self.valid.validate_age("25."))
        self.assertFalse(self.valid.validate_age("25a"))

    def test_validate_country(self):
        self.assertTrue(self.valid.validate_country("Canada"))
        self.assertFalse(self.valid.validate_country("C"))
        self.assertFalse(self.valid.validate_country("C"*21))
        self.assertFalse(self.valid.validate_country("Canada1"))
        self.assertFalse(self.valid.validate_country("canada"))
        self.assertTrue(self.valid.validate_country("UK"))

    def test_validate_region(self):
        self.assertTrue(self.valid.validate_region("Ontario"))
        self.assertTrue(self.valid.validate_region("Ontario1"))
        self.assertFalse(self.valid.validate_region("O"))
        self.assertFalse(self.valid.validate_region("ontario"))

    def test_validate_living_place(self):
        self.assertTrue(self.valid.validate_living_place("Main st. 1a"))
        self.assertFalse(self.valid.validate_living_place("main st. 1a"))
        self.assertFalse(self.valid.validate_living_place("Main lane 1a"))
        self.assertFalse(self.valid.validate_living_place("Main st. 1"))
        self.assertFalse(self.valid.validate_living_place("Main st. a1"))
        self.assertTrue(self.valid.validate_living_place("Main st. 11"))

    def test_validate_index(self):
        self.assertTrue(self.valid.validate_index("12345"))
        self.assertFalse(self.valid.validate_index("1234"))
        self.assertFalse(self.valid.validate_index("123456"))
        self.assertFalse(self.valid.validate_index("1234q"))
        self.assertFalse(self.valid.validate_index("123 45"))

    def test_validate_phone(self):
        self.assertTrue(self.valid.validate_phone("+14161234567"))
        self.assertFalse(self.valid.validate_phone("1 (416) 123-45-67"))
        self.assertFalse(self.valid.validate_phone("14161234567"))
        self.assertFalse(self.valid.validate_phone("-14161234567"))
        self.assertTrue(self.valid.validate_phone("+1416123456"))

    def test_validate_email(self):
        self.assertTrue(self.valid.validate_email("user.name@domain.com"))
        self.assertTrue(self.valid.validate_email("user-name@domain.com"))
        self.assertTrue(self.valid.validate_email("username@ucu.edu.net"))
        self.assertFalse(self.valid.validate_email("username@domaincom"))
        self.assertFalse(self.valid.validate_email("username@domain.abc"))
        self.assertFalse(self.valid.validate_email("username@aaa"))
        self.assertFalse(self.valid.validate_email("username@.com"))
        self.assertFalse(self.valid.validate_email("@domain.com"))
        self.assertTrue(self.valid.validate_email("my_str=and$e.em/ai{l@ukr.net"))

    def test_validate_id(self):
        self.assertFalse(self.valid.validate_id("123456"))
        self.assertFalse(self.valid.validate_id("123006"))
        self.assertFalse(self.valid.validate_id("1230916"))
        self.assertFalse(self.valid.validate_id("12306"))

    def test_validate(self):
        self.assertTrue(self.valid.validate("John Doe,25,Canada,Ontario,Main st. 1a,12345,+14161234567,user.name@domain.com,123045"))
        self.assertTrue(self.valid.validate("John Doe;25;Canada;Ontario;Main st. 1a;12345;+14161234567;user.name@domain.com;123045"))
        self.assertTrue(self.valid.validate("John Doe; 25; Canada; Ontario; Main st. 1a; 12345; +14161234567; user.name@domain.com; 123045"))
        self.assertTrue(self.valid.validate("John Doe, 25, Canada, Ontario, Main st. 1a, 12345, +14161234567, user.name@domain.com, 123045"))
