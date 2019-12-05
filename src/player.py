# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name='Player', CurrentRoom='outside', health=90,):
        self.name = name
        self.CurrentRoom = CurrentRoom 
        #Add Ons
        self.health = health

    def heal(self):
        self.health += 10
        print(self.health)