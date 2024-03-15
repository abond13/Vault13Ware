<<<<<<< HEAD
import func
from colorama import Fore, Back, Style
from colorama import just_fix_windows_console
import time, platform
from datetime import datetime
=======
from datetime import datetime
import time
import platform
from colorama import Fore, Back, Style
from colorama import just_fix_windows_console
import func

>>>>>>> 5becf1ab98f34ff7938a219bdf1b6a9455942091
if platform.system() == "Windows":
    import winsound


def display(today_style_string: str):
    '''
    old-computer-style printing function
    '''
    just_fix_windows_console()
    print_style = Fore.GREEN + Back.BLACK + Style.BRIGHT

    print(print_style + "\033[40m")  # чорний колір в терміналі

    os_type = platform.system()

    for char in today_style_string:
        print(print_style + char, end="", flush=True)
        if os_type == "Windows":
            winsound.Beep(840, 80)
            time.sleep(0.001)
        else:
            time.sleep(0.04)

def greeting():
    '''
    Відображення фічі СтартоваЗаставка
    '''
    print_style = Fore.GREEN + Back.BLACK + Style.BRIGHT
    print(print_style + "\033[40m")  # чорний колір в терміналі
    print(print_style + "\x1b[2J")  # clean the screen

    with open('splash_screen.txt', 'r') as file:
        print(print_style + file.read())

    print('\n\n\n')
    print(print_style + "Welcome to Personal Information Processor PIP-Boy-Bot-3000!\n")
<<<<<<< HEAD
    print(print_style + "VaultTec Personal computer Copyright(C) 1981, 1982, 1983, 1984 by VaultTec Corporation\n")
=======
    print(print_style + "VaultTec Personal computer Copyright(C) 1981, 1982, 1983, 1984" +\
                        " by VaultTec Corporation\n")
>>>>>>> 5becf1ab98f34ff7938a219bdf1b6a9455942091
    print(print_style + "640 K RAM\n")
    print(print_style + "** CMOS]\n")
    print(print_style + "Date / Time: **\n")
    print(print_style + f"{datetime.now().date()}\n")
    print(print_style + f"{datetime.now().time().strftime('%I:%M%p')}\n")
<<<<<<< HEAD
    print(print_style + f"** Type the name of the command interpreter: COMMAND.COM **")
=======
    print(print_style + "** Type the name of the command interpreter: COMMAND.COM **")
>>>>>>> 5becf1ab98f34ff7938a219bdf1b6a9455942091
    print('\n\n\n')

    func.hello()


def goodbye():
    '''
    Відображення фічі ФінальнаЗаставка
    '''
    print_style = Fore.GREEN + Back.BLACK + Style.BRIGHT
<<<<<<< HEAD
    print(
        print_style + "Good bye! I wish you to survive in this beautiful world! See you next time!\n")
=======
    print(print_style + "Good bye! I wish you to survive in this beautiful world!" +\
                        " See you next time!\n")
>>>>>>> 5becf1ab98f34ff7938a219bdf1b6a9455942091
    print(print_style + 'C:\> exit\n**C:\>**\nC:> shutdown /r /t 0')

    print(Style.RESET_ALL)  # відновлення кольорів терміналу
    print("\033[0m")  # відновлення кольору в терміналі
