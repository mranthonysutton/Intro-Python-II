from player import Player

# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    # TODO: Format the print of the room information, instead of having it
    # within the adv.py
    def __str__(self):
        return (f"{self.name}")

    def items_in_room(self):
        if len(self.items) >= 1:
            for item in self.items:
                print(f"{item.name}")

    def pickup_item(self, item):
        self.items.remove(item)
        Player.add_item(item)

    # TODO: Add list of exists that are available.
