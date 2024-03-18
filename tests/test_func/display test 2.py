from colorama import Fore, Back, Style
from colorama import just_fix_windows_console
import time

def display(today_style_string: str):

    just_fix_windows_console()
    print_style = Fore.GREEN + Back.BLACK + Style.BRIGHT

    print(print_style + "\033[40m")  # чорний колір в терміналі
    print(print_style + "\x1b[2J")  # очистка екрану термінал

    for char in today_style_string:
        print(print_style + char, end="", flush=True)
        time.sleep(0.04)

    print(Style.RESET_ALL) # відновлення кольорів терміналу
    print("\033[0m")  # відновлення кольору в терміналі

name = 'John'

display(f"Hello {name} vfvfdnvfnvfdkv vfdvfdv fd  f \n" +
        "vfdvfdvfdmvfdmvlfdm\n")