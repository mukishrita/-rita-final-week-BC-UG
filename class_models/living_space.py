from class_models.room import Room

class LivingSpace(Room):
    """
        A type of room in the Dojo
    """
    livingspace_rooms = []
    def __init__(self, room_name):
        self.room_capacity = 4
        self.room_name = room_name
        # return [self.room_name, self.room_capacity]