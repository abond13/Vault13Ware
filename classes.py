import re
import datetime
from collections import UserDict
from collections import defaultdict
import json
import tempfile
import os
from features import display


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


class NoTextError(Exception):
    pass


class NoIdEnteredError(Exception):
    pass


class NoIdFoundError(Exception):
    pass


class MinArgsQuantityError(Exception):
    pass


class NotFoundNameError(Exception):
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
    
    def __repr__(self):
        return str(self.value)


class Name(Field):
    """
    Клас для зберігання імені контакту.
    Імʼя має задоволняти наступним вимогам:
            1. Довжина повинна бути 2+ символів.
                Наприклад: Al, me, iA
    """

    def __init__(self, name):
        if not re.fullmatch("[A-Za-z]{2,}", name):
            raise NameFormatError
        super().__init__(name)


class Phone(Field):
    """
    Клас для зберігання номера телефону.
    Телефон мoжуть мати наступний вигляд:
        0671234567
        (044)4567890
        +380509876543
        +380(4565)7890001
    """

    def __init__(self, phone):
        if not re.fullmatch(r'^(\+[1-9]\d{,2})?(\(\d{1,4}\))?\d{6,15}$', phone):
            raise PhoneFormatError
        super().__init__(phone)


class Birthday(Field):
    """
    Клас для зберігання дня народження.
    Формат виводу: DD.MM.YYYY
    """

    def __init__(self, value):
        try:
            datetime.datetime.strptime(value, '%d.%m.%Y')
        except ValueError as exception:
            raise BirthdayFormatError from exception
        super().__init__(value)
        self.day, self.month, self.year = map(int, self.value.split('.'))

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
        if not re.fullmatch(r'[a-z0-9]{1,10}@[a-z0-9]{1,10}\.[a-z]{2,5}', email):
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
    
    def __repr__(self):
        return f"{self.name} Record"

    def add_phone(self, phone):
        # Додаємо лише унікальний телефон
        if self.find_phone_record(phone) is None:
            self.phones.append(Phone(phone))
            return True
        return False
    
    def change_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:    
                self.phones.remove(phone)
                self.phones.append(Phone(new_phone))
                return True
        return False

    def delete_phone(self, phone_str):
        for phone in self.phones:
            if phone.value == phone_str:    
                self.phones.remove(phone)
                return True
        return False

    def change_email(self, old_email, new_email):
        for email in self.emails:
            if email.value == old_email:    
                self.emails.remove(email)
                self.emails.append(Email(new_email))
                return True
        return False
        
    def delete_email(self, email_str):
        for email in self.emails:
            if email.value == email_str:    
                self.emails.remove(email)
                return True
        return False

    def delete_birthday(self):
        if self.birthday:
            self.birthday = None
            return True
        else:
            return False

    def delete_address(self):
        if self.address:
            self.address = None
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
        self.birthday = Birthday(birthday)

    # def find_email(self, email):
    #     for email_field in self.emails:
    #         if email_field.value == email:
    #             return email_field
    #         else:
    #             return None

    def add_email(self, email):
        if self.find_email(email) is None:
            self.emails.append(Email(email))

    def add_address(self, new_address: str):
        MAX_ADDRESS_LENGTH = 250
        self.address = Address(new_address[:MAX_ADDRESS_LENGTH])

    def __str__(self):
        return (f"Contact name: {self.name.value}, \n"
                f"    birthday: {self.birthday}, \n"
                f"      phones: {'; '.join(p.value for p in self.phones)}, \n"
                f"      emails: {'; '.join(e.value for e in self.emails)}, \n"
                f"     address: {self.address}\n")


class AddressBook(UserDict):
    """
    Клас для зберігання адресної книги
    """

    def __init__(self):
        super().__init__()
        self.filename = './.address_book.json'
        self.load(self.filename)

    def find(self, name):
        return self.data.get(name, None)

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def change_record(self, old_name: str, new_name: str):
        self.data[new_name] = self.data.pop(old_name)
        self.data[new_name].name = Name(new_name)

    def delete(self, name):
        if self.data.pop(name, None):
            return True
        return False

    def load(self, filename=None):
        """
        Зчитування данних з JSON файлу і створення записів (Record)
        для данного екземпляру AddressBook.
        Зчитування відбувається в режимі обʼєднання, але у разі
        співпадіння імен записів, записи з JSON файлу мають перевагу
        над вже існуючими записами в екземплярі AddressBook. 
        """
        if not filename:
            filename = self.filename
        try:
            with open(filename, "r", encoding="utf-8") as book_file:
                book_dict = json.load(book_file)
        except OSError:
            # Файла з записами немає, тихо виходимо
            return
        except json.JSONDecodeError:
            print(f"Address book JSON file {filename} is broken.")
            return
        for name, attrs in book_dict.items():
            try:
                record = Record(name)
                for attr, value in attrs.items():
                    if value:
                        if attr == "phones":
                            for phone in value:
                                record.add_phone(phone["value"])
                        elif attr == "emails":
                            for email in value:
                                record.add_email(email["value"])
                        elif attr == "address":
                            record.add_address(value["value"])
                        elif attr == "birthday":
                            record.add_birthday(value["value"])
                self.add_record(record)
            except (NameFormatError,
                    PhoneFormatError,
                    EmailFormatError,
                    BirthdayFormatError,
                    AddressFormatError):
                continue

    def save(self, filename=None):
        """
        Зберігання всіх записів (Record) данного екземпляра AddressBook в JSON файл.
        Додатково використовується проміжний TMP файл для запобігання
        втрати данних під час відкриття файла на запис, але без подальшого запису
        у випадку нештатної ситуації.
        """
        if not filename:
            filename = self.filename
        book_json = json.dumps(self.data, default=lambda o: o.__dict__, indent=4)
        with tempfile.NamedTemporaryFile('w', encoding="utf-8",
                                         dir='.', prefix=filename + '~', delete=False) as tf:
            tf.write(book_json)
        # Fix for Windows: os.rename can be executed when tf is closed
        try:
            if os.path.exists(filename):
                os.remove(filename)
            os.rename(tf.name, filename)
        except OSError as error:
            print(error)

    def get_birthdays(self, quantity: int):
        """
        Функція get_birthdays_per_week шукає в усіх записах атрибут birthday
        i виводить імена іменинників
            з днями народження на тиждень вперед від поточного дня,
            Користувачів, у яких день народження був на вихідних, потрібно привітати в понеділок.

            у форматі:
            Monday: Bill Goots, Foo Bar
            Friday: John Smith

        Function recieves an AddressBook object and number of days to look ahead.\n
        Prints out birthdays of contacts within the range of days.
        Returns nothing.
        """

        if quantity > 365:
            display("Are you sure you will live more than a year? Try to write some real number instead.")
            return

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
                key_outer = next_birthday.replace(day=1)  # This is datetime.date, but we will print out 'March, 2024'
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
        print()
        for key_outer, inner_dict in calendar.items():
            inner_dict = DictSortable(inner_dict)
            inner_dict = inner_dict.sort_keys()
            print_string = str(key_outer.strftime("%B, %Y"))
            display(print_string)
            for key_inner, name_list in inner_dict.items():
                print_string2 = (
                    f"{key_inner}: " + f"{', '.join([name.value for name in name_list])}"
                )
                display(print_string2)
            print()


    def __str__(self):
        return 'Address book:\n\t' + '\n\t'.join(record.__str__() for record in self.data.values())


class Note(Field):

    def __init__(self, value: str):
        super().__init__(value)
        self.title = ""
        self.body = ""
        self.tags = []
        self.id = None
        self.__extract_title_and_body()
        self.__extract_tags()

    def __extract_title_and_body(self):
        """
        Заголовок може бути лише на початку нотатки і за умови, що він виділений спеціальними символами
        """
        start_symbols = '<<'
        end_symbols = '>>'
        start_index = self.value.find(start_symbols)
        end_index = self.value.find(end_symbols)

        if start_index == 0 and end_index != -1:
            self.title = self.value[len(start_symbols):end_index]
            self.body = self.value[end_index + len(end_symbols):]
        else:
            self.title = ""
            self.body = self.value

    def __extract_tags(self):
        matches = re.findall(r'#[A-z\d_]+', self.value)
        for match in matches:
            self.tags.append(match[1:])

    def __str__(self):
        result = ""
        if self.title:
            result += f'Title: {self.title}\n'              # deleted << >> in title printing
        result += f'Body: {self.body}'
        if len(self.tags) > 0:
            result += f'\nTags: {", ".join(self.tags)}'
        return result

    def short_str(self):
        if self.title:
            return self.title
        elif len(self.body) < 30:
            return self.body
        else:
            return f"{self.body[:30]}..."


class NoteBook(UserDict):
    id = 0

    def __init__(self):
        super().__init__()
        self.filename = './.note_book.json'
        self.load(self.filename)

    def load(self, filename=None):
        """
        Зчитування даних з JSON файлу і створення нотаток (Record)
        для даного екземпляру NoteBook.
        """
        if not filename:
            filename = self.filename
        try:
            with open(filename, "r", encoding="utf-8") as book_file:
                notes_dict = json.load(book_file)
        except OSError:
            # Файла з записами немає, тихо виходимо
            return
        except json.JSONDecodeError:
            print(f"Address book JSON file {filename} is broken.")
            return

        for note_id_str, note_text in notes_dict.items():
            try:
                if type(note_id_str) == str and type(note_text) == str:
                    note_id = int(note_id_str)
                    note = Note(note_text)
                    self[note_id] = note
                    if note_id > NoteBook.id:
                        NoteBook.id = note_id + 1
            except ValueError:
                continue

    def save(self, filename=None):
        """
        Зберігання всіх нотаток (Note) даного екземпляра NoteBook в JSON файл.
        Додатково використовується проміжний TMP файл для запобігання
        втрати даних під час відкриття файла на запис, але без подальшого запису
        у випадку нештатної ситуації.
        """
        if not filename:
            filename = self.filename
        to_store = {k: v.value for k, v in self.data.items()}
        notes_json = json.dumps(to_store, default=lambda o: o.__dict__, indent=4)
        with tempfile.NamedTemporaryFile('w', encoding="utf-8",
                                         dir='.', prefix=filename + '~', delete=False) as tf:
            tf.write(notes_json)
        # Fix for Windows: os.rename can be executed when tf is closed
        try:
            if os.path.exists(filename):
                os.remove(filename)
            os.rename(tf.name, filename)
        except OSError as error:
            print(error)

    def add_note(self, note: Note):
        self.data[NoteBook.id] = note
        NoteBook.id += 1

    def delete(self, id_to_delete: int):
        if self.data.pop(id_to_delete, None):
            return True
        return False

    def find_notes_by_text(self, text):
        result = {}
        for note_id, note in self.data.items():
            if text in note.value:
                result[note_id] = note

        return result

    def find_note_by_id(self, id_to_find):
        return self.data.get(id_to_find, None)

    def get_all_tags(self):
        result = defaultdict(list)
        for note_id, note in self.data.items():
            if len(note.tags) == 0:
                result["#"].append(str(note_id))
            else:
                for tag in note.tags:
                    result[tag].append(str(note_id))
        return result

    def find_notes_by_teg(self, tag):
        result = {}
        for note_id, note in self.data.items():
            if tag in note.tags:
                result[note_id] = note

        return result
