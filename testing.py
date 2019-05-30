class Ticket(Roster, CallType, Location):
    def __init___(self, cadnum, tuid, tstatus, tctype, tftype, tlocation, tlzone):
        self.cadnum = cadnum
        super().__init__(uid, status, atick, ctype, ftype, location, lzone)

tic1 = (1, None, None, None, None, None, None)
tic1 = (2, None, None, None, None, None, None)
tic3 = (3, None, None, None, None, None, None)