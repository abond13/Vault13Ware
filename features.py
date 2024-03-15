import func
from colorama import Fore, Back, Style
from colorama import just_fix_windows_console
import time, platform
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
    Відображення фічі СтартоваЗаставка - зробимо коли дійдуть руки.
    На мінімалках - друк привітання.
    '''
    print(Fore.GREEN + Back.BLACK + Style.BRIGHT + "\033[40m")  # чорний колір в терміналі
    print(Fore.GREEN + Back.BLACK + Style.BRIGHT + "\x1b[2J")  # clean the screen

    print(Fore.GREEN + Back.BLACK + Style.BRIGHT + "Welcome to Personal Information Processor PIP-Boy-Bot-3000!\n")
    func.hello()


def goodbye():
    '''
    Відображення фічі ФінальнаЗаставка - зробимо коли дійдуть руки.
    На мінімалках - друк прощання.
    '''
    print(Fore.GREEN + Back.BLACK + Style.BRIGHT + "Good bye! I wish you to survive in this beautiful world! See you next time!")
    print(Style.RESET_ALL)  # відновлення кольорів терміналу
    print("\033[0m")  # відновлення кольору в терміналі
