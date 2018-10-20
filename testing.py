class Location():

    def __init__(self, location, lzone):
        self.location = location
        self.lzone = lzone

    def lparser(self):
        if self int([0]) <= 2:
            self = 8
        if self.location[0] > 2:
            self.lzone = 6
        if isnumber(self.location[-1]):
            self.lzone = 5

Location.lparser(2432)
