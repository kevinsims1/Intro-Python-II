from player import Player

class Room_item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"<{self.name}, {self.description}"


class Generic_Chair(Room_item):
    def __init__(self):
        super().__init__("Generic Chair", "Type 'Sit' to take a seat")
    
    def sit(self):
        print("You have taken a seat, type 'Stand' to stand and continue your journey!")
    
    def stand(self):
        print("You're Standing")

class Healing_Chair(Room_item):
    def __init__(self):
        super().__init__("Healing Chair", "Type 'Sit' to take a seat and heal")
    
    def sit(self):
        print("You have taken a seat you are now healed, type 'Stand' to stand and continue your journey!")
    
    def stand(self):
        print("You're Standing")
