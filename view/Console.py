__author__ = 'Viktor'

import os
import time
from controller.controller import *
from peewee import *

db = SqliteDatabase('yachat_club.db')


def main_text():
    print('Press 1 for Member/Boat configuration \n'
          'Press 2 for List viewer \n'
          'Press \'q\' to exit program')
    text = raw_input()

    if text == '1':
        create()

    elif text == '2':
        member_boat_information()

    elif text == 'q':
        exit_console()


def create():
    while True:
        clear()
        print('Press 1 to add Member \n'
              'Press 2 to add Boat \n'
              'Press 3 to change Member information \n'
              'Press 4 to change Boat information \n'
              'Press 5 to delete Members \n'
              'Press 6 to delete Boat \n'
              'Press 7 to go back')
        text = raw_input()

        if text == '1':
            create_member()

        elif text == '2':
            create_boat()

        elif text == '3':
            change_member()

        elif text == '4':
            change_boat()

        elif text == '5':
            remove_member()

        elif text == '6':
            remove_boat()

        elif text == '7':
            main_text()


def lists():
    while True:
        clear()
        print('Press 1 for Compact list \n'
              'Press 2 for Verbose list \n'
              'Press 3 to go back')
        text = raw_input()


def create_member():
    while True:
        clear()
        name = raw_input('Enter mebers name: ')
        socialnumber = raw_input('Enter members socialnumber: ')
        add_member(name, socialnumber)
        create()


def create_boat():
    clear()
    owner = raw_input('Enter owners name: ')
    type = raw_input('Enter type of boat: ')
    length = raw_input('Enter length of boat: ')
    add_boat(owner, type, length)
    create()


def member_boat_information():
    clear()
    print('Press 1 to view member list: \n'
          'Press 2 to view boat list: \n')
    text = raw_input()

    if text == '1':
        member_list()

    elif text == '2':
        boat_list()


def member_list():
    clear()
    for i in get_member_list():
        print i


def boat_list():
    clear()


def remove_member():
    clear()


def remove_boat():
    clear()


def change_member():
    clear()
    name = raw_input('Enter new name: ')
    socialnumber = raw_input('Enter new socialnumber: ')
    create()


def change_boat():
    clear()
    owner = raw_input('Enter new owner: ')
    type = raw_input('Enter new type_ ')
    length = raw_input('Enter new length')
    update_boat(owner, type, length)
    create()


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
