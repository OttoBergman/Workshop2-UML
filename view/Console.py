__author__ = 'Viktor'

import os
import time
import sys
pathname = os.path.dirname(sys.argv[0])
parent_dir_name = os.path.abspath(os.path.join(pathname, os.pardir))
sys.path.append(parent_dir_name)
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
    for count, member in enumerate(members):
        print member.name + ' ' + member.personalnumber + ' [' + str(count) + ']'

    member_nr = raw_input('Press the number adjacent to the member who should own the boat: ')
    if 0 <= int(member_nr) < len(members):
        owner = members[int(member_nr)]
        boat_types = get_boat_types()
        length = None
        for boat_type in boat_types:
            print str(boat_types.index(boat_type) + 1) + ' ' + boat_type
        boat_type_input = raw_input('Enter the number of what type of boat: ')
        if 1 <= int(boat_type_input) <= len(boat_types):
            while True:
                length = raw_input('Enter length of boat: ')
                try:
                    length = float(length)
                    if length == 0:
                        clear()
                        print 'Not a correct length'
                        continue
                    break
                except ValueError:
                    clear()
                    print 'Not a correct length'
            add_boat(owner, boat_types[int(boat_type_input) - 1], length)
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
          'Press 3 to view a specific members information: \n'
          'Press 4 to go back')
    text = raw_input()

    if text == '1':
        clear()
        member_lists()
    elif text == '2':
        clear()
        boat_list()
    elif text == '4':
        clear()
        main_text()
    elif text == '3':
        clear()
        specific_member_information()
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
    for count, member in enumerate(members):
        print member.name + ' ' + member.personalnumber + ' [' + str(count) + ']'

    nr = raw_input('Press the number adjacent to the member whom you want to delete: ')
    if 0 <= int(nr) < len(members):
        delete_member(members[int(nr)])
    else:
        clear()
        print 'Not a valid number!'
        print
        remove_member()

def remove_boat():
    members = get_member_list()
    for count, member in enumerate(members):
        print member.name + ' ' + member.personalnumber + ' [' + str(count) + ']'
    member_input = raw_input('Press the number adjacent to the member whom\'s boat you want to remove: ')
    if 0 <= int(member_input) < len(members):
        boats = get_boats_for_member(members[int(member_input)])
        for boat in boats:
            print str(boats.index(boat)) + ' ' + boat.type + ' ' + str(boat.boat_length)
        boat_input = raw_input('Press the number adjacent to the boat you want to delete: ')
        if 0 <= int(boat_input) < len(boats):
            delete_boat(boats[int(boat_input)])
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
    for count, member in enumerate(members):
        print member.name + ' ' + member.personalnumber + ' [' + str(count) + ']'

    nr = raw_input('Press the id-number adjacent to the member whom you want to change: ')
    if 0 <= int(nr) < len(members):
        name = raw_input('Enter new name: ')
        socialnumber = raw_input('Enter new socialnumber: ')

        update_member(members[(int(nr))], name, socialnumber)
        create()
    else:
        clear()
        print 'Not a valid number'
        print
        change_member()


def change_boat():
    boats = get_boat_list()
    length = None
    for boat in boats:
        print str(boats.index(boat)) + ' ' + boat.owner.name + ' ' + boat.type + ' ' + str(boat.boat_length)
    boat_input = raw_input('Press the number adjacent to the boat you want to change: ')
    if 0 <= int(boat_input) < len(boats):
        clear()
        members = get_member_list()
        for count, member in enumerate(members):
            print member.name + ' ' + member.personalnumber + ' [' + str(count) + ']'
        owner = raw_input('Press the number adjacent to the member who should own the boat: ')
        if 0 <= int(owner) < len(members):
            boat_types = get_boat_types()
            for boat_type in boat_types:
                print str(boat_types.index(boat_type)) + ' ' + boat_type
            boat_type = raw_input('Press the number adjacent to the type of boat: ')
            if 0 <= int(boat_type) < len(boat_types):
                while True:
                    length = raw_input('Enter length of boat: ')
                    try:
                        length = float(length)
                        if length == 0:
                            clear()
                            print 'Not a correct length'
                            continue
                        break
                    except ValueError:
                        clear()
                        print 'Not a correct length'
                update_boat(boats[int(boat_input)], members[int(owner)], boat_types[int(boat_type)], length)
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


def specific_member_information():
    name = raw_input('Enter members name: ')
    members = get_member_info(name)
    if len(members) > 0:
        clear()
        for member in members:
            print member.name + ' ' + member.personalnumber + ' [' + str(member.id) + ']'
            print
        member_boat_information()
    else:
        clear()
        print 'No member with that name was found.'
        print
        member_boat_information()

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
