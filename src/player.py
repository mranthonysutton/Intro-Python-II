# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return (f"{self.name} is in the {self.current_room}.")

    def move(self, direction):
        # Set a direction to move to
        move_to = f"{direction}_to"

        # Check if that direction can be moved from the rooms
        # If an error, inform the player
        # else, set the new room
        if hasattr(self.current_room, move_to):
            current_room = getattr(self.current_room, move_to)
            self.current_room = current_room
            print(f"You have entered the {current_room}.\n")
        else:
            print("You hit a wall and are unable to pass through."
                  + " Try a different direction.\n")
