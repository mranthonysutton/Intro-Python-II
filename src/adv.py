from room import Room
from player import Player
from item import Item

import os

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     Item("axe", """Used to chop wood. Mostly...""")),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", Item("coin", """You find
    a coin that has been left behind.""")),
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

player = Player(input("What is your name? "), room['outside'])
os.system("clear")

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

print("Welcome to the adventure game. ")
print("You must navigate to where you would like to go.\n")
print(player)
print(player.current_room.description + "\n")
print("Command Table\n" + "=" * 30)
print("Travel: (n) North (e) East (s) South (w) West")
print("""Player: (i) Inventory (l) Locate items (get) Items
        (drop) Items (q) quit""")
print("\nWhat would you like to do?")

while True:

    player_input = input("> ")

    # Sets the available directions for the user
    acceptable_travel_directions = ['n', 'e', 's', 'w']
    acceptable_player_actions = ['i', 'inventory']
    current_room = player.current_room

    print()
    print("=" * 20 + "\n")

    if player_input.lower() in acceptable_travel_directions:
        player.move(player_input)
    elif player_input.lower() in acceptable_player_actions:
        player.items_in_inventory()
    elif player_input.lower() == "l":
        player.current_room.items_in_room()
    elif "get" in player_input.lower():
        player_words = player_input.split()

        if len(player_words) > 1:
            player_item_selection = player_words[1]
            found_item = current_room.does_item_exist(player_item_selection)

            print(found_item)
            if found_item:
                player.add_item(found_item)
                current_room.remove_item(found_item)
        else:
            print("What are you trying to get?")

    elif "drop" in player_input.lower():
        print("Dropping...")

        player_words = player_input.split()

        if len(player_words) > 1:
            player_item_selection = player_words[1]
            player_has_item = player.is_item_in_inventory(
                player_item_selection)

            if (player_has_item):
                current_room.add_item(player_has_item)
                player.drop_item(player_has_item)
        else:
            print("What are you trying to drop?")

            print(player_item_selection)
    elif player_input == 'q':
        os.system("clear")
        print("Thank you for playing!\n")
        break
    else:
        print("Invalid operation. Please select again.\n")
