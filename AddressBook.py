"""
    AddressBook
"""

import re
import datetime
from collections import UserDict
from collections import defaultdict
from contextlib import contextmanager

### Exceptions
class NameFormatError(Exception):
    pass

class PhoneFormatError(Exception):
    pass

class BirthdayFormatError(Exception):
    pass

class EmailFormatError(Exception):
    pass

### Classes
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

class Birthday(datetime.date):
    """
    Клас для зберігання дня народження.
    Формат виводу: DD.MM.YYYY
    """
    def __str__(self):
        return f"{self.day:02}.{self.month:02}.{self.year:04}"

class Record:
    """
    Клас для зберігання інформації про контакт,
    включаючи ім'я та список телефонів.
    """
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
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
        # Якщо старий телефон існує, і якщо ми успішно додали новий
        # телефон, то тоді видаляємо старий
        if self.find_phone(old_phone) and self.add_phone(new_phone):
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
        if not re.fullmatch("[0-9]{2}\\.[0-9]{2}\\.[0-9]{4}", birthday):
            raise BirthdayFormatError
        day, month, year = birthday.split('.')
        # Strong check by creating a date object
        try:
            self.birthday = Birthday(day=int(day), month=int(month), year=int(year))
        except ValueError as exception:
            raise BirthdayFormatError from exception

    def __str__(self):
        return (f"Contact name: {self.name.value}, "
                f"phones: {'; '.join(p.value for p in self.phones)}, "
                f"birthday: {self.birthday}")

class AddressBook(UserDict):
    """
    Клас для зберігання адресної книги
    """
    def find(self, name):
        return self.data.get(name, None)

    def add_record(self, record:Record):
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


# Ловимо наші виняткoві ситуації
@contextmanager
def catch_my_exceptions(*exceptions):
    try:
        yield
    except NameFormatError:
        print("Wrong name")
    except PhoneFormatError:
        print("Wrong phone")
    except BirthdayFormatError:
        print("Wrong b-day")
    except EmailFormatError:
        print("Wrong email")


def main():
    # Створення нової адресної книги
    book = AddressBook()

    print("\nTest #1")
    with catch_my_exceptions(Exception):
        bad_name = Name("john") # Виведення: Wrong name
        print(bad_name)

    print("\nTest #2")
    with catch_my_exceptions(Exception):
        bad_phone = Phone("333") # Виведення: Wrong phone
        print(bad_phone)

    print("\nTest #3")
    #jbond = Record("James Bond")
    jbond = Record("Jbond")
    jbond.add_phone("8765432100")
    jbond.add_phone("1111111111")
    jbond.add_phone("8765432100") # номер–дублікат -- не додаємо
    print(jbond) # Виведення: Contact name: James Bond, phones: 8765432100; 1111111111

    print("\nTest #4")
    with catch_my_exceptions(Exception):
        jbond.edit_phone("1111111111","1234") # Виведення: Wrong phone

    print("\nTest #5")
    with catch_my_exceptions(Exception):
        jbond.edit_phone("1111111111","8765432100") # Заміна на номер, який вже існує -- ігноруєм
    print(jbond) # Виведення: Contact name: James Bond, phones: 8765432100; 1111111111

    print("\nTest #6")
    with catch_my_exceptions(Exception):
        jbond.remove_phone("111") # Видалення неіснуючого номера -- ігноруєм
    print(jbond) # Виведення: Contact name: James Bond, phones: 8765432100; 1111111111

    print("\nTest #7")
    print(jbond.find_phone("5555555555")) # Виведення: None

    print("\nTest #8")
    book.add_record(jbond)
    book.add_record(jbond) # додаємо дублікат
    print(book) # друкуемо всю книгу
    # Виведення:
    # Address book:
    #         Contact name: John, phones: 5555555555; 1112223333
    #         Contact name: James Bond, phones: 8765432100; 1111111111

    print("\nTest #9")
    print(book.find("James")) # Виведення: None
    print(book.delete("James")) # видаляємо неіснуючий контакт -- Виведення: False
    print(book) # друкуемо всю книгу
    # Виведення:
    # Address book:
    #         Contact name: John, phones: 5555555555; 1112223333
    #         Contact name: James Bond, phones: 8765432100; 1111111111

    print("\nTest #10")
    jbond.add_birthday("22.12.2012")
    print(jbond)
    with catch_my_exceptions(Exception):
        jbond.add_birthday("22.22.2014")
    print(jbond)
    print(jbond.birthday)
    book.add_record(jbond)
    print(book)

    print("\nTest #11")
    jbond.add_birthday("13.03.2012")
    jane = Record("Jane")
    jane.add_phone("2323232323")
    jane.add_birthday("09.03.1914")
    book.add_record(jane)
    jane2 = Record("Janee")
    jane2.add_phone("1323232329")
    jane2.add_birthday("10.03.1914")
    book.add_record(jane2)
    jane3 = Record("Jaine")
    jane3.add_phone("9323232329")
    book.add_record(jane3)
    print(book)
    book.get_birthdays_per_week()

if __name__ == "__main__":
    main()
