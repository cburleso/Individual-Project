import equipment
import member

class Reservation:
    def __init__(self, member, equipment, time):
        self.member = member
        self.equipment = equipment
        self.equipment.reserved = True
        self.time = time

    def __str__(self):
        return 'Member: ' + str(self.member) + ' - Equipment: '\
             + str(self.equipment) + ' - Time: ' + self.time

    def get_equipment(self):
        return self.equipment
    
    def get_member(self):
        return self.member

    def get_time(self):
        return self.time 