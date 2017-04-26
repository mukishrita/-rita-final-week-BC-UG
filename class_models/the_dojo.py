from class_models.room import Room
from class_models.office import Office
from class_models.living_space import LivingSpace
from class_models.person import Person
from class_models.fellow import Fellow
from class_models.staff import Staff

class Dojo(object):

    """The Dojo contained rooms with fellows and staff"""

    def __init__(self):
        self.no_of_rooms = 0
        self.list_rooms = []
        self.max_no_rooms = 50
        self.max_no_people = 120
        self.list_people = []

    def create_room(self, room_name, room_type):
        if len(self.list_rooms) < self.max_no_rooms:
            if not self.room_exists(room_name):
                if room_type == "office":
                    office = Office(room_name)
                    self.list_rooms.append(office)
                    return "An office called "+room_name+" has been successfully created!"

                elif roomtype == "livingspace":
                    livingspace = LivingSpace(room_name)
                    self.list_rooms.append(livingspace)
                    #self.list_rooms.append(Office(room_name))
                    return "A living space called "+room_name+" has been successfully created!"
            else:
                return "Room "+room_name+" already exists"
        else:
            return "The Dojo has no extra rooms to add"

    def room_exists(self, room_name):
        for room in self.list_rooms:
            if room.room_name == room_name:
                return True
        return False

    def add_person(self, person_name, person_type):
        if len(self.list_people) < self.max_no_people:
            if not self.person_exists(person_name):
                if person_type == "staff":
                    staff = Staff(person_name)
                    self.list_people.append(staff)
                    return "An person called " + person_name + " has been successfully added!"

                elif person_type == "fellow":
                    fellow = Fellow(person_name)
                    self.list_people.append(fellow)
                    return "A person called " + person_name + " has been successfully created!"
            else:
                return " Person " + person_name+ " already exists"
        else:
            return "Sorry! This Dojo is full"

    def person_exists(self, person_name):
        for person in self.list_people:
            if person.person_name == person_name:
                return True
        return False
