__author__ = 'Viktor'

import os
import time
import sys
pathname = os.path.dirname(sys.argv[0])
parent_dir_name = os.path.abspath(os.path.join(pathname, os.pardir))
sys.path.append(parent_dir_name)
print parent_dir_name
from controller.controller import *
from peewee import *

db = SqliteDatabase('yacht_club.db')

def main_text():
    print('Press 1 for Member/Boat configuration \n'
          'Press 2 for List viewer \n'
          'Press \'q\' to exit program')
    text = raw_input()

    if text == '1':
        create()

    elif text == '2':
        clear()
        member_boat_information()

    elif text == 'q':
        exit_console()

    else:
        clear()
        main_text()


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
            clear()
            create_boat()

        elif text == '3':
            clear()
            change_member()

        elif text == '4':
            clear()
            change_boat()

        elif text == '5':
            clear()
            remove_member()

        elif text == '6':
            clear()
            remove_boat()

        elif text == '7':
            clear()
            main_text()

        else:
            clear()
            create()


def member_lists():
    while True:
        print('Press 1 for Compact list \n'
              'Press 2 for Verbose list \n'
              'Press 3 to go back')
        text = raw_input()
        if text == '1':
            clear()
            compact_member_list()
        elif text == '2':
            clear()
            verbose_member_list()
        elif text == '3':
            clear()
            member_boat_information()
        else:
            clear()
            member_lists()


def create_member():
    while True:
        clear()
        name = raw_input('Enter mebers name: ')
        socialnumber = raw_input('Enter members socialnumber: ')
        add_member(name, socialnumber)
        create()


def create_boat():
    clear()
    members = get_member_list()
    for member in members:
        print member.name + ' ' + member.personalnumber + ' [' + str(member.id) + ']'

    member_id = raw_input('Press the number adjacent to the member who should own the boat: ')
    if 1 <= int(member_id) <= len(members):
        owner = members[int(member_id) - 1]
        boat_types = get_boat_types()
        for boat_type in boat_types:
            print str(boat_types.index(boat_type) + 1) + ' ' + boat_type
        boat_type_input = raw_input('Enter the number of what type of boat: ')
        if 1 <= int(boat_type_input) <= len(boat_types):
            length = raw_input('Enter length of boat: ')
            add_boat(owner, boat_types[int(boat_type_input)], length)
            create()
        else:
            clear()
            print 'Not a valid type index'
            print
            create_boat()
    else:
            clear()
            print 'Not a valid member index'
            print
            create_boat()


def member_boat_information():
    print('Press 1 to view member list: \n'
          'Press 2 to view boat list: \n'
          'Press 3 to go back')
    text = raw_input()

    if text == '1':
        clear()
        member_lists()
    elif text == '2':
        clear()
        boat_list()
    elif text == '3':
        clear()
        main_text()
    else:
        clear()
        member_boat_information()

def compact_member_list():
    clear()
    for member in get_member_list():
        boats = get_boats_for_member(member)
        print member.name + ' ' + str(member.id) + ' ' + str(len(boats))
        print
    member_lists()

def verbose_member_list():
    clear()
    for member in get_member_list():
        boats = get_boats_for_member(member)
        print member.name + ' ' + member.personalnumber + ' ' + str(member.id)
        if boats:
            print 'Boats:'
            for boat in boats:
                print boat.type + ' ' + str(boat.boat_length)
        print ''
    member_lists()

def boat_list():
    clear()
    for boat in get_boat_list():
        print 'Owner: ' + boat.owner.name + ' ' + boat.type + ' ' + str(boat.boat_length)
        print
    member_boat_information()


def remove_member():
    members = get_member_list()
    for member in members:
        print member.name + ' ' + member.personalnumber + ' [' + str(member.id) + ']'

    id_nr = raw_input('Press the number adjacent to the member whom you want to delete: ')
    if 0 <= int(id_nr) <= len(members):
        members[int(id_nr) - 1].delete_instance()
    else:
        clear()
        print 'Not a valid number!'
        print
        remove_member()

def remove_boat():
    members = get_member_list()
    for member in members:
        print member.name + ' ' + member.personalnumber + ' [' + str(member.id) + ']'
    member_input = raw_input('Press the number adjacent to the member whom\'s boat you want to remove: ')
    if 0 <= int(member_input) <= len(members):
        boats = get_boats_for_member(members[int(member_input) - 1])
        for boat in boats:
            print str(boats.index(boat) + 1) + ' ' + boat.type + ' ' + str(boat.boat_length)
        boat_input = raw_input('Press the number adjacent to the boat you want to delete: ')
        if 0 <= int(boat_input) - 1 <= len(boats):
            boats[int(boat_input) - 1].delete_instance()
        else:
            clear()
            print 'Not a valid boat index'
            print
            remove_boat()
    else:
        clear()
        print 'Not a valid member index'
        print
        remove_boat()


def change_member():
    members = get_member_list()
    for member in members:
        print member.name + ' ' + member.personalnumber + ' [' + str(member.id) + ']'

    id_nr = raw_input('Press the id-number adjacent to the member whom you want to change: ')
    if 1 <= int(id_nr) <= len(members):
        name = raw_input('Enter new name: ')
        socialnumber = raw_input('Enter new socialnumber: ')

        update_member(members[(int(id_nr) - 1)], name, socialnumber)
        create()
    else:
        clear()
        print 'Not a valid member id'
        print
        change_member()


def change_boat():
    boats = get_boat_list()
    for boat in boats:
        print str(boats.index(boat) + 1) + ' ' + boat.owner.name + ' ' + boat.type + ' ' + str(boat.boat_length)
    boat_input = raw_input('Press the number adjacent to the boat you want to change: ')
    if 1 <= int(boat_input) <= len(boats):
        clear()
        members = get_member_list()
        for member in members:
            print member.name + ' ' + member.personalnumber + ' [' + str(member.id) + ']'
        owner = raw_input('Press the number adjacent to the member who should own the boat: ')
        if 1 <= int(owner) <= len(members):
            boat_types = get_boat_types()
            for boat_type in boat_types:
                print str(boat_types.index(boat_type)) + ' ' + boat_type
            boat_type = raw_input('Press the number adjacent to the type of boat: ')
            if 1 <= int(boat_type) <= len(boat_types):
                length = raw_input('Enter new length: ')
                update_boat(boats[int(boat_input) - 1], owner, boat_type, length)
                create()
            else:
                clear()
                print 'Not a valid type index'
                print
                change_boat()
        else:
            clear()
            print 'Not a valid member index'
            print
            change_boat()
    else:
        clear()
        print 'Not a valid boat index'
        print
        change_boat()


def exit_console():
    clear()

    print('Goodbye!')
    time.sleep(2)
    close_database()
    exit(0)


if __name__ == '__main__':

    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')


    while True:
        main_text()
