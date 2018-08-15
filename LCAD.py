class Roster():
    """
    uid = unit identifier, atick = what ticket they are currently assigned to.
    status: 0 = Unavailable, 1 = Stationary, 2 = One high priority call 3 = Break, 4 = On low priority call,
    5 = Available.
    """
    def __init__(self, post, uid, zone, status, atick):
        self.post = post
        self.uid = uid
        self.zone = zone
        self.status = status
        self. atick = atick

    def roster_entry():
        for i in r_list:
            i.uid = input("Please enter the unit identifier. Press enter for no officer. ")
            if i.uid == "":
                i.uid = None
            print(i, i.uid)

        print(r_list)

#        post, uid, zone, status, atick
p1 = Roster(1, None, None, 0, None)
p2 = Roster(2, None, None, 0, None)
p3 = Roster(3, None, None, 0, None)
p4 = Roster(4, None, None, 0, None)
p5 = Roster(5, None, None, 0, None)
p6 = Roster(6, None, None, 0, None)
p7 = Roster(7, None, None, 0, None)
p8 = Roster(8, None, None, 0, None)
p9 = Roster(9, None, None, 0, None)
p10 = Roster(10, None, None, 0, None)
p11 = Roster(11, None, None, 0, None)
p12 = Roster(12, None, None, 0, None)

r_list = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]


Roster.roster_entry()
