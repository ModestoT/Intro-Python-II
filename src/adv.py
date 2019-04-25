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

items = {
    'sword': Item('Sword', 'Sharp blade allows the wielder to cut their foes cleanly.'),
    'apple': Item('Apple', 'An apple that the is able to be eaten. I wonder if it taste good?'),
    'gold': Item('Gold', 'Looks like this is a currency of some type.'),
    'shield': Item('Shield', 'A wooden shield that is great for blocking weak attacks')
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

# Add items to the rooms
room['outside'].addItem(items['sword'])
room['foyer'].addItem(items['apple'])
room['overlook'].addItem(items['shield'])
room['narrow'].addItem(items['apple'])
room['treasure'].addItem(items['gold'])
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Drol', room['outside'])
print(f'Welcome {player.name}!!\nYou are currently in the room: {player.current_room}\nHow would you like to proceed?')
user = input('Check available paths? Check for items in current room or Quit\n')
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
def changeRoom(direction, current_room):
    if direction == 'north':
        player.current_room = current_room.n_to
        
    elif direction == 'south':
        player.current_room = current_room.s_to
       
    elif direction == 'east':
        player.current_room = current_room.e_to

    elif direction == 'west':
        player.current_room = current_room.w_to

def getItem(item, room):
    if item: 
        player.addItem(items[f'{item}'])
        room.removeItem(items[f'{item}'])
        print(f'You added the {item} to your inventory!')
        print(player.inventory)

    
while not user == 'quit':
    if user == 'paths':
        paths = player.current_room.checkPaths()
        routes = player.current_room.paths
        if len(paths) == 1:
            print(f'\nLooks like we can only go {paths[0]}')
            print('What would you like to do now?')
            print(f'Go {paths[0]}? Check for items in current room or Quit')
            newInput = input('')
            if newInput != 'quit':
                changeRoom(newInput, player.current_room)
                print(f'\nYou are now in the {player.current_room}\nHow would you like to proceed?')
                user = input('Check avaiable paths? Check for items in current room or Quit\n')
            elif newInput == 'items':
                user = 'items'
            else:
                user = 'quit'
        else :
            print(f'\nLooks like we can go either {player.current_room.printPaths(paths)}')
            
            if len(paths) == 4:
                print(f'Go {paths[0]}? Go {paths[1]}? Go {paths[2]}? Go {paths[3]}? Check for items in current room or Quit')
                newInput = input('')

                if newInput != 'quit':
                    changeRoom(newInput, player.current_room)
                    print(f'\nYou are now in the {player.current_room}\nHow would you like to proceed?')
                    user = input('Check avaiable paths? Check for items in current room or Quit\n')
                elif newInput == 'items':
                    user = 'items'
                else:
                    user = 'quit'

            elif len(paths) == 3:
                print(f'Go {paths[0]}? Go {paths[1]}? Go {paths[2]}? Check for items in current room or Quit')
                newInput = input('')

                if newInput != 'quit':
                    changeRoom(newInput, player.current_room)
                    print(f'\nYou are now in the {player.current_room}\nHow would you like to proceed?')
                    user = input('Check avaiable paths? Check for items in current room or Quit\n')
                elif newInput == 'items':
                    user = 'items'
                else:
                    user = 'quit'

            elif len(paths) == 2:
                print(f'Go {paths[0]}? Go {paths[1]}? Check for items in current room or Quit')
                newInput = input('')

                if newInput != 'quit':
                    changeRoom(newInput, player.current_room)
                    print(f'\nYou are now in the {player.current_room}\nHow would you like to proceed?')
                    user = input('Check avaiable paths? Check for items in current room or Quit\n')
                elif newInput == 'items':
                    user = 'items'
                else:
                    user = 'quit'
        
    elif user == 'items':
        if len(player.current_room.items) == 0:
            print('There are no items in this room!')
            user = input('Check avaiable paths? Check for items in current room or Quit\n')
        else:
            items = player.current_room.getItems()
            print(f'Current items in the room:\n{items}') 
            newInput = input('Looks like theirs some items here, what would you like to do?\n')

            if newInput == 'quit':
                user = 'quit'
            else:
                getItem(newInput, player.current_room)
                user = input('What would you like to do next? Check the available paths? Check for more items? Or quit\n')
    else:
        print(user)
        print('Invalid input please try again.')
        break
    
    #print(f'{player.name}. You are in the {player.current_room} room. What would you like to do now?')
    #user = int(input('[1] Check available paths [2] Check for items in current room [5] Quit\n'))