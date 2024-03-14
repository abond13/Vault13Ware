from classes import NameFormatError, PhoneFormatError, BirthdayFormatError, EmailFormatError, AddressFormatError, \
    NoTextError, NoIdEnteredError, NoIdFoundError
from classes import Name, Phone, Address, Birthday, Record, AddressBook, NoteBook, Note


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
        except NoTextError:
            return "Give me text please"
        except NoIdEnteredError:
            return "Give me id please"
        except NoIdFoundError:
            return "Cannot find id"

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
    print("Usage:")  # FIXME наповнити змістом #######################


def hello():
    '''
    Друк сторінки з привітанням
    '''
    print("How can I help you?")  # FIXME наповнити змістом #######################


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
    else:
        print(f"Contact {name} is exist already. Nothing is added.")


@input_error
def del_man(args):
    '''
    Функція видалення контакту
    '''
    pass  # FIXME наповнити кодом #######################


@input_error
def cng_man(args):
    '''
    Функція зміни/оновлення контакту
    '''
    pass  # FIXME наповнити кодом #######################


@input_error
def show_man(args):
    '''
    Функція показу даних контакту
    '''
    pass  # FIXME наповнити кодом #######################


@input_error
def find_man(args):
    '''
    Функція пошуку контакту
    '''
    pass  # FIXME наповнити кодом #######################


@input_error
def add_phone(args):
    '''
    Функція додавання номеру(-ів) телефону(-ів)
    '''
    pass  # FIXME наповнити кодом #######################


@input_error
def cng_phone(args):
    '''
    Функція зміни номеру телефону
    '''
    pass  # FIXME наповнити кодом #######################


@input_error
def del_phone(args):
    '''
    Функція зміни номеру телефону
    '''
    pass  # FIXME наповнити кодом #######################


@input_error
def add_email(args):
    '''
    Функція додавання email
    '''
    pass  # FIXME наповнити кодом #######################


@input_error
def cng_email(args):
    '''
    Функція додавання email
    '''
    pass  # FIXME наповнити кодом #######################


@input_error
def find_email(args):
    '''
    Функція пошуку email
    '''
    pass  # FIXME наповнити кодом #######################


@input_error
def del_email(args):
    '''
    Функція видаленя email
    '''
    pass  # FIXME наповнити кодом #######################


@input_error
def add_bday(args):
    '''
    Функція додавання дня народження
    '''
    pass  # FIXME наповнити кодом #######################


@input_error
def cng_bday(args):
    '''
    Функція додавання дня народження
    '''
    pass  # FIXME наповнити кодом #######################


@input_error
def del_bday(args):
    '''
    Функція видалення дня народження
    '''
    pass  # FIXME наповнити кодом #######################


@input_error
def show_bday(args):
    '''
    Функція видалення дня народження
    '''
    pass  # FIXME наповнити кодом #######################


@input_error
def add_adr(args):
    '''
    Функція додавання адреси
    '''
    pass  # FIXME наповнити кодом #######################


@input_error
def del_adr(args):
    '''
    Функція видалення адреси
    '''
    pass  # FIXME наповнити кодом #######################


@input_error
def find_adr(args):
    '''
    Функція пошуку адреси
    '''
    pass  # FIXME наповнити кодом #######################


@input_error
def add_note(args, notes: NoteBook):
    '''
    Функція додавання нотатки
    '''
    if len(args) == 0:
        raise NoTextError()

    text = args[0]
    note = Note(text)
    notes.add_note(note)
    print("Note added")


@input_error
def del_note(args, notes: NoteBook):
    '''
    Функція додавання нотатки
    '''
    if len(args) == 0:
        raise NoIdEnteredError()
    id_to_delete = int(args[0])
    if notes.delete(id_to_delete):
        print("Note deleted")
    else:
        raise NoIdFoundError()


@input_error
def find_note(args, notes: NoteBook):
    '''
    Функція додавання нотатки
    '''
    if len(args) == 0:
        raise NoTextError()
    text = args[0]
    found_notes = notes.find_notes_by_text(text)
    if len(found_notes) == 0:
        print("No notes found")
    else:
        print("\n----\n".join(
            map(lambda note_item: f"{note_item[0]}: {note_item[1].short_str()}", found_notes.items())))


@input_error
def show_note(args, notes: NoteBook):
    '''
    Функція додавання нотатки
    '''
    if len(args) == 0:
        raise NoIdEnteredError()
    id_to_find = int(args[0])
    note = notes.find_note_by_id(id_to_find)
    if note:
        print(note)
    else:
        raise NoIdFoundError()
