from class_models.room import Room

class Office(Room):
    """
        A type of room in the Dojo
    """


    def __init__(self, room_name, room_type):
        super().__init__(room_name, room_type)
        self.capacity = 6
        self.room_type = "office"

