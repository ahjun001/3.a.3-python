#!/usr/bin/env python
"""
 for each menu entry define:
 - a number to be that command in the menu or submenu
 - a string to indicate what the menu will do
 - a function to be executed when the command is entered
 each function shows a progression or suggest a default
 """
import os
import sys

# =======================
#     MENUS DISPLAY
# =======================


# Main menu
def menu_0_f():
    os.system('clear')

    print("Welcome,\n")
    print("Please choose the menu you want to start:")
    print("1. Menu 1")
    print("2. Menu 2")
    print("\n0. Quit")
    choice = input(" >>  ")
    exec_menu_f(choice, menu_0_dct)
    return


# Menu 1
def menu_0_1_f():
    print("Hello Menu 1 !\n")
    print("9. Back")
    print("0. Quit")
    choice = input(" >>  ")
    exec_menu_f(choice, menu_0_2_dct)
    return


# Menu 2
def menu_0_2_f():
    print("Hello Menu 2 !\n")
    print("9. Back")
    print("0. Quit")
    choice = input(" >>  ")
    exec_menu_f(choice, menu_0_2_dct)
    return


# =======================
#     MENUS FUNCTIONS
# =======================


# Back to main menu
def back_f():
    menu_0_dct['menu_display']()


# Exit program
def exit_f():
    sys.exit()


# Menu definition
menu_0_dct = {
    'menu_display': menu_0_f,
    '1': menu_0_1_f,
    '2': menu_0_2_f,
    '9': back_f,
    '0': exit_f,
}

menu_0_1_dct = {
    'Subtitle 1': menu_0_1_f,
    '9': back_f,
    '0': exit_f,
}

menu_0_2_dct = {
    'Subtitle 2': menu_0_2_f,
    '9': back_f,
    '0': exit_f,
}


# Execute menu
def exec_menu_f(choice, def_dct):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        def_dct['menu_display']()
    else:
        try:
            def_dct[ch]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            def_dct['menu_display']()
    return


# =======================
#      MAIN PROGRAM
# =======================
def main():
    menu_0_f()


# Main Program
if __name__ == "__main__":
    #  Launch main menu
    main()
