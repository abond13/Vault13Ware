"""
    AddressBook
"""

import re
import datetime
from collections import UserDict
from collections import defaultdict                     # I don't understand, why it's here. If not needed, we should delete this
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
    
    def __repr__(self):
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
        return f"{datetime.datetime(self.year, self.month, self.day).strftime("%d %B, %Y")}"
    
    def __repr__(self):
        return f"{datetime.datetime(self.year, self.month, self.day).strftime("%d %B, %Y")}"
    
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

    def add_birthday(self, birthday_str):
        # Quick naїve check of date format
        if not re.fullmatch("[0-9]{2}\\.[0-9]{2}\\.[0-9]{4}", birthday_str):
            raise BirthdayFormatError
        # Strong check by creating a date object
        try:
            self.birthday = Birthday(birthday_str)
        except ValueError as exception:
            raise BirthdayFormatError from exception

    def __str__(self):
        return (f"Contact name: {self.name.value}, "
                f"phones: {'; '.join(p.value for p in self.phones)}, "
                f"birthday: {self.birthday}")
    
    def __repr__(self):
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

    def get_birthdays_per_week(self, quantity: int):
        """
        Функція get_birthdays_per_week шукає в усіх записах атрибут birthday 
        i виводить імена іменинників
            з днями народження на тиждень вперед від поточного дня,
            Користувачів, у яких день народження був на вихідних, потрібно привітати в понеділок.
            
            у форматі:
            Monday: Bill Goots, Foo Bar
            Friday: John Smith
        """
    
    def get_birthdays(self, quantity: int):
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
                print(f"{key_inner}: {", ".join([name.value for name in name_list])}")
            print()

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
    
    michael = Record("Michael")
    michael.add_birthday("13.03.2016")
    book.add_record(michael)
    
    jane = Record("Jane")
    jane.add_birthday("18.03.2016")
    book.add_record(jane)
    
    oscar = Record("Oscar")
    oscar.add_birthday("15.03.2016")
    book.add_record(oscar)
    
    volodymyr = Record("Volodymyr")
    volodymyr.add_birthday("15.05.2016")
    book.add_record(volodymyr)
    
    stasy = Record("Stacy")
    stasy.add_birthday("10.04.2016")
    book.add_record(stasy)

    melissa = Record("Melissa")
    melissa.add_birthday("20.03.2016")
    book.add_record(melissa)

    angela = Record("Angela")
    angela.add_birthday("19.03.2016")
    book.add_record(angela)

    jane = Record("Jane")
    jane.add_phone("2323232323")
    jane.add_birthday("16.03.1914")
    book.add_record(jane)
    
    jane2 = Record("Janee")
    jane2.add_phone("1323232329")
    jane2.add_birthday("15.03.1914")
    book.add_record(jane2)
    
    jane3 = Record("Jaine")
    jane3.add_phone("9323232329")
    book.add_record(jane3)
    
    jane4 = Record("Janet")
    jane4.add_phone("9323232329")
    jane4.add_birthday("10.04.1914")
    book.add_record(jane4)
    
    print(book)
    book.get_birthdays(60)

if __name__ == "__main__":
    main()
