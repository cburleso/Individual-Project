import reservation
import member

class Gym:
    def __init__(self):
        self.members = set()
        self.equipment = set()
        self.reservations = set()

    def add_equipment(self, e):
        self.equipment.add(e)

    def add_member(self, m):
        self.members.add(m)

    def get_members(self):
        members = []
        for m in self.members:
            members.append(str(m))
        return members

    def get_equipment(self):
        equipment = []
        for e in self.equipment:
            equipment.append(str(e))
        return equipment

    def get_reservations(self):
        reservations = []
        for r in self.reservations:
            reservations.append(str(r))

        return reservations

    def make_reservation(self, m, e, t):
        if e.is_reserved():
            return None
        r = reservation.Reservation(m, e, t)
        self.reservations.add(r)
        m.add_reservation(r)
        return r 

    def get_available_equipment(self):
        available = []
        for e in self.equipment:
            if e.reserved == False:
                available.append(str(e))
            
        return available

    def unreserve(self, m, e):
        for r in self.reservations:
            if r.get_member() == m and r.get_equipment() == e:
                self.reservations.remove(r)
                m.reservations.remove(r)
                return True
        
        return False 

    def find_member(self, mem_id):
        for m in self.members:
            if m.get_member_id() == mem_id:
                return m.name
        
        return None 

