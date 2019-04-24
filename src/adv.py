from room import Room
from player import Player
from item import Item
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
player = Player('Drol', room['outside'])
print(f'Welcome {player.name}!!\nYou are currently in the room: {player.current_room.name}\nHow would you like to proceed?')
user = int(input('[1] Check available paths [2] Check for items in current room [6] Quit\n'))
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

while not user == 6:
    if user == 1:
        paths = player.current_room.checkPaths()

        if len(paths) == 1:
            print(f'Looks like we can only go {paths[0]}')
            print('What would you like to do now?')
            newInput = int(input(f'[1] Go {paths[0]}? [2] Check for items in current room [6] Quit\n'))
            
            if newInput == 1:
                player.current_room = player.current_room.paths[0][paths[0]]
                print(f'You are now in the {player.current_room.name}\nHow would you like to proceed?')
                user = int(input('[1] Check avaiable paths? [2] Check for items in current room [6] Quit\n'))
            elif newInput == 6:
                user = 6
        else :
            print(f'Looks like we can go either {player.current_room.printPaths(paths)}')
            
            if len(paths) == 4:
                print(paths)
                newInput = int(input(f'[1] Go {paths[0]}? [2] Go {paths[1]}? [3] Go {paths[2]}? [4] Go {paths[3]}? [5] Check for items in current room [6] Quit\n'))
                
                if newInput < 5:
                    player.current_room = player.current_room.getPaths()[newInput-1]
                    print(f'You are now in the {player.current_room.name}\nHow would you like to proceed?')
                    user = int(input('[1] Check avaiable paths? [2] Check for items in current room [6] Quit\n'))
                elif newInput == 6:
                    user = 6

            elif len(paths) == 3:
                newInput = int(input(f'[1] Go {paths[0]}? [2] Go {paths[1]}? [3] Go {paths[2]}? [4] Check for items in current room [6] Quit\n'))
                
                if newInput < 5:
                    player.current_room = player.current_room.getPaths()[newInput-1]
                    print(f'You are now in the {player.current_room.name}\nHow would you like to proceed?')
                    user = int(input('[1] Check avaiable paths? [2] Check for items in current room [6] Quit\n'))
                elif newInput == 6:
                    user = 6

            elif len(paths) == 2:
                newInput = int(input(f'[1] Go {paths[0]}? [2] Go {paths[1]}? [3] Check for items in current room [6] Quit\n'))
                
                if newInput < 5:
                    player.current_room = player.current_room.getPaths()[newInput-1]
                    print(f'You are now in the {player.current_room.name}\nHow would you like to proceed?')
                    user = int(input('[1] Check avaiable paths? [2] Check for items in current room [6] Quit\n'))
                elif newInput == 6:
                    user = 6
        
    elif user == 2:
        print(f'Current items in the room:\n{player.current_room.items}') 

    else:
        print('Invalid input please try again.')
    
    #print(f'{player.name}. You are in the {player.current_room} room. What would you like to do now?')
    #user = int(input('[1] Check available paths [2] Check for items in current room [5] Quit\n'))