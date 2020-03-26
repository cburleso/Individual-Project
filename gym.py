import reservation

# represents the overall gym structure, containing a set of member, equipment, and reservation
# instances, encapsulating and abstracting individual instance methods and operations 
class Gym:
    def __init__(self):
        self.members = set()
        self.equipment = set()
        self.reservations = set()

    # adds an equipment instance to the gym 
    def add_equipment(self, e):
        self.equipment.add(e)

    # adds a member instance to the gym 
    def add_member(self, m):
        self.members.add(m)

    # returns a list of member instances belonging to the gym 
    def get_members(self):
        members = []
        for m in self.members:
            members.append(str(m)) # append __str__ representation (rather than memory address)
        return members

    # returns a list of equipment instances belonging to the gym 
    def get_equipment(self):
        equipment = []
        for e in self.equipment:
            equipment.append(str(e)) # append __str__ representation (rather than memory address)
        return equipment

    # returns a list of reservation instances belonging to the gym 
    def get_reservations(self):
        reservations = []
        for r in self.reservations:
            reservations.append(str(r))  # append __str__ representation (rather than memory address)

        return reservations

    # creates an equipment reservation belonging to a member instance within the gym 
    def make_reservation(self, m, e, t):
        if e.is_reserved():  # if the equipment is already reserved, return None 
            return None
        r = reservation.Reservation(m, e, t)  # otherwise, create a reservation instance and add such 
        # instance to the gym, as well as the members personal reservations list 
        self.reservations.add(r)
        m.add_reservation(r)
        return r 

    # returns a list of equipment instances belonging to the gym that are available to be reserved 
    def get_available_equipment(self):
        available = []
        for e in self.equipment:
            if e.reserved == False:  # append equipment instance if not reserved 
                available.append(str(e))
            
        return available

    # unreserves a specified piece of equipment reserved by a given member instance (returns True if successful,
    # False otherwise)
    def unreserve(self, m, e):
        for r in self.reservations:
            if r.get_member() == m and r.get_equipment() == e:  # if the equipment is reserved by the member,
                # remove the reservation from the gym set as well as the members personal reservation set 
                self.reservations.remove(r)
                m.reservations.remove(r)
                return True
        
        return False 

    # returns the name of the gym member instance provided a unique member ID, returns None if member doesn't exist
    def find_member(self, mem_id):
        for m in self.members:
            if m.get_member_id() == mem_id:
                return m.name
        
        return None 

