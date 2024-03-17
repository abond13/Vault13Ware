from datetime import datetime
import time
import platform
from colorama import Fore, Back, Style
from colorama import just_fix_windows_console

if platform.system() == "Windows":
    import winsound


def display(today_style_string: str):
    '''
    old-computer-style printing function
    '''
    just_fix_windows_console()

    # os_type = platform.system()
    os_type = "notWindows"  # заглушка, бо зі звуком не працює нормально

    for char in today_style_string:
        print(char, end="", flush=True)
        if os_type == "Windows":
            winsound.Beep(840, 80)
            time.sleep(0.001)
        else:
            time.sleep(0.005)
    print('')

def greeting():
    '''
    Відображення фічі СтартоваЗаставка
    '''
    print(Fore.GREEN + Back.BLACK + Style.BRIGHT)
    display("\033[40m")  # чорний колір в терміналі
    display("\x1b[2J")  # clean the screen

    with open('splash_screen.txt', 'r') as file:
        display(file.read())

    print('\n\n\n')
    display("Welcome to Personal Information Processor PIP-Boy-Bot-3000!\n")
    display("VaultTec Personal computer Copyright(C) 1981, 1982, 1983, 1984" +\
                        " by VaultTec Corporation\n")
    display("640 K RAM\n")
    display("** CMOS]\n")
    display("Date / Time: **\n")
    display(f"{datetime.now().date()}\n")
    display(f"{datetime.now().time().strftime('%I:%M%p')}\n")
    display("** Type the name of the command interpreter: COMMAND.COM **")
    print('\n\n\n')




def goodbye():
    '''
    Відображення фічі ФінальнаЗаставка
    '''
    display("Good bye! I wish you to survive in this beautiful world!" +\
                        " See you next time!\n")
    display('C:\\> exit\n**C:\\>**\nC:> shutdown /r /t 0')

    print(Style.RESET_ALL)  # відновлення кольорів терміналу
    print("\033[0m")  # відновлення кольору в терміналі
