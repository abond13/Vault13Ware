from features import display
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
            display("Give me name and phone please.")
        except IndexError:
            display("Give me name please.")
        except KeyError:
            display("No such contact.")
        except NameFormatError:
            display("Wrong name format.")
        except PhoneFormatError:
            display("Wrong phone format.")
        except BirthdayFormatError:
            display("Wrong birthday format. Use DD.MM.YYYY.")
        except EmailFormatError:
            display("Wrong email format.")
        except AddressFormatError:
            display("Wrong address format.")
        except NoTextError:
            display("Give me text please")
        except NoIdEnteredError:
            display("Give me id please")
        except NoIdFoundError:
            display("Cannot find id")
        except MinArgsQuantityError:
            display("Not enough parameters for executing this command.")
        except NotFoundNameError:
            display("This contact is not found. Please add the contact first.")

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
        display(file.read())
        print('\n')


def hello():
    '''
    Друк сторінки з привітанням. Відображаємо на старті. А також по команді hello.
    '''
    # print("\x1b[2J")  # clean the screen
    display('Hail to you, representative of the remnants of humanity, bag of bones!\n')

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
        display(f"Now is {datetime.now().strftime('%a %d %b %Y, %I:%M%p')}."
              f" The best day for fighting for existence!\n")
        display(f"You are near the place marked on old maps as city:"
              f" {city}, region: {region}, country: {country}\n")
        display(f" The conditions for existence in your location is:"
              f" {weather['main']['temp']} \u00B0C\n")
        display(f"                                       "
              f"feels like: {weather['main']['feels_like']} \u00B0C\n")
        display(f"                                         "
              f"humidity: {weather['main']['humidity']}%\n")
        display(f"                                         "
              f"pressure: {weather['main']['pressure']} mm m.c.\n")
        display(f"                       The forecast for near time:"
              f" {weather['weather'][0]['description']}\n")
        display(f"The WaultTecBank gave now next exchange rate"
              f" for North American money papers: {dollar_buy_rate}/{dollar_sell_rate},"
              f" for European money papers: {euro_buy_rate}/{euro_sell_rate}\n")

    except requests.ConnectionError:  # when the server requests answer is not status '200'
        display('Сommunication satellite disabled by radiation emission.' +
              ' Displaying your location and weather is temporarily unavailable.\n')

    finally:
        display("How can I help you?\n")


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
        display(f"Contact {name} is added.")
    else:
        display(f"Contact {name} is exist already. Nothing is added.")


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
        display(f"Contact {name} deleted successfully.")
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
        display(f"Contact name changed from {old_name} to {new_name}.")
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
    display(f"\nContacts with '{substring}' in name:\n")
    flag = 0

    for name in book.keys():
        if substring.lower() in name.lower():
            flag = 1
            display(name)
    if flag == 0:
        display("Not found.")

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
        record_string = (f"Contact name: {record.name.value}, \n" + f"    birthday: {record.birthday}, \n" +
                         f"      phones: {'; '.join(p.value for p in record.phones)}, \n" +
                         f"      emails: {'; '.join(e.value for e in record.emails)}, \n" +
                         f"     address: {record.address}\n")
        if record:
            display('\nContact profile:')
            display('----------------')
            display(f'{record_string}\n')
            display('----------------')
        else:
            raise NotFoundNameError
    else:
        if len(book.data) < 1:
            display('No contacts')
            return

        display('\nContact profiles:')
        display('----------------')
        records_left = len(book.data)

        counter = 1  # стартове значення лічильника
        for record in book.data.values():
            records_left -= 1
            record_string = (f"Contact name: {record.name.value}, \n" + f"    birthday: {record.birthday}, \n" +
                             f"      phones: {'; '.join(p.value for p in record.phones)}, \n" +
                             f"      emails: {'; '.join(e.value for e in record.emails)}, \n" +
                             f"     address: {record.address}\n")
            display(record_string)
            display('----------------')
            if counter >= PAGE_SIZE and records_left > 0:
                if os_type == "Windows":
                    display('\n                                           '+
                          '--- Press any key to continue ---            '+
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
                display(f"Phone number {phone} is added to {name}.\n")
            else:
                display(f"Phone number {phone} exists for {name} already.\n")
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
            display(f"Phone number updated from {old_phone} to {new_phone} for {name}.")
        else:
            display("Old phone number not found.")
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
            display(f"Phone number {phone} deleted for {name}.")
        else:
            display("Phone number not found.")
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
                display(f"Email {email} is added to {name}.\n")
            else:
                display(f"Email {email} exists for {name} already.\n")
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
            display(f"Email updated from {old_email} to {new_email} for {name}.")
        else:
            display("Old email not found.")
    else:
        raise NotFoundNameError


@input_error
def find_email(args: tuple, book: AddressBook):
    """
    Функція пошуку пошти за підрядком.
    Виводить список електроних пошт, які мають в собі заданий підрядок
    """
    if len(args) < 1:
        raise MinArgsQuantityError

    substring = args[0]
    display(f"\nContacts with '{substring}' in email:\n")
    flag = 0

    for name, record in book.items():

        # Перевіряємо, чи є у даного контакта хоча б одна пошта, яка містить в собі підрядок substring
        if len(list(filter(lambda email: substring in email.value, record.emails))):
            flag = 1
            display(f"{name}:")
            for email in filter(lambda email: substring in email.value, record.emails):
                display(email.value)
            print()
    if flag == 0:
        display("Not found.\n")


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
            display(f"Email {email} deleted for {name}.")
        else:
            display("Email not found.")
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
            display(f"{new_bday} is added as birthday for {name}.\n")
        else:
            record.add_birthday(new_bday)
            display(f"Email {new_bday} is updated as birthday to {name}.\n")
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
            display(f"Birthday updated to {new_bday} for {name}.")
        else:
            display("Error updating birthday.")
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
            display(f"Birthday deleted for {name}.")
        else:
            display("Error deleting birthday or birthday not set.")
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
            display(f"\n{new_address[:ADDRESS_LENGHT]}... is added as address for {name}.\n")
        else:
            record.add_address(new_address)
            display(f"\nAddress {new_address[:ADDRESS_LENGHT]}... is updated as address to {name}.\n")
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
            display(f"Address deleted for {name}.")
        else:
            display("Address not found or already deleted.")
    else:
        raise NotFoundNameError

@input_error
def find_adr(args: tuple, book: AddressBook):
    """
    Функція пошуку адреси.
    Виводить на екран контакти, адреса яких містить в собі заданий підрядок
    """
    if len(args) < 1:
        raise MinArgsQuantityError

    substring = args[0]
    display(f"\nContacts with '{substring}' in address:\n")
    flag = 0

    for name, record in book.items():
        
        # Якщо адреса не задана, то пропускаємо даний контакт
        if record.address is None:
            continue
        
        # Перевіряємо, чи адреса даного контакта містить в собі підрядок substring
        if substring in record.address.value:
            flag = 1
            display(f"{name}: {record.address}")

    if flag == 0:
        display("Not found.\n")
    else: display('')               # just for design


@input_error
def save_book(book):
    '''
    Виклик зберігання адресної книги у файл
    '''
    book.save()


# @input_error
# def save_book(book):
#     '''
#     Виклик зберігання адресної книги у файл
#     '''
#     book.save()


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
    display("Note added")


@input_error
def del_note(args, notes: NoteBook):
    '''
    Функція видалення нотатки
    '''
    if len(args) == 0:
        raise NoIdEnteredError()
    id_to_delete = int(args[0])
    if notes.delete(id_to_delete):
        display("Note deleted")
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
        display("No notes found")
    else:
        display("\n----\n".join(
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
    if note: # в ідеалі треба створити метод, який би повертав рядок для виводу на display (аналог __str__ для print)
        result = ""
        if note.title:
            result += f"Title: <<{note.title}>>\n"
        result += f"Body: {note.body}"
        if len(note.tags) > 0:
            result += f'\nTags: {", ".join(note.tags)}'
        display(result)
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
        display("No notes found")
    else:
        display("\n----\n".join(
            map(lambda note_item: f"{note_item[0]}: {note_item[1].short_str()}", found_notes.items())))


def show_sorted_tags(notes: NoteBook):
    '''
    Функція виведення всіх тегів за алфавітом.
    '''
    tags_dict = notes.get_all_tags()
    if len(tags_dict) == 0:
        display("Notebook is empty")
        return
    without_tags = tags_dict.pop("#", None)
    if without_tags:
        display(f"Without tags: {', '.join(without_tags)}")
    for tag in sorted(tags_dict.keys(), key=str.lower):
        display(f"Tag: {tag}, notes: {', '.join(tags_dict[tag])}")


@input_error
def save_notes(notes: NoteBook):
    '''
    Виклик зберігання нотаток у файл
    '''
    notes.save()
