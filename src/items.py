class Room_item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"<{self.name}, {self.description}"

    # def sit(self):
    #     if player_input == "Sit":
    #         return "Player is sitting"


class Generic_Chair(Room_item):
    def __init__(self):
        super().__init__("Chair", "Chair")
