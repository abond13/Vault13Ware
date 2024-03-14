
from classes import NameFormatError, PhoneFormatError, BirthdayFormatError, EmailFormatError, AddressFormatError
from classes import Name, Phone, Address, Birthday, Record, AddressBook, Email

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
    print("Usage:")    # FIXME наповнити змістом #######################

def hello():
    '''
    Друк сторінки з привітанням
    '''
    print("How can I help you?") # FIXME наповнити змістом #######################

@input_error
def add_man(args: tuple):
    '''
    Функція додавання контакту
    '''
    if len(args) == 0:
        print("Ім'я не введено. Будь ласка, введіть або отримайте довідку (command 'Help').")
        return

    name = args[0]
    record = AddressBook.find(name)
    if not record:
        record = Record(name)
        AddressBook.add_record(record)
        print(f"Контакт {name} додано.")
    else:
        print(f"Контакт {name} вже створенно.")

@input_error
def del_man(args):
    '''
    Функція видалення контакту
    '''
    if len(args) == 0:
        print("Ім'я не введено. Будь ласка, введіть ім'я або отримайте допомогу (команда 'Help').")
        return

    name = args[0]
    try:
        AddressBook.delete_record(name)
        print(f"Контакт {name} видалено.")
    except KeyError:
        print(f"Контакт з іменем {name} не існує.")

@input_error
def cng_man(args):
    '''
    Функція зміни/оновлення контакту
    '''
    if len(args) < 2:
        print("Недостатньо даних. Будь ласка, надайте ім'я та нові деталі.")
        return
    
    name = args[0]
    new_detail = args[1]  # Це може бути номер телефону, електронна адреса тощо, залежно від реалізації.
    try:
        record = AddressBook.find(name)
        record.update_detail(new_detail)  
        print(f"Контакт {name} оновлено з новим деталем: {new_detail}.")
    except KeyError:
        print(f"Контакт з іменем {name} не існує.")

@input_error
def show_man(args):
    '''
    Функція показу даних контакту
    '''
    if len(args) == 0:
        print("Ім'я не введено. Будь ласка, введіть ім'я або отримайте допомогу (команда 'Help').")
        return

    name = args[0]
    try:
        record = AddressBook.find(name)
        print(f"Деталі контакту для {name}: {record}")
    except KeyError:
        print(f"Контакт з іменем {name} не існує.")

@input_error
def find_man(args):
    '''
    Функція пошуку контакту
    '''
    if len(args) == 0:
        print("Будь ласка, введіть критерій пошуку.")
        return
    
    search_term = args[0]
    results = AddressBook.search(search_term)  # Припускаємо, що в AddressBook є метод пошуку.
    if results:
        for result in results:
            print(result)
    else:
        print("Співпадінь не знайдено.")

@input_error
def add_phone(args):
    '''
    Функція додавання номеру(-ів) телефону(-ів)
    '''
    if len(args) < 2:
        return "Будь ласка, вкажіть ім'я та принаймні один номер телефону."
    
    name, *phones = args
    try:
        record = AddressBook.find(name)
        for phone in phones:
            record.add_phone(Phone(phone))
        print(f"Телефон {phones} додано до {name}.")
    except KeyError:
        return "Такого контакту немає."

@input_error
def cng_phone(args):
    '''
    Функція зміни номеру телефону
    '''
    if len(args) < 3:
        return "Будь ласка, вкажіть ім'я, старий номер телефону та новий номер телефону."
    
    name, old_phone, new_phone = args
    try:
        record = AddressBook.find(name)
        record.change_phone(Phone(old_phone), Phone(new_phone))
        print(f"Телефон {old_phone} змінено на новий {new_phone} для контакту {name}.")
    except KeyError:
        return "Такого контакту або номера телефону немає."

@input_error
def del_phone(args):
    '''
    Функція зміни номеру телефону
    '''
    if len(args) < 2:
        return "Будь ласка, вкажіть ім'я та номер телефону, який ви хочете видалити."
    
    name, phone = args
    try:
        record = AddressBook.find(name)
        record.remove_phone(Phone(phone))
        print(f"Телефон {phone} видалено у {name}.")
    except KeyError:
        return "Такого контакту або номера телефону немає."

@input_error
def add_email(args):
    '''
    Функція додавання email
    '''
    if len(args) < 2:
        return "Будь ласка, вкажіть ім'я та електронну адресу."
    
    name, email = args
    try:
        record = AddressBook.find(name)
        record.add_email(Email(email))   #####???????????
        print(f"Email {email} додано до {name}.")
    except KeyError:
        return "Такого контакту немає."

@input_error
def cng_email(args):
    '''
    Функція додавання email
    ''' 
    if len(args) < 3:
        return "Будь ласка, вкажіть ім'я, стару та нову електронну пошту."
    
    name, old_email, new_email = args
    try:
        record = AddressBook.find(name)
        record.change_email(Email(old_email), Email(new_email))
        print(f"Email {old_email} змінено на {new_email} для {name}.")
    except KeyError:
        return "Такого контакту чи електронної пошти немає."

@input_error
def find_email(args):
    '''
    Функція пошуку email
    '''
    if len(args) < 1:
        return   "Будь ласка, введіть адресу електронної пошти для пошуку."
    email = args[0]
    found = False
    for record in AddressBook.data.values():
        if email in [e.value for e in record.emails]:
            print(f"Знайдено електронну пошту {email} для контакту {record.name.value}.")
            found = True
    if not found:
        print(f"Контакту з електронною поштою {email} не знайдено.")

@input_error
def del_email(args):
    '''
    Функція видаленя email
    '''
    if len(args) < 2:
        return "Будь ласка, вкажіть ім'я та адресу електронної пошти, яку ви хочете видалити."
    
    name, email = args
    try:
        record = AddressBook.find(name)
        record.remove_email(Email(email))
        print(f"Email {email} видалено у {name}.")
    except KeyError:
        return "Такого контакту чи електронної пошти немає."

@input_error
def add_bday(args):
    '''
    Функція додавання дня народження
    '''
    if len(args) < 2:
        return "Будь ласка, вкажіть ім'я та дату народження (DD-MM-YYYY)."
    
    name, bday = args
    try:
        record = AddressBook.find(name)
        record.add_birthday(Birthday(bday))
        print(f"День народження {bday} додано до {name}.")
    except KeyError:
        return "Такого контакту немає."

@input_error
def cng_bday(args):
    '''
    Функція додавання дня народження
    '''
    if len(args) < 2:
        return "Будь ласка, вкажіть ім'я та новий день народження (DD-MM-YYYY)."
    
    name, bday = args
    try:
        record = AddressBook.find(name)
        record.change_birthday(Birthday(bday))
        print(f"День народженння {bday} змінено для {name}.")
    except KeyError:
        return "Такого контакту немає."

@input_error
def del_bday(args):
    '''
    Функція видалення дня народження
    '''
    if len(args) < 1:
        return "Будь ласка, вкажіть ім'я та день народження кого ви хочете видалити."
    
    name = args[0]
    try:
        record = AddressBook.find(name)
        record.remove_birthday()
        print(f"День народження видалено у {name}.")
    except KeyError:
        return "Такого контакту немає."

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
    if len(args) < 2:
        return "Будь ласка, вкажіть ім'я та адресу."
    
    name, address = args[0], " ".join(args[1:])
    try:
        record = AddressBook.data[name]
        if not record.address:
            record.address = Address(address)
            print(f"Адреса '{address}' додана до {name}.")
        else:
            print(f"{name} вже має адресу. Використовуйте 'cng_adr', щоб змінити її.")
    except KeyError:
        return f"Адресу для {name} не вказано."
    
@input_error 
def cng_adr(args):
    '''
    Змінює адресу контакту.
    '''
    if len(args) < 2:
        return "Будь ласка, вкажіть назву та нову адресу."
    
    name, new_address = args[0], " ".join(args[1:])
    try:
        record = AddressBook.data[name]
        record.address = Address(new_address)
        print(f"Адреса для {name} зміненна на нову '{new_address}'.")
    except KeyError:
        return f"Адресу для {name} не вказано."

@input_error
def del_adr(args):
    '''
    Функція видалення адреси
    '''
    if len(args) < 1:
        return "Будь ласка, вкажіть ім'я, з якого потрібно видалити адресу."
    
    name = args[0]
    try:
        record = AddressBook.data[name]
        if record.address:
            record.address = None
            print(f"Адреса видалена з {name}.")
        else:
            print(f"{name} не має адреси для видалення.")
    except KeyError:
        return f"Адресу для {name} не вказано."

@input_error
def find_adr(args):
    '''
    Функція пошуку адреси
    '''
    if len(args) < 1:
        return "Будь ласка, вкажіть адресу для пошуку."
    
    search_address = " ".join(args)
    found = False
    for name, record in AddressBook.data.items():
        if record.address and record.address.value == search_address:
            print(f"Знайдено адресу '{search_address}'  для контакту {name}.")
            found = True
    if not found:
        print(f"Контактів за адресою '{search_address}' не знайдено.")

@input_error
def add_note(args):
    '''
    Функція додавання нотатки
    '''
    pass  # FIXME наповнити кодом #######################

@input_error
def del_note(args):
    '''
    Функція додавання нотатки
    '''
    pass  # FIXME наповнити кодом #######################

@input_error
def find_note(args):
    '''
    Функція додавання нотатки
    '''
    pass  # TODO наповнити кодом #######################

@input_error
def show_note(args):
    '''
    Функція додавання нотатки
    '''
    pass  # TODO наповнити кодом #######################

