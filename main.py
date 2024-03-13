from classes import AddressBook, NoteBook # модуль з класами
import func # модуль з функціями базового функціоналу
import features # модуль з фічами


def main():
    '''
     Main function
    '''

    # ініціалізація
    book = AddressBook.load()
    notes = NoteBook.load()
    features.greeting()

    # work cycle
    while True:

        # parsing
        user_input = input("Enter a command >>> ")
        if user_input:
            command, argums = func.parse_input(user_input)
        else:
            continue

        # handling
        if command in ("close", "exit", "quit"):
            book.save()
            features.goodbye()
            break

        elif command == "help":
            func.help()

        elif command == "hello":
            func.hello()

        elif command == "add-man":
            func.add_man(argums)

        elif command == "del-man":
            func.del_man(argums)

        elif command == "cng-man":
            func.cng_man(argums)

        elif command == "show-man":
            func.show_man(argums)

        elif command == "find-man":
            func.find_man(argums)

        elif command == "add-phone":
            func.add_phone(argums)

        elif command == "cng-phone":
            func.cng_phone(argums)

        elif command == "del-phone":
            func.del_phone(argums)

        elif command == "add-email":
            func.add_email(argums)

        elif command == "cng-email":
            func.cng_email(argums)

        elif command == "find-email":
            func.find_email(argums)

        elif command == "del-email":
            func.del_email(argums)

        elif command == "add-bday":
            func.add_bday(argums)

        elif command == "cng-bday":
            func.cng_bday(argums)

        elif command == "del-bday":
            func.del_bday(argums)

        elif command == "show-bday":
            func.show_bday(argums)

        elif command == "add-adr":
            func.add_adr(argums)

        elif command == "del-adr":
            func.del_adr(argums)

        elif command == "find-adr":
            func.find_adr(argums)

        elif command == "add-note":
            func.add_note(argums)

        elif command == "del-note":
            func.del_note(argums)

        elif command == "find-note":
            func.find_note(argums)

        elif command == "show-note":
            func.show_note(argums)

        else:
            print("Invalid command. Type 'help' for get a list of commands.")
if __name__ == "__main__":
    main()