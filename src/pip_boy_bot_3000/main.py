from pip_boy_bot_3000.features import display, greeting, goodbye  # модуль з фічами
from pip_boy_bot_3000.classes import AddressBook, NoteBook  # модуль з класами
from pip_boy_bot_3000.func import *  # модуль з функціями виконання команд боту



def main():
    '''
     Main function
    '''

    # ініціалізація
    book = AddressBook()
    notes = NoteBook()
    greeting()
    hello()

    # work cycle
    while True:

        # parsing
        user_input = input("Enter a command >>> ")
        if user_input:
            command, args = parse_input(user_input)
        else:
            continue

        # handling
        if command in ("close", "exit", "quit"):
            goodbye()
            break

        elif command == "help":
            help_doc()

        elif command == "hello":
            hello()

        elif command == "add-man":
            add_man(args, book)
            save_book(book)

        elif command == "del-man":
            del_man(args, book)
            save_book(book)

        elif command == "cng-man":
            cng_man(args, book)
            save_book(book)

        elif command == "show-man":
            show_man(args, book)

        elif command == "find-man":
            find_man(args, book)

        elif command == "add-phone":
            add_phone(args, book)
            save_book(book)

        elif command == "cng-phone":
            cng_phone(args, book)
            save_book(book)

        elif command == "del-phone":
            del_phone(args, book)
            save_book(book)

        elif command == "add-email":
            add_email(args, book)
            save_book(book)

        elif command == "cng-email":
            cng_email(args, book)
            save_book(book)

        elif command == "find-email":
            find_email(args, book)

        elif command == "del-email":
            del_email(args, book)
            save_book(book)

        elif command == "add-bday":
            add_bday(args, book)
            save_book(book)

        elif command == "del-bday":
            del_bday(args, book)
            save_book(book)

        elif command == "show-bday":
            show_bday(args, book)

        elif command == "add-adr":
            add_adr(args, book)
            save_book(book)

        elif command == "del-adr":
            del_adr(args, book)
            save_book(book)

        elif command == "find-adr":
            find_adr(args, book)

        elif command == "add-note":
            add_note(args, notes)
            save_notes(notes)

        elif command == "del-note":
            del_note(args, notes)
            save_notes(notes)

        elif command == "find-note":
            find_note(args, notes)

        elif command == "show-note":
            show_note(args, notes)

        elif command == "find-tag":
            find_tag(args, notes)

        elif command == "show-sorted-tags":
            show_sorted_tags(notes)

        else:
            display("Invalid command. Type 'help' for get a list of commands.")


if __name__ == "__main__":
    main()
