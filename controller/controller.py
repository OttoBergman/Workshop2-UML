__author__ = 'otto'
from peewee import *
from model.Member import Member
from model.Boat import Boat

db = SqliteDatabase('yacht_club.db')

db.connect()

db.create_tables([Member, Boat], True)

def add_member(name, personalnr):
    member = Member.create(name=name, personalnumber=personalnr)
    return member

def delete_member(member):
    member.delete_instance()


def update_member(member, name, personalnr):
    member.name = name
    member.personalnumber = personalnr
    member.save()


def add_boat(owner, type, boat_length):
    boat = Boat.create(owner=owner, type=type, boat_length=boat_length)
    return boat


def delete_boat(boat):
    boat.delete_instance()


def update_boat(boat, owner, type, boat_length):
    boat.owner = owner
    boat.type = type
    boat.boat_length = boat_length
    boat.save()


def get_member_list():
    members = []
    for member in Member.select().order_by(Member.name):
        members.append(member)
    return members

def get_boat_list():
    boats = []
    for boat in Boat.select().join(Member):
        boats.append(boat)
    return boats