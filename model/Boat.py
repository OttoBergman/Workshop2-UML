__author__ = 'Viktor'

class Boat:

    type = ''
    length = 0.0

    def __init__(self, sailboat, motorsailer, kayak, canoe, other):
        self.sailboat = sailboat
        self.motorsailer = motorsailer
        self.kayak = kayak
        self.canoe = canoe
        self.other = other

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_length(self):
        return self.length

    def set_length(self, length):
        self.length = length



