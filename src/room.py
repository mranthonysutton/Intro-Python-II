from player import Player

# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, *items):
        self.name = name
        self.description = description
        self.item_list = []

        if len(items) > 0:
            for item in items:
                self.item_list.append(item)

    def __str__(self):
        return (f"{self.name}")

    def remove_item(self, item):
        self.item_list.remove(item)

    def add_item(self, item):
        self.item_list.append(item)

    def items_in_room(self):
        # Checks if an item list of a room is empty and returns an error
        if self.item_list == []:
            print("You find no items in the room.")
        # Return the items that are found
        else:
            for item in self.item_list:
                print(f"You find a(n) {item.name}.")

    def does_item_exist(self, item_name):
        for item in self.item_list:
            if item_name.lower() == item.name.lower():
                return item
            else:
                print("You broke something.")

    def pickup_item(self, item):
        if type(self.items) is list:
            for item in self.items:
                self.items.remove(item)
                Player.add_item(item)
        elif self.items == []:
            print("That item does not exist")
        else:
            print(self.items)
            Player.add_item(self.items)
    # TODO: Add list of actions that are available.
