"""To do:
-Ticket class
    -location parser method in Ticket class
    -make all input .upper()
    -print ticket method in Ticket class
-Front end
"""


class Roster():
    """
    uid = unit identifier, atick = what ticket they are currently assigned to.
    status: 0 = Unavailable, 1 = Stationary, 2 = One high priority call 3 = Break, 4 = On low priority call, 5 = Available.
    """
    def __init__(self, post, uid, zone, status, atick):
        self.post = post
        self.uid = uid
        self.zone = zone
        self.status = status
        self.atick = atick

    def roster_entry():
        r_list = []
        for i in source_list:
            i.uid = input("Please enter the unit identifier. Press enter for no officer. ")
            if i.uid == "":
                i.uid = None
        for i in source_list:
            if i.uid != None:
                r_list.append(i)
        return r_list

    def __repr__(self):
        return("Post:%s Officer:%s Zone:%s Status:%s Ticket:%s" % (self.post, self.uid, self.zone, self.status, self.atick))


#         post, uid, zone, status, atick
p1 = Roster(1, None, None, 0, None)
p2 = Roster(2, None, 2, 1, None)
p3 = Roster(3, None, 3, 1, None)
p4 = Roster(4, None, 4, 1, None)
p5 = Roster(5, None, 5, 5, None)
p6 = Roster(6, None, 6, 5, None)
p7 = Roster(7, None, 7, 5, None)
p8 = Roster(8, None, 8, 5, None)
p9 = Roster(9, None, 9, 1, None)
p10 = Roster(10, None, None, 1, None)
p11 = Roster(11, None, 11, 5, None)
p12 = Roster(12, None, 12, 5, None)

source_list = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]


class CallType():
    """
    call types that go into tickets
    ctype: this is where the abbreviated name goes ie "UAV"
    priority: 0-3 priority level. 0 = Low, 1 = Medium, 2 = High 3 = Emergency
    backup: how many officers need to get assigned to this call
    ftype: the full name of the call type from the call_dict dictionary
    """
    def __init__(self, ctype, priority, backup, ftype):
        self.ctype = ctype
        self.priority = priority
        self.backup = backup
        self.ftype = ftype

    def __repr__(self):
        return"Call Type:%s Priority:%s Backup Needed:%s Full Type:%s" % (self.ctype, self.priority, self.backup,
                                                                          self.ftype)


#              ctype, priority, backup, ftype
UAP = CallType("UAP", 3, 3, "Unit Assist: Patient Issues")
UAV = CallType("UAV", 2, 2, "Unit Assist: Visitor Issues")
ACC = CallType("ACC", 0, 1, "Access Door Request")

call_list = [UAP, UAV, ACC]