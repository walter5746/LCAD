class Location():

    def __init__(self, location, lzone):
        self.location = location
        self.lzone = lzone

    def __repr__(self):
        return "Location:%s Zone:%s" % (self.location, self.lzone)

    def lparser(self):
        if self.location[-1] == "H":
            self.lzone = 4
        elif self.location[-1].isdigit() == True and len(self.location) == 4:
            self.lzone = 5
        elif (self.location[-1] == "E" or "W") and (len(self.location) == 5):
            if int(self.location[0]) <= 2:
                self.lzone = 8
            else:
                self.lzone = 6
        elif self.location[-1] == "S":
            if int(self.location[0]) <= 2:
                self.lzone = 8
            else:
                self.lzone = 6
        elif self.location == "ED INTAKE":
            self.lzone = 2
        elif self.location[:2] == "ER":
            self.lzone = 3
        elif self.location[:3] == "TOW" or "GAR" or "LOT" or "EXT":
            self.lzone = 7


newL = Location("134S", None)
print(newL)
Location.lparser(newL)
print(newL)