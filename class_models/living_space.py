from class_models.room import Room

class LivingSpace(Room):
    """
        A type of room in the Dojo
    """
    livingspace_rooms = []

    def __init__(self, room_name):
        super().__init__(room_name)
        self.room_capacity = 4
        # return [self.room_name, self.room_capacity]