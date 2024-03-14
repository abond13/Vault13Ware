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


class NoTextError(Exception):
    pass


class NoIdEnteredError(Exception):
    pass


class NoIdFoundError(Exception):
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


class Birthday(datetime.date):  # Why not Field? #######################
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
        if self.find_phone(old_phone) and self.add_phone(new_phone) and (
                self.find_phone(old_phone) != self.add_phone(new_phone)):
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


class Note:

    def __init__(self, text: str):
        self.raw_text = text
        self.title = ""
        self.body = ""
        self.tags = []  # todo заповнити пізніше
        self.__extract_title_and_body()

    def __extract_title_and_body(self):
        """
        Заголовок може бути лише на початку нотатки і за умови, що він виділений спеціальними символами
        """
        start_symbols = '<<'
        end_symbols = '>>'
        start_index = self.raw_text.find(start_symbols)
        end_index = self.raw_text.find(end_symbols)

        if start_index == 0 and end_index != -1:
            self.title = self.raw_text[len(start_symbols):end_index]
            self.body = self.raw_text[end_index + len(end_symbols):]
        else:
            self.title = ""
            self.body = self.raw_text

    def __str__(self):
        if self.title:
            return f'Title: <<{self.title}>>\nBody: {self.body}'
        else:
            return f'Body: {self.body}'

    def short_str(self):
        if self.title:
            return self.title
        elif len(self.body) < 10:
            return self.body
        else:
            return f"{self.body[:10]}..."


class NoteBook(UserDict):
    id = 0

    def load(self):
        # TODO
        pass

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
            if text in note.raw_text:
                result[note_id] = note

        return result

    def find_note_by_id(self, id_to_find):
        return self.data.get(id_to_find, None)
