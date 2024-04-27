"""Check validate registration"""

import re

class Validator:
    """Validation"""
    def validate_name_surname(self, name_surname: str):
        """Check name and surname"""
        pattern = re.compile(r'^[A-Z][a-z]+\s[A-Z][a-z]{2,30}+$')
        return bool(re.search(pattern, name_surname))

    def validate_age(self, age: str):
        """Check age between 16 and 99"""
        pattern = re.compile(r'[1-9][0-9]$')
        return bool(re.search(pattern, age))

    def validate_country(self, country: str):
        """Check country 2-10 characters without digits"""
        pattern = re.compile(r'^[A-Z][a-zA-Z]{0,10}\D$')
        return bool(re.search(pattern, country))

    def validate_region(self, region: str):
        """Check region same as country but with digits"""
        pattern = re.compile(r'^[A-Z][a-z0-9]{1,10}$')
        return bool(re.search(pattern, region))

    def validate_living_place(self, living_place: str):
        """Check street in Koselnytska st. 2a format"""
        pattern = re.compile(r'Koselnytska (st|av|prosp|rd). [0-9][a-z0-9]')
        return bool(re.search(pattern, living_place))

    def validate_index(self, index: str):
        """Check index with exactly 5 digits"""
        pattern = re.compile(r'^\d{5}$')
        return bool(re.search(pattern, index))

    def validate_phone(self, phone: str):
        """Check phone number"""
        pattern = re.compile(r'^\+\d{9,12}$|^\+\d{2}\s?\(\d{3}\)\s?\d{3}-\d{2}-\d{2}$')
        return bool(re.search(pattern, phone))

    def validate_email(self, email: str):
        """Check the email"""
        pattern = re.compile(r'^[a-zA-Z0-9!#$%&\'*+\-=?^_`{|}~]+(\.[a-zA-Z0-9!#$%&\'*+\-=?^_`{|}~]+)*@[a-z]+(\.[a-z]+)*(com|org|edu|gov|net|ua)$')
        return bool(re.search(pattern, email))

    def validate_id(self, id: str):
        """Check id with 6 digits where one is 0"""
        pattern = re.compile(r'^([1-9]*0[1-9]*)\d{6}$|^0[1-9]{5}$|^[1-9]{5}0$')
        return bool(re.search(pattern, id))

    def validate(self, data: str):
        """Check the whole string"""
        if ';' in data and '; ' not in data:
            values = data.split(';')
        elif '; ' in data:
            values = data.split('; ')
        elif ',' in data and ', ' not in data:
            values = data.split(',')
        elif ', ' in data:
            values = data.split(', ')
            return all(Validator().validate_name_surname(values[0]), \
Validator().validate_age(values[1]), Validator().validate_country(values[2]), Validator().validate_region(values[3]),\
Validator().validate_living_place(values[4]), Validator().validate_index(values[5]), Validator().validate_phone(values[6]),\
Validator().validate_email(values[7]), Validator().validate_id(values[8]))
