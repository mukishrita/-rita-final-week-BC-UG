from room import Room

class Office(Room):
    """
        A type of room in the Dojo
    """
    offices = []

    def __init__(self, room_name):
        self.room_capacity = 6
        self.room_name = room_name
        # return [self.room_name, self.room_capacity]