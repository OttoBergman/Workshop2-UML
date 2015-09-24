__author__ = 'otto'


class Member:

    name = ''
    personalnumber = ''
    id = None

    def __init__(self, name, personalnumber, id):
        self.name = name
        self.personalnumber = personalnumber
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_personalnumber(self):
        return self.personalnumber

    def set_personalnumber(self, personalnumber):
        self.personalnumber = personalnumber

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id