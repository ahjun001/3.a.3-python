#!/usr/bin/env python3
""" 
Example of simple User Interface to run in bash
From Jack Diederich Youtube video 'Stop writing classes'
Classes are great but they are also overused.  
Refactor the unnecessary classes, exceptions, and modules out of them.
 """
import sys


class Menu:
    """Display a menu and respond to choices when run."""

    def __init__(self):
        self.menus = {
            "main_menu": {
                "1": self.submenu_1,
                "2": self.submenu_2,
                "0": self.quit
            },
            "submenu_1": {
                "7": self.back,
                "8": self.quit
            },
            "submenu_2": {
                "9": self.back,
                "0": self.quit
            }
        }
        self.menu = 'main_menu'

    def run(self):
        while True:
            # display menu with data from menus dict
            for k, v in self.menus.get(self.menu).items():
                print(f'{k}. {v.__name__}')
            choice = input("Enter an option: ")
            action = self.menus[self.menu].get(choice)
            if action:
                action()
            else:
                print(f'{choice} is not a valid choice')

    def submenu_1(self):
        self.menu = 'submenu_1'
        print('Performing submenu 1 actions ...')

    def submenu_2(self):
        self.menu = 'submenu_2'
        print('Performing submenu 2 actions ...')

    def back(self):
        self.menu = 'main_menu'
        print('Returning to main menu ...')

    @staticmethod
    def quit():
        print('Exiting program ...')
        sys.exit(0)


def main():
    """ Driver """
    m = Menu()
    m.run()


if __name__ == '__main__':
    main()