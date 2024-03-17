from datetime import datetime
import platform
import requests # API-для запитів
from classes import BirthdayFormatError, EmailFormatError, AddressFormatError,\
                    NameFormatError, PhoneFormatError, NoTextError,\
                    NoIdEnteredError, NoIdFoundError, MinArgsQuantityError, NotFoundNameError,\
                    Record, AddressBook, NoteBook, Note
if platform.system() == "Windows":
    import msvcrt  # для використання функції очикування натискання будь-якої клавіши


def input_error(func):
    '''
    Декоратор обробки помилок
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


def help_doc():
    '''
    Друк сторінки з синтаксисом команд
    help_doc - в файлі help.txt
    '''
    with open('help.txt', 'r') as file:
        print("\x1b[2J")  # clean the screen
        print(file.read())


def hello():
    '''
    Друк сторінки з привітанням. Відображаємо на старті. А також по команді hello.
    '''
    print("\x1b[2J")  # clean the screen
    print('Hail to you, representative of the remnants of humanity, bag of bones!\n')

    try:
        ip_address = requests.get('https://api.ipify.org', timeout=10).text
        location = requests.get(f'https://ipinfo.io/{ip_address}?token=746910603a9959', timeout=10).json()
        lat = location["loc"].split(',')[0]
        lon = location["loc"].split(',')[1]
        city = location["city"]
        region = location["region"]
        country = location["country"]
        weather_url = (f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}'
                      f'&appid=63a5ea9311a8d101ec009f9cd3145775&units=metric')
        weather = requests.get(weather_url, timeout=10).json()
        ex_rates = requests.get('https://api.monobank.ua/bank/currency', timeout=10).json()
        for line in ex_rates:
            if line['currencyCodeA'] == 840 and line['currencyCodeB'] == 980:
                dollar_buy_rate = line['rateBuy']
                dollar_sell_rate = line['rateSell']
            if line['currencyCodeA'] == 978 and line['currencyCodeB'] == 980:
                euro_buy_rate = line['rateBuy']
                euro_sell_rate = line['rateSell']
        # raise ValueError # for imitation of getting the server request answer 'not status '200''
        print(f"Now is {datetime.now().strftime('%a %d %b %Y, %I:%M%p')}."
              f" The best day for fighting for existence!")
        print(f"You are near the place marked on old maps as city:"
              f" {city}, region: {region}, country: {country}")
        print(f" The conditions for existence in your location is:"
              f" {weather['main']['temp']} \u00B0C")
        print(f"                                       "
              f"feels like: {weather['main']['feels_like']} \u00B0C")
        print(f"                                         "
              f"humidity: {weather['main']['humidity']}%")
        print(f"                                         "
              f"pressure: {weather['main']['pressure']} mm m.c.")
        print(f"                       The forecast for near time:"
              f" {weather['weather'][0]['description']}")
        print(f"The WaultTecBank gave now next exchange rate"
              f" for North American money papers: {dollar_buy_rate}/{dollar_sell_rate},"
              f" for Europa money papers: {euro_buy_rate}/{euro_sell_rate}\n")

    except requests.ConnectionError:  # when the server requests answer is not status '200'
        print('Сommunication satellite disabled by radiation emission.',
              ' Displaying your location and weather is temporarily unavailable.\n')

    finally:
        print("How can I help you?\n")


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
def del_man(args: tuple, book: AddressBook):
    """
    Функція видалення контакту
    """
    if len(args) < 1:
        raise MinArgsQuantityError
    
    name = args[0]
    result = book.delete(name)
    if result:
        print(f"Contact {name} deleted successfully.")
    else:
        raise NotFoundNameError

@input_error
def cng_man(args: tuple, book: AddressBook):
    """
    Функція зміни/оновлення контакту
    """
    if len(args) < 2:
        raise MinArgsQuantityError
    
    old_name, new_name = args
    record = book.find(old_name)
    if record:
        book.change_record(old_name, new_name)
        print(f"Contact name changed from {old_name} to {new_name}.")
    else:
        raise NotFoundNameError
    
@input_error
def find_man(args: tuple, book: AddressBook):
    """
    Функція пошуку контактів за підрядком
    Виводить імена, які мають в собі заданий підрядок тексту
    """
    if len(args) < 1:
        raise MinArgsQuantityError
    
    substring = args[0]
    print(f"\nContacts with '{substring}' in name:\n")
    flag = 0

    for name in book.keys():
        if substring.lower() in name.lower():
            flag = 1
            print(name)
    if flag == 0:
        print("Not found.")

@input_error
def show_man(args: tuple, book: AddressBook):
    '''
    Функція показу даних контакту
    '''
    PAGE_SIZE = 4  # Кількість контактів, які виводяться на екран за раз #TODO налаштувати константу на бойовому екрані
    os_type = platform.system()

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
        records_left = len(book.data)

        counter = 1  # стартове значення лічильника
        for record in book.data.values():
            records_left -= 1
            print(record)
            print('----------------')
            if counter >= PAGE_SIZE and records_left > 0:
                if os_type == "Windows":
                    print('\n                                           ',
                          '--- Press any key to continue ---            ',
                          '                                \n')
                    msvcrt.getch()  # очікування натискання будь-якої клавіши
                else:  #  очікування натискання клавіши (for Mac&Linux)
                    input('                                           '+\
                          '--- Press Enter key to continue ---        '+\
                          '                                    ')
                counter = 1
            else:
                counter += 1

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
def cng_phone(args: tuple, book: AddressBook):
    '''
    Функція зміни номеру телефону
    '''
    if len(args) < 3:
        raise MinArgsQuantityError
    
    name, old_phone, new_phone = args
    record = book.find(name)
    if record:
        success = record.change_phone(old_phone, new_phone)
        if success:
            print(f"Phone number updated from {old_phone} to {new_phone} for {name}.")
        else:
            print("Old phone number not found.")
    else:
        raise NotFoundNameError

@input_error
def del_phone(args: tuple, book: AddressBook):
    """
    Функція зміни номеру телефону.
    """
    com_min_args_qty = 2  # name & the phone to delete
    if len(args) < com_min_args_qty:
        raise MinArgsQuantityError
    
    name, phone = args
    record = book.find(name)
    if record:
        success = record.delete_phone(phone)
        if success:
            print(f"Phone number {phone} deleted for {name}.")
        else:
            print("Phone number not found.")
    else:
        raise NotFoundNameError


@input_error
def add_email(args: tuple, book: AddressBook):
    '''
    Функція додавання email
    '''
    com_min_args_qty = 2    # name & the first email
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
def cng_email(args: tuple, book: AddressBook):
    """
    Функція зміни пошти.
    """
    com_min_args_qty = 3    # name + old email + new email
    if len(args) < 3:
        raise MinArgsQuantityError
    
    name, old_email, new_email = args
    record = book.find(name)
    if record:
        success = record.change_email(old_email, new_email)
        if success:
            print(f"Email updated from {old_email} to {new_email} for {name}.")
        else:
            print("Old email not found.")
    else:
        raise NotFoundNameError



@input_error
def find_email(args: tuple, book: AddressBook):
    """
    Функція пошуку пошти.
    """
    if len(args) < 1:
        raise MinArgsQuantityError
    
    name = args[0]
    found = book.find_email(name)
    if found:
        print(f"Contact {name} has email:")
        for record in found:
            print(record)
    else:
        print("Email not found.")


@input_error
def del_email(args: tuple, book: AddressBook):
    """
    Функція видалення пошти.
    """
    if len(args) < 2:
        raise MinArgsQuantityError
    
    name, email = args
    record = book.find(name)
    if record:
        success = record.delete_email(email)
        if success:
            print(f"Email {email} deleted for {name}.")
        else:
            print("Email not found.")
    else:
        raise NotFoundNameError


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
            record.add_birthday(new_bday)
            print(f"{new_bday} is added as birthday for {name}.\n")
        else:
            record.add_birthday(new_bday)
            print(f"Email {new_bday} is updated as birthday to {name}.\n")
    else:
        raise NotFoundNameError


@input_error
def cng_bday(args: tuple, book: AddressBook):
    """
    Функція зміни дня народження.
    """
    if len(args) < 2:
        raise MinArgsQuantityError
    
    name, new_bday = args
    record = book.find(name)
    if record:
        success = record.change_birthday(new_bday)
        if success:
            print(f"Birthday updated to {new_bday} for {name}.")
        else:
            print("Error updating birthday.")
    else:
        raise NotFoundNameError

@input_error
def del_bday(args: tuple, book: AddressBook):
    """
    Функція видалення дня народження.
    """
    if len(args) < 1:
        raise MinArgsQuantityError

    name = args[0]
    record = book.find(name)
    if record:
        success = record.delete_birthday()
        if success:
            print(f"Birthday deleted for {name}.")
        else:
            print("Error deleting birthday or birthday not set.")
    else:
        raise NotFoundNameError


@input_error
def show_bday(args: tuple, book: AddressBook):
    '''
    Функція виведення днів народження в наперед заданому проміжку
    '''
    try:
        quantity = int(args[0])
    except IndexError:
        quantity = 7
    book.get_birthdays(quantity)


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
    new_address = ' '.join(args[1:])
    record = book.find(name)

    if record:
        if record.address is None:
            record.add_address(new_address)
            print(f"\n{new_address[:ADDRESS_LENGHT]}... is added as address for {name}.\n")
        else:
            record.add_address(new_address)
            print(f"\nAddress {new_address[:ADDRESS_LENGHT]}... is updated as address to {name}.\n")
    else:
        raise NotFoundNameError


@input_error
def del_adr(args: tuple, book: AddressBook):
    """
    Функція видалення адреси.
    """
    if len(args) < 1:
        raise MinArgsQuantityError

    name = args[0]
    record = book.find(name)
    if record:
        success = record.delete_address()
        if success:
            print(f"Address deleted for {name}.")
        else:
            print("Address not found or already deleted.")
    else:
        raise NotFoundNameError

@input_error
def find_adr(args: tuple, book: AddressBook):
    """
    функція пошуку адреси.
    """
    if len(args) < 1:
        raise MinArgsQuantityError

    name = args[0]
    found = book.find_address(name)
    if found:
        print(f"Address for {name}: {found}.")
    else:
        print("Address not found.")



@input_error
def save_book(book):
    '''
    Виклик зберігання адресної книги у файл
    '''
    book.save()


@input_error
def save_book(book):
    '''
    Виклик зберігання адресної книги у файл
    '''
    book.save()


@input_error
def add_note(args, notes: NoteBook):
    '''
    Функція додавання нотатки
    '''
    if len(args) == 0:
        raise NoTextError()

    text = " ".join(args)
    note = Note(text)
    notes.add_note(note)
    print("Note added")


@input_error
def del_note(args, notes: NoteBook):
    '''
    Функція видалення нотатки
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
    Функція пошуку в нотатках за текстом
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
    Функція виведення нотатки за її номером
    '''
    if len(args) == 0:
        raise NoIdEnteredError()
    id_to_find = int(args[0])
    note = notes.find_note_by_id(id_to_find)
    if note:
        print(note)
    else:
        raise NoIdFoundError()


@input_error
def find_tag(args, notes: NoteBook):
    '''
    Функція пошуку за тегом
    '''
    if len(args) == 0:
        raise NoTextError()
    teg = args[0]
    found_notes = notes.find_notes_by_teg(teg)
    if len(found_notes) == 0:
        print("No notes found")
    else:
        print("\n----\n".join(
            map(lambda note_item: f"{note_item[0]}: {note_item[1].short_str()}", found_notes.items())))


def show_sorted_tags(notes: NoteBook):
    '''
    Функція виведення всіх тегів за алфавітом.
    '''
    tags_dict = notes.get_all_tags()
    if len(tags_dict) == 0:
        print("Notebook is empty")
        return
    without_tags = tags_dict.pop("#", None)
    if without_tags:
        print(f"Without tags: {', '.join(without_tags)}")
    for tag in sorted(tags_dict.keys(), key=str.lower):
        print(f"Tag: {tag}, notes: {', '.join(tags_dict[tag])}")


@input_error
def save_notes(notes: NoteBook):
    '''
    Виклик зберігання нотаток у файл
    '''
    notes.save()
