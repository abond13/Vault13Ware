from classes import AddressBook, NoteBook  # модуль з класами
import func  # модуль з функціями виконання команд боту
import features  # модуль з фічами


def main():
    '''
     Main function
    '''

    # ініціалізація
    book = AddressBook()
    book.load()
    notes = NoteBook()
    notes.load()
    features.greeting()

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
            features.goodbye()
            break

        elif command == "help":
            func.help()

        elif command == "hello":
            func.hello()

        elif command == "add-man":
            func.add_man(args)

        elif command == "del-man":
            func.del_man(args)

        elif command == "cng-man":
            func.cng_man(args)

        elif command == "show-man":
            func.show_man(args)

        elif command == "find-man":
            func.find_man(args)

        elif command == "add-phone":
            func.add_phone(args)

        elif command == "cng-phone":
            func.cng_phone(args)

        elif command == "del-phone":
            func.del_phone(args)

        elif command == "add-email":
            func.add_email(args)

        elif command == "cng-email":
            func.cng_email(args)

        elif command == "find-email":
            func.find_email(args)

        elif command == "del-email":
            func.del_email(args)

        elif command == "add-bday":
            func.add_bday(args)

        elif command == "cng-bday":
            func.cng_bday(args)

        elif command == "del-bday":
            func.del_bday(args)

        elif command == "show-bday":
            func.show_bday(args)

        elif command == "add-adr":
            func.add_adr(args)

        elif command == "del-adr":
            func.del_adr(args)

        elif command == "find-adr":
            func.find_adr(args)

        elif command == "add-note":
            func.add_note(args, notes)

        elif command == "del-note":
            func.del_note(args, notes)

        elif command == "find-note":
            func.find_note(args, notes)

        elif command == "show-note":
            func.show_note(args, notes)

        else:
            print("Invalid command. Type 'help' for get a list of commands.")


if __name__ == "__main__":
    main()
