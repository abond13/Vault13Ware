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

class Birthday(datetime.date): # Why not Field? #######################
    """
    Клас для зберігання дня народження.
    Формат виводу: DD.MM.YYYY
    """
    def __str__(self):
        return f"{self.day:02}.{self.month:02}.{self.year:04}"

class Email(Field):
    """
    Клас для зберігання email.
    Email має задоволняти формату login@subdomen.domen:
    """
    def __init__(self, email):
        if not re.fullmatch(r".+@.+\..+", email):
            raise PhoneFormatError
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
    включаючи ім'я та список телефонів.
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
            self.birthday = Birthday(day=int(day), month=int(month), year=int(year))
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

    def get_birthdays_per_week(self):
        """
        Функція get_birthdays_per_week шукає в усіх записах атрибут birthday
        i виводить імена іменинників
            з днями народження на тиждень вперед від поточного дня,
            Користувачів, у яких день народження був на вихідних, потрібно привітати в понеділок.

            у форматі:
            Monday: Bill Goots, Foo Bar
            Friday: John Smith
        """
        today = datetime.datetime.today().date()
        weekday_to_name = []
        for name, record in self.data.items():
            birthday = record.birthday
            if not birthday:
                continue
            birthday_this_year = birthday.replace(year=today.year)
            if birthday_this_year < today:
                birthday_this_year = birthday.replace(year=today.year + 1)
            if birthday_this_year.weekday() == 5:
                birthday_this_year += datetime.timedelta(days=2)
            if birthday_this_year.weekday() == 6:
                birthday_this_year += datetime.timedelta(days=1)
            delta_days = (birthday_this_year - today).days
            if delta_days < 7:
                weekday_to_name.append((delta_days, birthday_this_year.strftime('%A'), name))
        weekday_to_name.sort()
        dd_list = defaultdict(list)
        for delta_days, weekday, name in weekday_to_name:
            dd_list[weekday].append(name)
        print('\n'.join([f"{day}: {', '.join(names)}" for day, names in dd_list.items()]))

    def __str__(self):
        return 'Address book:\n\t' + '\n\t'.join(record.__str__() for record in self.data.values())



class NoteBook():
    pass

