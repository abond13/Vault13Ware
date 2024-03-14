from classes import NameFormatError, PhoneFormatError, BirthdayFormatError, EmailFormatError, AddressFormatError, \
    NoTextError, NoIdEnteredError, NoIdFoundError, MinArgsQuantityError, NotFoundNameError
from classes import Name, Phone, Address, Birthday, Record, AddressBook, NoteBook, Note
import msvcrt # для використання функції очикування натискання будь-якої клавіши


def input_error(func):
    '''
    Судячи з усього - це декоратор обробки помилок
    '''
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print("Give me name and phone please.")
        except IndexError:
            print("Give me name please.")
        except KeyError:
            print("No such contact.")
        except NameFormatError:
            print("Wrong name format.")
        except PhoneFormatError:
            print("Wrong phone format.")
        except BirthdayFormatError:
            print("Wrong birthday format.")
        except EmailFormatError:
            print("Wrong email format.")
        except AddressFormatError:
            print("Wrong address format.")
        except NoTextError:
            print("Give me text please")
        except NoIdEnteredError:
            print("Give me id please")
        except NoIdFoundError:
            print("Cannot find id")
        except MinArgsQuantityError:
            print("Not enough parameters for executing this command.")
        except NotFoundNameError:
            print("This contact is not found. Please add the contact first.")
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
def add_man(args: tuple, book: AddressBook):
    '''
    Функція додавання контакту
    '''
    com_min_args_qty = 1  # name
    if len(args) < com_min_args_qty:
        raise MinArgsQuantityError

    name = args[0]
    record = book.find(name)
    if not record:
        record = Record(name)
        book.add_record(record)
        print(f"Contact {name} is added.")
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
def show_man(args: tuple, book: AddressBook):
    '''
    Функція показу даних контакту
    '''
    PAGE_SIZE = 4 # Кількість контактів, які виводяться на екран за раз #TODO налаштувати константу на бойовому екрані

    if len(args) >= 1:
        name = args[0]
        record = book.find(name)
        if record:
            print('\nContact profile:')
            print('----------------')
            print(f'{record}\n')
            print('----------------')
        else:
            raise NotFoundNameError
    else:
        if len(book.data) < 1:
            print('No contacts')
            return

        print('\nContact profiles:')
        print('----------------')

        counter = 1 # стартове значення лічильника
        for record in book.data.values():
            print(f'{book.find(record)}')
            print('----------------')
            if counter >= PAGE_SIZE:
                print(f'\n                                           --- Press any key to continue ---                                            \n')
                msvcrt.getch() # очикування натискання будь-якої клавіши
                counter = 1
            else:
                counter += 1


@input_error
def find_man(args):
    '''
    Функція пошуку контакту
    '''
    pass  # FIXME наповнити кодом #######################


@input_error
def add_phone(args: tuple, book: AddressBook):
    '''
    Функція додавання номеру(-ів) телефону(-ів)
    '''
    com_min_args_qty = 2  # name & the first phone number
    if len(args) < com_min_args_qty:
        raise MinArgsQuantityError

    name = args[0]
    new_phones_tuple = args[1:]
    record = book.find(name)

    if record:
        for phone in new_phones_tuple:
            if not record.find_phone(phone):
                record.add_phone(phone)
                print(f"Phone number {phone} is added to {name}.\n")
            else:
                print(f"Phone number {phone} exists for {name} already.\n")
    else:
        raise NotFoundNameError


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
def add_email(args: tuple, book: AddressBook):
    '''
    Функція додавання email
    '''
    com_min_args_qty = 2  # name & the first email
    if len(args) < com_min_args_qty:
        raise MinArgsQuantityError

    name = args[0]
    new_email_tuple = args[1:]
    record = book.find(name)

    if record:
        for email in new_email_tuple:
            if record.find_email(email) is None:
                record.add_email(email)
                print(f"Email {email} is added to {name}.\n")
            else:
                print(f"Email {email} exists for {name} already.\n")
    else:
        raise NotFoundNameError


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
def add_bday(args: tuple, book: AddressBook):
    '''
    Функція додавання дня народження
    '''
    com_min_args_qty = 2  # name & new_bday
    if len(args) < com_min_args_qty:
        raise MinArgsQuantityError

    name = args[0]
    new_bday = args[1]
    record = book.find(name)

    if record:
        if record.birthday is None:
            record.add_bday(new_bday)
            print(f"{new_bday} is added as birthday for {name}.\n")
        else:
            record.add_bday(new_bday)
            print(f"Email {new_bday} is updated as birthday to {name}.\n")
    else:
        raise NotFoundNameError



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
def add_adr(args: tuple, book: AddressBook):
    '''
    Функція додавання адреси
    '''
    ADDRESS_LENGHT = 15

    com_min_args_qty = 2  # name & new_address
    if len(args) < com_min_args_qty:
        raise MinArgsQuantityError

    name = args[0]
    new_address = args[1]
    record = book.find(name)

    if record:
        if record.address is None:
            record.add_address(new_address)
            print(f"\n{new_address[:ADDRESS_LENGHT]}... is added as address for {name}.\n")
        else:
            record.add_address(new_address)
            print(f"\nEmail {new_address[:ADDRESS_LENGHT]}... is updated as address to {name}.\n")
    else:
        raise NotFoundNameError


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
