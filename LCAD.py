class Roster(object):
    def __init__(self, post, id, status):
        self.post = post
        self.id = id
        self.status = status

    def assign_id(self, unit):
        self.unit[1] = input("Enter the identifier for post: ")
        return unit


p1 = Roster(1, None, None)
p2 = Roster(2, None, None)
p3 = Roster(3, None, None)
p4 = Roster(4, None, None)
p5 = Roster(5, None, None)
p6 = Roster(6, None, None)
p7 = Roster(7, None, None)
p8 = Roster(8, None, None)
p9 = Roster(9, None, None)
p10 = Roster(10, None, None)
p11 = Roster(11, None, None)
p12 = Roster(12, None, None)

r_list = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]

Roster.assign_id(p1)
print(p1.post)
