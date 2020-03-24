member_count = 0

class Member:
    def __init__(self, name):
        global member_count
        self.name = name
        self.member_id = member_count
        self.reservations = set()

        member_count += 1

    def __str__(self):
        return self.name + ' - Member ID: ' + str(self.member_id)

    def add_reservation(self, res):
        self.reservations.add(res)

    def get_reservations(self):
        reservations = []
        for r in self.reservations:
            reservations.append(str(r))

        return reservations

    def get_info(self):
        info = "Name: " + self.name + "\nMember ID: " + str(self.member_id)
        return info 

    def get_member_id(self):
        return self.member_id