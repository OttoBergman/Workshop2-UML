__author__ = 'Viktor'
from peewee import *
from model.Member import Member

db = SqliteDatabase('yacht_club.db')

class Boat(Model):
    owner = ForeignKeyField(Member, related_name='boats')
    type = CharField()
    boat_length = FloatField()

    class Meta:
        database = db  # This model uses the "yacht_club.db" database.



