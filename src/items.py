class Room_items():
    def __init__(self):
        self.name = "Chair"
        self.description = "Black Rocking Chair"

    def __str__(self):
        return f"<{self.name}, {self.description}"

    # def sit(self):
    #     if player_input == "Sit":
    #         return "Player is sitting"
        