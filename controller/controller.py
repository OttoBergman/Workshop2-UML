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


def add_boat(owner, type, boat_length):
    boat = Boat.create(owner=owner, type=type, boat_length=boat_length)
    return boat


def delete_boat(boat):
    boat.delete_instance()


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

