from collections import UserDict


class AddressBook(UserDict):
    
    def add_record(self, record):
        key = record.name.value
        self.data[key] = record
            

class Field:
    pass


class Record:
    
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        
    def add_phone(self, number):
        phone = Phone(number)
        self.phones.append(phone)
        
    def remove_phone(self, number):
        for phone in self.phones:
            if phone.number == number:
                self.phones.remove(phone)
                
    def edit_phone(self, old_number, new_number):
        for phone in self.phones:
            if phone.number == old_number:
                phone.number = new_number


class Name(Field):
    def __init__(self, value):
        self.name = value


class Phone(Field):
    def __init__(self, number):
        self.number = number

