import re
import datetime
from collections import UserDict
from collections import defaultdict


# Exceptions
class NameFormatError(Exception):
    pass


class PhoneFormatError(Exception):
    pass


class BirthdayFormatError(Exception):
    pass


class EmailFormatError(Exception):
    pass

class AddressFormatError(Exception):
    pass


class DictSortable(UserDict):
    def sort_keys(self) -> dict:
        """
        Sort the dictionary through key values (int or datetime, for example)
        """
        sorted_dict = {}
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            sorted_dict[key] = self.data[key]
        return sorted_dict

class Field:
    """
    Базовий клас для полів запису.
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    """
    Клас для зберігання імені контакту.
    Імʼя має задоволняти наступним вимогам:
            1. Довжина повинна бути 2+ символів.
            2. Перша літера велика.
                Наприклад: Al
    """
    def __init__(self, name):
        if not re.fullmatch("[A-Z][a-z]+", name):
            raise NameFormatError
        super().__init__(name)

class Phone(Field):
    """
    Клас для зберігання номера телефону.
    Телефон має задоволняти наступним вимогам:
        1. Складається з цифр.
        2. Довжина повинна бути 10 символів.
    """
    def __init__(self, phone):
        if not re.fullmatch("[0-9]{10}", phone):
            raise PhoneFormatError
        super().__init__(phone)

class Birthday(Field):
    """
    Клас для зберігання дня народження.
    Формат виводу: DD.MM.YYYY
    """
    def __init__(self, value):
        super().__init__(value)
        day, month, year = self.value.split('.')
        self.day, self.month, self.year = int(day), int(month), int(year)
        
        try:
            datetime.date(self.year, self.month, self.day)
        except ValueError:
            raise ValueError("Incorrect date format, should be DD.MM.YYYY")
        
    def __str__(self):
        return f"{datetime.datetime(self.year, self.month, self.day).strftime('%d %B, %Y')}"
    
    def __repr__(self):
        return f"{datetime.datetime(self.year, self.month, self.day).strftime('%d %B, %Y')}"

class Email(Field):
    """
    Клас для зберігання email.
    Email має задоволняти формату login@subdomen.domen:
    """
    def __init__(self, email):
        if not re.fullmatch(r".+@.+\..+", email):
            raise EmailFormatError
        super().__init__(email)

class Address(Field):
    """
    Клас для зберігання адреси контакту.
    Імʼя має задоволняти наступним вимогам:
            1. Довжина повинна бути 2+ символів.
    """
    def __init__(self, name):
        if not re.fullmatch(r"^.{3,}", name):
            raise NameFormatError
        super().__init__(name)

class Record:
    """
    Клас для зберігання інформації про контакт,
    включаючи ім'я, список телефонів, список Emails, адресу, день народження
    """
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.emails = []
        self.address = None
        self.birthday = None

    def add_phone(self, phone):
        # Додаємо лише унікальний телефон
        if self.find_phone_record(phone) is None:
            self.phones.append(Phone(phone))
            return True
        return False

    def remove_phone(self, phone):
        record = self.find_phone_record(phone)
        if record:
            self.phones.remove(record)
            return True
        return False

    def edit_phone(self, old_phone, new_phone):
        # Якщо старий телефон існує, і якщо ми успішно додали новий, та якщо старий та новий не співпадають
        # телефон, то тоді видаляємо старий
        if self.find_phone(old_phone) and self.add_phone(new_phone) and (self.find_phone(old_phone) != self.add_phone(new_phone)):
            self.remove_phone(old_phone)
            return True
        return False

    def find_phone(self, phone):
        record = self.find_phone_record(phone)
        if record:
            return self.find_phone_record(phone).value
        return None

    def find_phone_record(self, phone):
        # Так як номер унікальний (див. add_phone()),
        # то виходимо відразу, якщо його знайшли.
        for record in self.phones:
            if record.value == phone:
                return record
        return None

    def add_birthday(self, birthday):
        # Quick naїve check of date format
        if not re.fullmatch(r'\b(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(19\d\d|20\d\d)\b', birthday):
            raise BirthdayFormatError
        day, month, year = birthday.split('.')
        # Strong check by creating a date object
        try:
            self.birthday = Birthday(birthday)
        except ValueError as exception:
            raise BirthdayFormatError from exception
    def __str__(self):
        return (f"Contact name: {self.name.value}, \n"
                f"phones: {'; '.join(p.value for p in self.phones)}, \n"
                f"emails: {'; '.join(e.value for e in self.emails)}, \n"
                f"address: {self.address}, \n"
                f"birthday: {self.birthday}\n")


class AddressBook(UserDict):
    """
    Клас для зберігання адресної книги
    """
    def find(self, name):
        return self.data.get(name, None)

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def delete(self, name):
        if self.data.pop(name, None):
            return True
        return False

    def load(self):
        """
        Load configuration from YAML file
        """

    def save(self):
        """
        Save configuration to YAML file
        """

    def get_birthdays(self, quantity: int):
        """
        Функція get_birthdays_per_week шукає в усіх записах атрибут birthday
        i виводить імена іменинників
            з днями народження на тиждень вперед від поточного дня,
            Користувачів, у яких день народження був на вихідних, потрібно привітати в понеділок.

            у форматі:
            Monday: Bill Goots, Foo Bar
            Friday: John Smith
        """
        """
        Function recieves an AddressBook object and number of days to look ahead.\n
        Prints out birthdays of contacts within the range of days.
        Returns nothing.
        """
        
        calendar = {}
        today = datetime.datetime.today().date()

        for record in self.data.values():
            if record.birthday is None:
                continue
            next_birthday = datetime.date(today.year, record.birthday.month, record.birthday.day)
            if next_birthday < today:
                next_birthday = next_birthday.replace(year=today.year + 1)
            delta_days = (next_birthday - today).days
            if delta_days >= quantity:
                continue
            else:
                
                # Going to work with the next structure: (dict of dicts)
                #
                # {
                #   'March, 2024' : { 12: ['Brandon','Olivia'], 27: ['Gregor'] }
                #   'April, 2024' : { 3: ['Viktor'], 14: ['Sofia'], 18: ['Thomas', 'Andrea', 'Magnus'] }                       
                # }

                # set keys for the outer and inner dictionaries
                key_outer = next_birthday.replace(day=1)        # This is datetime.date, but we will print out 'March, 2024'
                key_inner = next_birthday.day
                name = record.name
                
                # if there is no such key - create it!
                try:
                    calendar[key_outer]
                except KeyError:
                    calendar[key_outer] = {}
                
                    # it's time to fill in the inner dictionary:
                if len(calendar[key_outer]) == 0:
                    calendar[key_outer][key_inner] = [name] 
                else:
                    try:
                        # if there is already such cell with given month and day - append new name
                        calendar[key_outer][key_inner].append(name)
                    except KeyError:
                        # if there is no such key for inner dictionary - also create it
                        calendar[key_outer][key_inner] = [name]
        
        # Don't forget to sort our dictionaries by date
        calendar = DictSortable(calendar)
        calendar = calendar.sort_keys()
        for key_outer, inner_dict in calendar.items():
            inner_dict = DictSortable(inner_dict)
            inner_dict = inner_dict.sort_keys()
            print(key_outer.strftime("%B, %Y"))
            for key_inner, name_list in inner_dict.items():
                print(f"{key_inner}: {', '.join([name.value for name in name_list])}")
            print()

    def __str__(self):
        return 'Address book:\n\t' + '\n\t'.join(record.__str__() for record in self.data.values())

class NoteBook():
    pass

