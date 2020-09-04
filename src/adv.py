from room import Room
from player import Player
from item import Item
import textwrap

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

    'secret': Room("Secret Hideout", """A shadowy corner of the treasure
room had a small crevace that led to this enormous hidden
chamber! At the end of the long rows of mable columns is a
table with a key. There appear to be no other exits besides
the one you entered from.""")
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
room['treasure'].n_to = room['secret']
room['secret'].s_to = room['treasure']

# Add items to rooms

room['foyer'].items.append(Item('key', 'This rusted tool surely belongs to a nearby lock'))
room['foyer'].items.append(Item('stone', 'A solitary brick that appears to have fallen out of the wall'))
room['overlook'].items.append(Item('ring', 'A simple bronze band, seemingly forgotten by its previous owner'))

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

quitGame = False
moveError = 'Cannot move that way\n'
invalidAction = 'Input not recognized as an action\n'
player1 = Player('Daniel', room['outside'])

while not quitGame:
    print(f'Location: {player1.current_room.name}')
    print(textwrap.fill(f'Description: {player1.current_room.description}\n', 70))
    action = input('Choose an action: ')

    #player action is a single letter
    if len(action) == 1:
        #move north
        if(action == 'n'):
            if player1.current_room.n_to:
                print(f'Moving North to {player1.current_room.n_to.name}\n')
                player1.current_room = player1.current_room.n_to
            else: 
                print(moveError)
        #move south
        elif(action == 's'):
            if player1.current_room.s_to:
                print(f'Moving South to {player1.current_room.s_to.name}\n')
                player1.current_room = player1.current_room.s_to
            else:
                print(moveError)
        #move east
        elif(action == 'e'):
            if player1.current_room.e_to:
                print(f'Moving East to {player1.current_room.e_to.name}\n')
                player1.current_room = player1.current_room.e_to
            else:
                print(moveError)
        #move west
        elif(action == 'w'):
            if player1.current_room.w_to:
                print(f'Moving West to {player1.current_room.w_to.name}\n')
                player1.current_room = player1.current_room.w_to
            else:
                print(moveError)
        #quit game
        elif(action == 'q'):
            print('Quitting Game...')
            quitGame = True
        #print inventory
        elif(action == 'i'):
            print('Inventory:')
            if len(player1.inventory) == 0:
                print('Empty')
            else:
                for item in player1.inventory:
                    print(f'{item.name}: {item.description}')
            print('\n')
        #invalid action input
        else:
            print(invalidAction)

    #player input is more verb noun
    elif(len(action.split()) == 2):
        verb, noun = action.split()
        #take item
        if(verb == 'get' or verb == 'take'):
            matchingItems = [item for item in player1.current_room.items if item.name == noun]
            if len(matchingItems) == 1:
                matchingItems[0].on_take()
                player1.inventory.append(matchingItems[0])
                player1.current_room.items.remove(matchingItems[0])
            else:
                print(f'Item {noun} not found\n')
        #drop item
        elif(verb == 'drop'):
            matchingItems = [item for item in player1.inventory if item.name == noun]
            if len(matchingItems) == 1:
                matchingItems[0].on_drop()
                player1.current_room.items.append(matchingItems[0])
                player1.inventory.remove(matchingItems[0])
            else:
                print(f'Item {noun} not found\n')
        else:
            print(invalidAction)
    else:
        print('Actions should be either 1 letter or a verb and a noun\n')


