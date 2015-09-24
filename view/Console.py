__author__ = 'Viktor'

import os
import time


def main_text():
    print('Press 1 for Member/Boat configuration \n'
          'Press 2 for List viewer \n'
          'Press \'q\' to exit program')
    text = raw_input()

    if text == '1':
        create()

    elif text == '2':
        lists()

    elif text == 'q':
        exit_console()


def create():
    while True:
        clear()
        print('Press 1 to add Member \n'
              'Press 2 to add Boat \n'
              'Press 3 to change Member/Boat information \n'
              'Press 4 to delete Members \n'
              'Press 5 to delete boat \n'
              'Press 6 to go back')
        text = raw_input()


def lists():
    while True:
        clear()
        print('Press 1 for Compact list \n'
              'Press 2 for Verbose list \n'
              'Press 3 to go back')
        text = raw_input()


def add_member():
    while True:
        clear()
        name = raw_input('Enter members name:')
        personalnumber = raw_input('Enter members personalnumber')
        id = raw_input('Enter members id')
        text = raw_input()


def add_boat():
    clear()


def member_boat_information():
    clear()


def delete_member():
    clear()


def delete_boat():
    clear()


def exit_console():
    clear()

    text = raw_input()
    print('Goodbye!')
    time.sleep(2)
    exit(0)


if __name__ == '__main__':

    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')


    while (True):
        main_text()
