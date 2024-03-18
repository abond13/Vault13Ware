from colorama import Fore, Back, Style
from colorama import just_fix_windows_console
import time, platform
if platform.system() == "Windows":
    import winsound


def display(today_style_string: str):

    just_fix_windows_console()
    print_style = Fore.GREEN + Back.BLACK + Style.BRIGHT

    print(print_style + "\033[40m")  # чорний колір в терміналі
    print(print_style + "\x1b[2J")  # очистка екрану термінала

    os_type = platform.system()

    for char in today_style_string:
        print(print_style + char, end="", flush=True)
        if os_type == "Windows":
            winsound.Beep(840, 80)
            time.sleep(0.001)
        else:
            time.sleep(0.04)

    print(Style.RESET_ALL) # відновлення кольорів терміналу
    print("\033[0m")  # відновлення кольору в терміналі

name = 'John'

display(f"Hello {name} vfvfdnvfnvfdkv vfdvfdv fd  f \n" +
        "vfdvfdvfdmvfdmvlfdm\n")

