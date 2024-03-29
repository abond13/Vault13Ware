from features import display, greeting, goodbye  # модуль з фічами
from classes import AddressBook, NoteBook  # модуль з класами
import func  # модуль з функціями виконання команд боту



def main():
    '''
     Main function
    '''

    # ініціалізація
    book = AddressBook()
    notes = NoteBook()
    greeting()
    func.hello()

    # work cycle
    while True:

        # parsing
        user_input = input("Enter a command >>> ")
        if user_input:
            command, args = func.parse_input(user_input)
        else:
            continue

        # handling
        if command in ("close", "exit", "quit"):
            goodbye()
            break

        elif command == "help":
            func.help_doc()

        elif command == "hello":
            func.hello()

        elif command == "add-man":
            func.add_man(args, book)
            func.save_book(book)

        elif command == "del-man":
            func.del_man(args, book)
            func.save_book(book)

        elif command == "cng-man":
            func.cng_man(args, book)
            func.save_book(book)

        elif command == "show-man":
            func.show_man(args, book)

        elif command == "find-man":
            func.find_man(args, book)

        elif command == "add-phone":
            func.add_phone(args, book)
            func.save_book(book)

        elif command == "cng-phone":
            func.cng_phone(args, book)
            func.save_book(book)

        elif command == "del-phone":
            func.del_phone(args, book)
            func.save_book(book)

        elif command == "add-email":
            func.add_email(args, book)
            func.save_book(book)

        elif command == "cng-email":
            func.cng_email(args, book)
            func.save_book(book)

        elif command == "find-email":
            func.find_email(args, book)

        elif command == "del-email":
            func.del_email(args, book)
            func.save_book(book)

        elif command == "add-bday":
            func.add_bday(args, book)
            func.save_book(book)

        elif command == "del-bday":
            func.del_bday(args, book)
            func.save_book(book)

        elif command == "show-bday":
            func.show_bday(args, book)

        elif command == "add-adr":
            func.add_adr(args, book)
            func.save_book(book)

        elif command == "del-adr":
            func.del_adr(args, book)
            func.save_book(book)

        elif command == "find-adr":
            func.find_adr(args, book)

        elif command == "add-note":
            func.add_note(args, notes)
            func.save_notes(notes)

        elif command == "del-note":
            func.del_note(args, notes)
            func.save_notes(notes)

        elif command == "find-note":
            func.find_note(args, notes)

        elif command == "show-note":
            func.show_note(args, notes)

        elif command == "find-tag":
            func.find_tag(args, notes)

        elif command == "show-sorted-tags":
            func.show_sorted_tags(notes)

        else:
            display("Invalid command. Type 'help' for get a list of commands.")


if __name__ == "__main__":
    main()
