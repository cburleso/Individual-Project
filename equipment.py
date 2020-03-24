class Equipment:
    def __init__(self, name, e_type):
        self.name = name
        self.type = e_type
        self.reserved = False

    def __str__(self):
        return self.name + ' (' + self.type + ')'

    def get_type(self):
        return self.type

    def get_name(self):
        return self.name

    def is_reserved(self):
        return self.reserved