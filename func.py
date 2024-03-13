
from contextlib import contextmanager
from classes import NameFormatError, PhoneFormatError, BirthdayFormatError, EmailFormatError, Name, Phone, Address, Birthday, Record, AddressBook

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

def input_error(func):
    '''
    Судячи з усього - це декоратор обробки помилок
    '''
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me name please."
        except KeyError:
            return "No such contact."
        except NameFormatError:
            return "Wrong name format."
        except PhoneFormatError:
            return "Wrong phone format."
        except BirthdayFormatError:
            return "Wrong birthday format."
        except EmailFormatError:
            return "Wrong email format."
    return inner

def parse_input(user_input: str):
    '''
    Парсер введеного рядка
    '''
    cmd_string, *args = user_input.split()
    cmd_string = cmd_string.strip().lower()
    argums_tuple = (*args,)
    return cmd_string, argums_tuple

def help():
    '''
    Друк сторінки з синтаксисом команд
    '''
    print("Usage:")    #################### наповнити змістом #######################

def hello():
    '''
    Друк сторінки з привітанням
    '''
    print("How can I help you?") #################### наповнити змістом #######################

@input_error
def add_man(argums):
    '''
    Функція додавання контакту
    '''
    name = argums[0]
    record = AddressBook.find(name)
    if not record:
        record = Record(name)
        AddressBook.add_record(record)
        return "Contact added."
    return "[ERROR] Expected command: add <name>"

@input_error
def del_man(argums):
    '''
    Функція видалення контакту
    '''
    pass #################### наповнити кодом #######################

@input_error
def cng_man(argums):
    '''
    Функція зміни/оновлення контакту
    '''
    pass #################### наповнити кодом #######################

@input_error
def show_man(argums):
    '''
    Функція показу даних контакту
    '''
    pass #################### наповнити кодом #######################

@input_error
def find_man(argums):
    '''
    Функція пошуку контакту
    '''
    pass #################### наповнити кодом #######################

@input_error
def add_phone(argums):
    '''
    Функція додавання номеру(-ів) телефону(-ів)
    '''
    pass #################### наповнити кодом #######################

@input_error
def cng_phone(argums):
    '''
    Функція зміни номеру телефону
    '''
    pass  #################### наповнити кодом #######################

@input_error
def del_phone(argums):
    '''
    Функція зміни номеру телефону
    '''
    pass  #################### наповнити кодом #######################

@input_error
def add_email(argums):
    '''
    Функція додавання email
    '''
    pass  #################### наповнити кодом #######################

@input_error
def cng_email(argums):
    '''
    Функція додавання email
    '''
    pass  #################### наповнити кодом #######################

@input_error
def find_email(argums):
    '''
    Функція пошуку email
    '''
    pass  #################### наповнити кодом #######################

@input_error
def del_email(argums):
    '''
    Функція видаленя email
    '''
    pass  #################### наповнити кодом #######################

@input_error
def add_bday(argums):
    '''
    Функція додавання дня народження
    '''
    pass  #################### наповнити кодом #######################

@input_error
def cng_bday(argums):
    '''
    Функція додавання дня народження
    '''
    pass  #################### наповнити кодом #######################

@input_error
def del_bday(argums):
    '''
    Функція видалення дня народження
    '''
    pass  #################### наповнити кодом #######################

@input_error
def show_bday(argums):
    '''
    Функція видалення дня народження
    '''
    pass  #################### наповнити кодом #######################

@input_error
def add_adr(argums):
    '''
    Функція додавання адреси
    '''
    pass  #################### наповнити кодом #######################

@input_error
def del_adr(argums):
    '''
    Функція видалення адреси
    '''
    pass  #################### наповнити кодом #######################

@input_error
def find_adr(argums):
    '''
    Функція пошуку адреси
    '''
    pass  #################### наповнити кодом #######################


@input_error
def add_note(argums):
    '''
    Функція додавання нотатки
    '''
    pass  #################### наповнити кодом #######################

@input_error
def del_note(argums):
    '''
    Функція додавання нотатки
    '''
    pass  #################### наповнити кодом #######################

@input_error
def find_note(argums):
    '''
    Функція додавання нотатки
    '''
    pass  #################### наповнити кодом #######################

@input_error
def show_note(argums):
    '''
    Функція додавання нотатки
    '''
    pass  #################### наповнити кодом #######################

