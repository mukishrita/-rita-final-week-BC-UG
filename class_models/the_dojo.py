from class_models.room import Room
from class_models.office import Office
from class_models.living_space import LivingSpace
from class_models.person import Person
from class_models.fellow import Fellow
from class_models.staff import Staff
import random

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

    def add_person(self, first_name,sur_name, person_type, need_livingspace):
        if len(self.list_people) < self.max_no_people:
            if not self.person_exists(first_name, sur_name):
                if person_type == "staff":
                    staff = Staff(first_name, sur_name)
                    self.list_people.append(staff)
                    message = "Staff " + first_name+" "+ sur_name+ " has been successfully added. /n"
                    office_name = self.assign_office(staff)
                    message += first_name+ " has been allocated the office" + office_name
                    return message

                elif person_type == "fellow":
                    fellow = Fellow(first_name, sur_name)
                    self.list_people.append(fellow)
                    message = "Fellow "  + first_name+" "+ sur_name+ " has been successfully added. /n"
                    office_name = self.assign_office(fellow)
                    message += first_name + " has been allocated the office" + office_name
                    if need_livingspace:
                        livingspace_name = self.assign_livingspace()
                        message += first_name + " has been allocated the livingspace" + livingspace_name
                    return message
            else:
                return " Person"  + first_name+" "+ sur_name+ " already exists"
        else:
            return "Create more rooms in Dojo"

    def person_exists(self, person_name):
        for person in self.list_people:
            if person.person_name == person_name:
                return True
        return False

    def assign_office(self, person):
        room = random.choice(self.list_rooms)
        # for room in self.list_rooms:
        if isinstance(room, Office) and len(room.occupants) < room.capacity:
            room.occupants.append(person)
            return room.room_name
        else:
            self.assign_office(person)

    def assign_livingspace(self, person):
        room = random.choice(self.list_rooms)
        # for room in self.list_rooms
        if isinstance(room, LivingSpace)and len(room.occupants) < room.capacity:
            room.occupants.append(person)
            return room.room_name
        else:
            self.assign_office(person)



