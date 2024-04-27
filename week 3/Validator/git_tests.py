import unittest
from git_fixed import Validator

class TestValidator(unittest.TestCase):
    def setUp(self):
        self.valid = Validator()

    def test_validate_name_surname(self):
        self.assertTrue(self.valid.validate_name_surname("Marilyn Monroe"))
        self.assertFalse(self.valid.validate_name_surname("MarilynMonroe"))
        self.assertFalse(self.valid.validate_name_surname("Marilyn Monroe forever"))
        self.assertFalse(self.valid.validate_name_surname("marilyn Monroe"))
        self.assertFalse(self.valid.validate_name_surname("Marilyn monroe"))
        self.assertFalse(self.valid.validate_name_surname("Marilyn MOroe"))
        self.assertFalse(self.valid.validate_name_surname("Marilyn Monroe" + "q"*31))
        self.assertFalse(self.valid.validate_name_surname("Marilyn M"))
        self.assertFalse(self.valid.validate_name_surname("Marilyn M,onroe"))
        self.assertFalse(self.valid.validate_name_surname("Mar1lyn Monroe"))

    def test_validate_age(self):
        self.assertTrue(self.valid.validate_age("30"))
        self.assertFalse(self.valid.validate_age("15"))
        self.assertFalse(self.valid.validate_age("100"))
        self.assertFalse(self.valid.validate_age("30."))
        self.assertFalse(self.valid.validate_age("30a"))

    def test_validate_country(self):
        self.assertTrue(self.valid.validate_country("Germany"))
        self.assertFalse(self.valid.validate_country("G"))
        self.assertFalse(self.valid.validate_country("G"*21))
        self.assertFalse(self.valid.validate_country("Germany1"))
        self.assertFalse(self.valid.validate_country("germany"))
        self.assertTrue(self.valid.validate_country("FR"))

    def test_validate_region(self):
        self.assertTrue(self.valid.validate_region("Bavaria"))
        self.assertTrue(self.valid.validate_region("Bavaria1"))
        self.assertFalse(self.valid.validate_region("B"))
        self.assertFalse(self.valid.validate_region("bavaria"))

    def test_validate_living_place(self):
        self.assertTrue(self.valid.validate_living_place("Broadway av. 3b"))
        self.assertFalse(self.valid.validate_living_place("broadway av. 3b"))
        self.assertFalse(self.valid.validate_living_place("Broadway lane 3b"))
        self.assertFalse(self.valid.validate_living_place("Broadway av. 3"))
        self.assertFalse(self.valid.validate_living_place("Broadway av. b3"))
        self.assertTrue(self.valid.validate_living_place("Broadway av. 33"))

    def test_validate_index(self):
        self.assertTrue(self.valid.validate_index("54321"))
        self.assertFalse(self.valid.validate_index("5432"))
        self.assertFalse(self.valid.validate_index("543210"))
        self.assertFalse(self.valid.validate_index("5432q"))
        self.assertFalse(self.valid.validate_index("543 21"))

    def test_validate_phone(self):
        self.assertTrue(self.valid.validate_phone("+491712345678"))
        self.assertTrue(self.valid.validate_phone("+49 (171) 123-45-67"))
        self.assertFalse(self.valid.validate_phone("49 (171) 123-45-67"))
        self.assertFalse(self.valid.validate_phone("491712345678"))
        self.assertFalse(self.valid.validate_phone("-491712345678"))
        self.assertFalse(self.valid.validate_phone("+4917123456789"))
        self.assertTrue(self.valid.validate_phone("+49171234567"))

    def test_validate_email(self):
        self.assertTrue(self.valid.validate_email("user.name@domain.com"))
        self.assertTrue(self.valid.validate_email("user-name@domain.org"))
        self.assertTrue(self.valid.validate_email("username@ucu.edu.net"))
        self.assertFalse(self.valid.validate_email("username@domaincom"))
        self.assertFalse(self.valid.validate_email("username@domain.abc"))
        self.assertFalse(self.valid.validate_email("username@aaa"))
        self.assertFalse(self.valid.validate_email("username@.com"))
        self.assertFalse(self.valid.validate_email("@domain.com"))
        self.assertTrue(self.valid.validate_email("my_str=and$e.em/ai{l@ukr.net"))

    def test_validate_id(self):
        # self.assertTrue(self.valid.validate_id("123040"))
        # self.assertTrue(self.valid.validate_id("011110"))
        self.assertTrue(self.valid.validate_id("123056"))
        self.assertFalse(self.valid.validate_id("123456"))
        self.assertFalse(self.valid.validate_id("123006"))
        self.assertFalse(self.valid.validate_id("1230916"))
        self.assertFalse(self.valid.validate_id("12306"))

    def test_validate(self):
        self.assertTrue(self.valid.validate("Marilyn Monroe,30,Germany,Bavaria,Broadway av. 3b,54321,+491712345678,user.name@domain.com,123056"))
        self.assertTrue(self.valid.validate("Marilyn Monroe;30;Germany;Bavaria;Broadway av. 3b;54321;+491712345678;user.name@domain.com;123056"))
        self.assertTrue(self.valid.validate("Marilyn Monroe; 30; Germany; Bavaria; Broadway av. 3b; 54321; +491712345678; user.name@domain.com; 123056"))
        self.assertTrue(self.valid.validate("Marilyn Monroe, 30, Germany, Bavaria, Broadway av. 3b, 54321, +491712345678, user.name@domain.com, 123056"))

if __name__ == '__main__':
    unittest.main()
