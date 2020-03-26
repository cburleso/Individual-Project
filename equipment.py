# represents a piece of equipment belonging to the gym, each instance contains a name
# (ie. 'Bench Press'), type (ie. 'Strength Training'), and boolean as to whether or not it is reserved
class Equipment:
    def __init__(self, name, e_type):
        self.name = name
        self.type = e_type
        self.reserved = False

    # overriden method to display the equipment name and its type in parenthesis when printing 
    def __str__(self):
        return self.name + ' (' + self.type + ')'

    # return the type of the equipment instance 
    def get_type(self):
        return self.type

    # return the name of the equipment instance 
    def get_name(self):
        return self.name

    # returns the instance boolean to depict whether the equipment is reserved or not 
    def is_reserved(self):
        return self.reserved