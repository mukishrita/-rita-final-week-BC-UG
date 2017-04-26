from class_models.room import Room

class Office(Room):
    """
        A type of room in the Dojo
    """
    offices = []

    def __init__(self, room_name):
        super().__init__(room_name)
        self.room_capacity = 6
        # return [self.room_name, self.room_capacity]