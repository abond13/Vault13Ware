
from contextlib import contextmanager
from classes import AddressFormatError, NameFormatError, PhoneFormatError, BirthdayFormatError, EmailFormatError, Name, Phone, Address, Birthday, Record, AddressBook

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
    except AddressFormatError:
        print("Wrong address")

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
        except AddressFormatError:
            return "Wrong email format."
    return inner

def parse_input(user_input: str):
    '''
    Парсер введеного рядка
    '''
    cmd_string, *args = user_input.split()
    cmd_string = cmd_string.strip().lower()
    args_tuple = (*args,)
    return cmd_string, args_tuple

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
def add_man(args: tuple):
    '''
    Функція додавання контакту
    '''
    if len(args) == 0:
        print("Name isn't entered. Please enter or get help (command 'Help').")
        return

    name = args[0]
    record = AddressBook.find(name)
    if not record:
        record = Record(name)
        AddressBook.add_record(record)
        print(f"Contact {name} added.")
        return
    print(f"Contact {name} is exist already. Nothing is added.")

@input_error
def del_man(args):
    '''
    Функція видалення контакту
    '''
    pass #################### наповнити кодом #######################

@input_error
def cng_man(args):
    '''
    Функція зміни/оновлення контакту
    '''
    pass #################### наповнити кодом #######################

@input_error
def show_man(args):
    '''
    Функція показу даних контакту
    '''
    pass #################### наповнити кодом #######################

@input_error
def find_man(args):
    '''
    Функція пошуку контакту
    '''
    pass #################### наповнити кодом #######################

@input_error
def add_phone(args):
    '''
    Функція додавання номеру(-ів) телефону(-ів)
    '''
    pass #################### наповнити кодом #######################

@input_error
def cng_phone(args):
    '''
    Функція зміни номеру телефону
    '''
    pass  #################### наповнити кодом #######################

@input_error
def del_phone(args):
    '''
    Функція зміни номеру телефону
    '''
    pass  #################### наповнити кодом #######################

@input_error
def add_email(args):
    '''
    Функція додавання email
    '''
    pass  #################### наповнити кодом #######################

@input_error
def cng_email(args):
    '''
    Функція додавання email
    '''
    pass  #################### наповнити кодом #######################

@input_error
def find_email(args):
    '''
    Функція пошуку email
    '''
    pass  #################### наповнити кодом #######################

@input_error
def del_email(args):
    '''
    Функція видаленя email
    '''
    pass  #################### наповнити кодом #######################

@input_error
def add_bday(args):
    '''
    Функція додавання дня народження
    '''
    pass  #################### наповнити кодом #######################

@input_error
def cng_bday(args):
    '''
    Функція додавання дня народження
    '''
    pass  #################### наповнити кодом #######################

@input_error
def del_bday(args):
    '''
    Функція видалення дня народження
    '''
    pass  #################### наповнити кодом #######################

@input_error
def show_bday(args):
    '''
    Функція видалення дня народження
    '''
    pass  #################### наповнити кодом #######################

@input_error
def add_adr(args):
    '''
    Функція додавання адреси
    '''
    pass  #################### наповнити кодом #######################

@input_error
def del_adr(args):
    '''
    Функція видалення адреси
    '''
    pass  #################### наповнити кодом #######################

@input_error
def find_adr(args):
    '''
    Функція пошуку адреси
    '''
    pass  #################### наповнити кодом #######################


@input_error
def add_note(args):
    '''
    Функція додавання нотатки
    '''
    pass  #################### наповнити кодом #######################

@input_error
def del_note(args):
    '''
    Функція додавання нотатки
    '''
    pass  #################### наповнити кодом #######################

@input_error
def find_note(args):
    '''
    Функція додавання нотатки
    '''
    pass  #################### наповнити кодом #######################

@input_error
def show_note(args):
    '''
    Функція додавання нотатки
    '''
    pass  #################### наповнити кодом #######################

