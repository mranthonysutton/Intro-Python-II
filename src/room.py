from player import Player

# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = []
        if len(self.items) > 0:
            for item in self.items:
                self.items.append(item)
        else:
            self.items = items

    def __str__(self):
        return (f"{self.name}")

    def items_in_room(self):
        # Checks if an item list of a room is empty and returns an error
        if self.items == []:
            print("No item(s) were found in this room.")

        # Checks if their is a list of items, and prints them out one, by one
        elif type(self.items) is list:
            for item in self.items:
                print(f"You find a(n) {item.name}.")

        # Else, just prints the single item found
        else:
            print(f"You find a(n) {self.items.name}.")

    def pickup_item(self, item):
        self.items.remove(item)
        Player.add_item(item)

    # TODO: Add list of exists that are available.
