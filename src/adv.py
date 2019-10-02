from room import Room

from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

player1 = Player("kevin")

player_input = ""


while player_input.lower() != "exit":
    player_input=""
    for key, value in room.items():
        if key == player1.CurrentRoom:
            print(f'Current Room: {key}, Description: {value.description}')

    player_input = input("Please select a direction, 'N,S,E,W': ")

    if player_input == 'N' and player1.CurrentRoom == 'outside':
        player1.CurrentRoom = 'foyer'
        
    elif player_input == 'N' and player1.CurrentRoom == 'foyer':
        player1.CurrentRoom = 'overlook'
            
    elif player_input == 'N' and player1.CurrentRoom == 'narrow':
        player1.CurrentRoom = 'treasure'
    
    if player_input == 'S' and player1.CurrentRoom == 'foyer':
        player1.CurrentRoom = 'outside'
        
    elif player_input == 'S' and player1.CurrentRoom == 'overlook':
        player1.CurrentRoom = 'foyer'
            
    elif player_input == 'S' and player1.CurrentRoom == 'treasure':
        player1.CurrentRoom = 'narrow'

    if player_input == 'E' and player1.CurrentRoom == 'foyer':
        player1.CurrentRoom = 'narrow'
        
    if player_input == 'W' and player1.CurrentRoom == 'narrow':
        player1.CurrentRoom = 'foyer'