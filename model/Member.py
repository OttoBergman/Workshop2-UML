__author__ = 'otto'
from peewee import *

db = SqliteDatabase('yacht_club.db')


class Member(Model):
    name = CharField()
    personalnumber = CharField()

    class Meta:
        database = db  # This model uses the "yacht_club.db" database.
