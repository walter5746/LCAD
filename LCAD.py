class Roster():
    def __init__(self, uid, status):
        self.uid = uid
        self.status = status

    def roster_entry():
        for i in r_list:
            i.uid = input("Please enter the unit identifier. Press enter for no officer. ")
            if i.uid == "":
                i.uid = None
            print(i, i.uid)

        print(r_list)

p1 = Roster(None, None)
p2 = Roster(None, None)
p3 = Roster(None, None)
p4 = Roster(None, None)
p5 = Roster(None, None)
p6 = Roster(None, None)
p7 = Roster(None, None)
p8 = Roster(None, None)
p9 = Roster(None, None)
p10 = Roster(None, None)
p11 = Roster(None, None)
p12 = Roster(None, None)

r_list = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]


Roster.roster_entry()