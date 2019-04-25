import random

from room import Room
from player import Player
from item import Item
from monster import Monster
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

monsters = {
    'goblin' : Monster('Goblin', 5, 2, 10),
    'orc': Monster('Orc', 10, 10, 20),
    'wolf': Monster('Wolf', 10, 10, 10),
    'snake': Monster('Snake', 2, 2, 2)
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

# Add monters to rooms

for i, r in room.items():
    for k, m in monsters.items():
        ran_num = random.randint(1,100)
        if ran_num > 80:
            r.monsters.append(monsters['goblin'])
        elif ran_num > 50:
            r.monsters.append(monsters['orc'])
        elif ran_num > 30:
            r.monsters.append(monsters['wolf'])
        else:
            r.monsters.append(monsters['snake'])

#
# Main
#
def changeRoom(direction, current_room):
    if direction.lower() == 'north':
        if current_room.n_to == '':
            print('Invalid direction, please try again. Or type help')
            return userInput[0] == 'paths'
        else:
            player.current_room = current_room.n_to
        
    elif direction.lower() == 'south':
        if current_room.s_to == '':
            print('Invalid direction, please try again. Or type help')
            return userInput[0] == 'paths'
        else:
            player.current_room = current_room.s_to
       
    elif direction.lower() == 'east':
        if current_room.e_to == '':
            print('Invalid direction, please try again. Or type help')
            return userInput[0] == 'paths'
        else:
            player.current_room = current_room.e_to

    elif direction.lower() == 'west':
        if current_room.w_to == '':
            print('Invalid direction, please try again. Or type help')
            return userInput[0] == 'paths'
        else:
            player.current_room = current_room.w_to
    else:
        print('Invalid direction, please try again. Or type help')
        return userInput[0] == 'paths'

def getItem(item, room):
    if item: 
        player.addItem(items[f'{item.lower()}'])
        room.removeItem(items[f'{item.lower()}'])
    else: 
        print('That item does not exist')

def dropItem(item, room):
    isItem = player.removeItem(items[f'{item.lower()}'])
    if isItem != False:
        room.addItem(items[f'{item.lower()}'])
        
def userInputField():
    user = input('Check available paths? Check for items in current room or Quit\n')
    userInputText = lowerCaseString(user.split())

    return userInputText

def lowerCaseString(string):
    for i, s in enumerate(string):
        string[i] = s.lower()
    return string

# Make a new player object that is currently in the 'outside' room.
player = Player('Drol', room['outside'])
print(f'Welcome {player.name}!!\nYou are currently in the room: {player.current_room}\nThere are {len(player.current_room.monsters)} Monsters here. How would you like to proceed?')
userInput = userInputField()

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

while not userInput[0] == 'quit':
    if userInput[0] == 'paths' or userInput[0] == 'check' and userInput[1] == 'paths':
        paths = player.current_room.checkPaths()
        routes = player.current_room.paths
        if len(paths) == 1:
            print(f'\nLooks like we can only go {paths[0]}')
            print('What would you like to do now?')
            print(f'Go {paths[0]}? Check for items in current room or Quit')
            newInput = input('')
            inputString = lowerCaseString(newInput.split())

            if len(inputString) == 2:
                if inputString[0] == 'go':
                    changeRoom(inputString[1], player.current_room)
                    print(f'\nYou are now in the {player.current_room}\nHow would you like to proceed?')
                    userInput = userInputField()
                elif inputString[0] == 'check' and inputString[1] == 'items':
                    userInput[0] == 'items'
                elif inputString[0] == 'drop':
                    userInput = inputString
                else:
                    print('Invalid command, please try again. Or type help')
                    userInput[0] == 'paths'

            else:
                if inputString[0] == 'items':
                    userInput[0] = 'items'
                elif inputString[0] == 'quit':
                    userInput[0] = 'quit'
                else:
                    changeRoom(inputString[0], player.current_room)
                    print(f'\nYou are now in the {player.current_room}\nHow would you like to proceed?')
                    userInput = userInputField()

        else :
            print(f'\nLooks like we can go either {player.current_room.printPaths(paths)}')
            
            if len(paths) == 4:
                print(f'Go {paths[0]}? Go {paths[1]}? Go {paths[2]}? Go {paths[3]}? Check for items in current room or Quit')
                newInput = input('')
                inputString = lowerCaseString(newInput.split())

                if len(inputString) == 2:
                    if inputString[0] == 'go':
                        changeRoom(inputString[1], player.current_room)
                        print(f'\nYou are now in the {player.current_room}\nHow would you like to proceed?')
                        userInput = userInputField()
                    elif inputString[0] == 'check' and inputString[1] == 'items':
                        userInput[0] == 'items'
                    elif inputString[0] == 'drop':
                        userInput = inputString
                    else:
                        print('Invalid command, please try again. Or type help')
                        userInput[0] == 'paths'

                else:
                    if inputString[0] == 'items':
                        userInput[0] = 'items'
                    elif inputString[0] == 'quit':
                        userInput[0] = 'quit'
                    else:
                        changeRoom(inputString[0], player.current_room)
                        print(f'\nYou are now in the {player.current_room}\nHow would you like to proceed?')
                        userInput = userInputField()

            elif len(paths) == 3:
                print(f'Go {paths[0]}? Go {paths[1]}? Go {paths[2]}? Check for items in current room or Quit')
                newInput = input('')
                inputString = lowerCaseString(newInput.split())

                if len(inputString) == 2:
                    if inputString[0] == 'go':
                        changeRoom(inputString[1], player.current_room)
                        print(f'\nYou are now in the {player.current_room}\nHow would you like to proceed?')
                        userInput = userInputField()
                    elif inputString[0] == 'check' and inputString[1] == 'items':
                        userInput[0] == 'items'
                    elif inputString[0] == 'drop':
                        userInput = inputString
                    else:
                        print('Invalid command, please try again. Or type help')
                        userInput[0] == 'paths'

                else:
                    if inputString[0] == 'items':
                        userInput[0] = 'items'
                    elif inputString[0] == 'quit':
                        userInput[0] = 'quit'
                    else:
                        changeRoom(inputString[0], player.current_room)
                        print(f'\nYou are now in the {player.current_room}\nHow would you like to proceed?')
                        userInput = userInputField()

            elif len(paths) == 2:
                print(f'Go {paths[0]}? Go {paths[1]}? Check for items in current room or Quit')
                newInput = input('')
                inputString = lowerCaseString(newInput.split())

                if len(inputString) == 2:
                    if inputString[0] == 'go':
                        changeRoom(inputString[1], player.current_room)
                        print(f'\nYou are now in the {player.current_room}\nHow would you like to proceed?')
                        userInput = userInputField()
                    elif inputString[0] == 'check' and inputString[1] == 'items':
                        userInput[0] == 'items'
                    elif inputString[0] == 'drop':
                        userInput = inputString
                    else:
                        print('Invalid command, please try again. Or type help')
                        userInput[0] == 'paths'

                else:
                    if inputString[0] == 'items':
                        userInput[0] = 'items'
                    elif inputString[0] == 'quit':
                        userInput[0] = 'quit'
                    else:
                        changeRoom(inputString[0], player.current_room)
                        print(f'\nYou are now in the {player.current_room}\nHow would you like to proceed?')
                        userInput = userInputField()
        
    elif userInput[0] == 'items' or userInput[0] == 'check' and userInput[1] == 'items':
        if len(player.current_room.items) == 0:
            print('There are no items in this room!')
            userInput = userInputField()
        else:
            room_items = player.current_room.getItems()
            print(f'Current items in the room:\n{room_items}') 
            newInput = input('Looks like theirs some items here, what would you like to do?\n')
            inputString = lowerCaseString(newInput.split())

            if len(inputString) == 2 and inputString[0] == 'get' or inputString[0] == 'take':
                getItem(inputString[1], player.current_room)
                userInput = userInputField()
            elif inputString[0] == 'drop':
                userInput = inputString
            elif inputString[0] == 'quit':
                userInput[0] = 'quit'
            else: 
                print('Command not recognized, please try again')
                userInput[0] = 'items'

    elif userInput[0] == 'inventory' or userInput[0] == 'check' and userInput[1] == 'inventory':
        print(f'Current inventory:\n{player.getInventory()}')
        userInput = userInputField()

    elif userInput[0] == 'drop':
        dropItem(userInput[1], player.current_room)
        userInput = userInputField()

    elif userInput[0] == 'help':
        print('Some command examples you can do are:\ncheck paths\ncheck items\ncheck inventory or inventory\ngo (some direction)')
        userInput = userInputField()

    else:
        print('Invalid input please try again.')
        userInput = userInputField()
    #print(f'{player.name}. You are in the {player.current_room} room. What would you like to do now?')
    #user = int(input('[1] Check available paths [2] Check for items in current room [5] Quit\n'))