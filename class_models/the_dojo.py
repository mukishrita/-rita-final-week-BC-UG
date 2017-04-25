from room import Room
from office import Office
from living_space import LivingSpace 

class Dojo(object):

    """The Dojo contained rooms with fellows and staff"""

    def __init__(self):
        self.no_of_rooms = 0
        self.list_rooms = []
        self.list_people = []


    def create_room(self, room_name, roomtype):
        if len(self.list_rooms) < self.max_no_rooms:
                if roomtype == "office":
                    office = Office(room_name)
                    self.list_rooms.append(office)
                    return "An office called "+room_name+" has been successfully created!"

                elif roomtype == "livingspace":
                    livingspace = LivingSpace(room_name)
                    self.list_rooms.append(livingspace)
                    #self.list_rooms.append(Office(room_name))
                    return "A living space called "+room_name+" has been successfully created!"
        else:
            return "The Dojo has no extra rooms to add"

        # def all_rooms(self):
    #     return self.list_rooms