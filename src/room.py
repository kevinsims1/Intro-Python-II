# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, chair=None):
        self.name = name
        self.description = description
        #items
        self.chair = chair
        #directions
        self.n_to = None
        self.w_to = None
        self.e_to = None
        self.s_to = None
        
    # This is for dev use only
#Room: {self.name}, description: {self.description}, 

    def __str__(self):
        return f"<Items: {self.chair}"
