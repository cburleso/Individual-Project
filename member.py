# running count of member instances 
member_count = 0

# represents a member of the gym, each instance contains a name (string), specific member ID,
# and a set of reservation instances 
class Member:
    def __init__(self, name):
        global member_count
        self.name = name
        self.member_id = member_count
        self.reservations = set()

        member_count += 1  # increment number of member instances 

    # overriden method to display member name and their ID when printing 
    def __str__(self):
        return self.name + ' - Member ID: ' + str(self.member_id)

    # adds a reservation instance to the members reservation set  
    def add_reservation(self, res):
        self.reservations.add(res)

    # returns a set of all reservations belonging to the member 
    def get_reservations(self):
        reservations = []
        for r in self.reservations:
            reservations.append(str(r)) # append __str__ representation (rather than memory address)

        return reservations

    # similar to overriden __str__, this method returns the name, member ID, and number of 
    # current reservations held by the gym member 
    def get_info(self):
        info = 'Name: ' + self.name + '\nMember ID: ' + str(self.member_id) \
            + '\nNumber of Reservations: ' + str(len(self.reservations))
        return info 

    # returns the unique member ID of the instance 
    def get_member_id(self):
        return self.member_id