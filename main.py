"""
    AddressBook Bot
"""
import AddressBook as AB

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me name please."
        except KeyError:
            return "No such contact."
        except AB.NameFormatError:
            return "Wrong name format."
        except AB.PhoneFormatError:
            return "Wrong phone format."
        except AB.BirthdayFormatError:
            return "Wrong birthday format."
        except AB.EmailFormatError:
            return "Wrong email format."
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def print_help(): # FIXME: Wrong commands
    return "Available commands:\n" + \
           "\tadd [name] [phone]\n" + \
           "\tchange [name] [old_phone] [new_phone]\n" + \
           "\tphone [name]\n" + \
           "\tadd-birthday [name] [birthday]\n" + \
           "\tshow-birthday [name]\n" + \
           "\tbirthdays\n" + \
           "\tall\n" + \
           "\texit"

@input_error
def add_contact(args, book):
    if len(args) == 2:
        name, phone_num = args
        record = book.find(name)
        if not record:
            record = AB.Record(name)
            book.add_record(record)
        record.add_phone(phone_num)
        book.save()
        return "Contact added."
    return "[ERROR] Expected command: add [name] [phone]"

@input_error
def change_contact(args, book):
    if len(args) == 3:
        name, old_phone, new_phone = args
        record = book.find(name)
        if record:
            record.edit_phone(old_phone, new_phone)
            book.save()
            return "Contact updated."
        return "[ERROR] No such contact."
    return "[ERROR] Expected command: change [name] [phone]"

@input_error
def phone(args, book):
    if len(args) == 1:
        name = args[0]
        record = book.find(name)
        if record:
            return record
        return "[ERROR] No such contact."
    return "[ERROR] Expected command: phone [name]"

@input_error
def add_birthday(args, book):
    if len(args) == 2:
        name, birthday = args
        record = book.find(name)
        if record:
            record.add_birthday(birthday)
            book.save()
            return "Birthday added."
        return "[ERROR] No such contact."
    return "[ERROR] Expected command: add-birthday [name] [birthday]"

@input_error
def show_birthday(args, book):
    if len(args) == 1:
        name = args[0]
        record = book.find(name)
        if record:
            return record.birthday
        return "[ERROR] No such contact."
    return "[ERROR] Expected command: show-birthday [name]"

@input_error
def birthdays(book):
    book.get_birthdays_per_week()

def main():
    book = AB.AddressBook()
    book.load()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if user_input:
            command, *args = parse_input(user_input)
        else:
            continue
        if command in ["close", "exit", "quit"]:
            print("Good bye!")
            book.save()
            break
        if command == "hello":
            print("How can I help you?")
        elif command == "help":
            print(print_help())
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(phone(args, book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args,book))
        elif command == "birthdays":
            birthdays(book)
        elif command == "all":
            print(book)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
