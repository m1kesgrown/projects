from collections import UserDict
from datetime import datetime


class AddressBook(UserDict):
    def add_record(self, record):
        key = record.name.get_value()
        self.data[key] = record

    def __iter__(self):
        return self.iterator()

    def iterator(self, n=5):
        records = list(self.data.values())
        total_records = len(records)
        current_index = 0
        while current_index < total_records:
            yield records[current_index:current_index+n]
            current_index += n


class Field:
    def __init__(self, value):
        self._value = None
        self.set_value(value)

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value


class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday) if birthday else None

    def add_phone(self, number):
        phone = Phone(number)
        self.phones.append(phone)

    def remove_phone(self, number):
        for phone in self.phones:
            if phone.get_value() == number:
                self.phones.remove(phone)

    def edit_phone(self, old_number, new_number):
        for phone in self.phones:
            if phone.get_value() == old_number:
                phone.set_value(new_number)

    def days_to_birthday(self):
        if self.birthday:
            return self.birthday.days_to_birthday()
        return None


class Name(Field):
    def __init__(self, value):
        self.set_value(value)


class Phone(Field):
    def set_value(self, value):
        if not self._is_valid_phone(value):
            raise ValueError('Invalid phone number')
        self._value = value

    def _is_valid_phone(self, value):
        return len(value) >= 5 and len(value) <= 10


class Birthday(Field):
    def set_value(self, value):
        if not self._is_valid_birthday(value):
            raise ValueError('Invalid birthday format')
        self._value = value

    def _is_valid_birthday(self, value):
        try:
            datetime.strptime(value, '%d-%m-%Y')
            return True
        except ValueError:
            return False

    def days_to_birthday(self):
        today = datetime.now().date()
        next_birthday = datetime(self._value.day, self._value.month, today.year).date()
        if next_birthday < today:
            next_birthday = datetime(self._value.day, self._value.month, today.year + 1).date()
        days_left = (next_birthday - today).days
        return days_left
