import equipment
import member

# represents an equipment reservation made by a user of the gym, each instance contains a reservation owner
# (member instance), an equipment instance, and a reservation time set by the member 
class Reservation:
    def __init__(self, member, equipment, time):
        self.member = member
        self.equipment = equipment
        self.equipment.reserved = True  # when a reservation is made with this equipment, set it to reserved 
        self.time = time

    # overriden method to display reservation owner (member), the equipment reserved, and the reservation time
    # when printing  
    def __str__(self):
        return 'Member: ' + str(self.member) + ' - Equipment: '\
             + str(self.equipment) + ' - Time: ' + self.time

    # returns the equipment instance belonging to the reservation
    def get_equipment(self):
        return self.equipment
    
    # returns the owner / member instance of the reservation 
    def get_member(self):
        return self.member

    # returns the specified reservation time 
    def get_time(self):
        return self.time 