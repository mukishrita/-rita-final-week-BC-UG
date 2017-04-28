from class_models.room import Room

class LivingSpace(Room):
    """
        A type of room in the Dojo
    """
    livingspace_rooms = []

    def __init__(self, room_name, room_type):
        super().__init__(room_name, room_type)
        self.capacity = 4
        self.room_type = "livingspace"


