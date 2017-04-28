from class_models.room import Room
from class_models.office import Office
from class_models.living_space import LivingSpace
from class_models.person import Person
from class_models.fellow import Fellow
from class_models.staff import Staff
import random
import sqlite3
import os

class Dojo(object):
    """The Dojo contains rooms with fellows and staff"""

    def __init__(self):
        self.list_rooms = []
        self.max_no_rooms = 50
        self.max_no_people = 300
        self.list_people = []
        self.list_offices = []
        self.list_livingspaces = []
        self.checked_rooms = []

    def create_room(self, room_name, room_type):
        if len(self.list_rooms) < self.max_no_rooms:
            if not self.room_exists(room_name):
                if room_type.lower() == "office":
                    office = Office(room_name, room_type)
                    self.list_rooms.append(office)
                    return [True, office]
                    # return "An office called " + room_name + " has been successfully created!"

                elif room_type.lower() == "livingspace":
                    livingspace = LivingSpace(room_name, room_type)
                    self.list_rooms.append(livingspace)
                    return [True, livingspace]
                    # return "A living space called " + room_name + " has been successfully created!"
            else:
                return [False, "Room " + room_name + " already exists"]
        else:
            return [False, "The Dojo has no extra rooms to add"]

    def add_person(self, first_name, sur_name, person_type, need_livingspace):
        if len(self.list_people) < self.max_no_people:
            if isinstance(first_name, str) and isinstance(sur_name, str):
                rooms = self.list_rooms
                if not self.person_exists(first_name, sur_name):
                    if person_type.lower() == "staff":
                        staff = Staff(first_name, sur_name)
                        message = "Staff " + first_name + " " + sur_name + " has been successfully added. \n"
                        office = self.assign_office(staff, rooms, [])
                        if not office:
                            message = "Please add office"
                        else:
                            staff.has_room = True
                            message += first_name + " has been allocated the office " + office.room_name
                        self.list_people.append(staff)
                        return [True, message, staff, office]
                        # return message

                    elif person_type.lower() == "fellow":
                        fellow = Fellow(first_name, sur_name)
                        message = "Fellow " + first_name + " " + sur_name + " has been successfully added. \n"
                        office = self.assign_office(fellow, rooms, [])
                        if not office:
                            message += "Please add office\n"
                        else:
                            fellow.has_room = True
                            message += first_name + " has been allocated the office " + office.room_name + "\n"
                        if need_livingspace:
                            livingspace = self.assign_livingspace(fellow, rooms, [])
                            if not livingspace:
                                message += "Please add living space"
                            else:
                                fellow.has_room = True
                                message += first_name + " has been allocated the livingspace " + livingspace.room_name
                            self.list_people.append(fellow)
                            return [True, message, fellow, office, livingspace]
                        else:
                            self.list_people.append(fellow)
                            return [True, message, fellow, office]
                        # return message
                else:
                    return [False, "Person " + first_name + " " + sur_name + " already exists"]
                    # return " Person " + first_name + " " + sur_name + " already exists"
            else:
                return [False, "Name should be a string"]
        else:
            return [False, "Dojo has reached maximum capacity"]

    def room_exists(self, room_name):
        for room in self.list_rooms:
            if room.room_name == room_name:
                return True
        return False

    def person_exists(self, first_name, sur_name):
        for person in self.list_people:
            if person.first_name == first_name and person.sur_name == sur_name:
                return True
        return False

    def assign_office(self, person, rooms, checked_rooms):
        if len(rooms) > 0 and len(rooms) > len(checked_rooms):
            room = random.choice(rooms)
            # for room in self.list_rooms:
            if isinstance(room, Office) and len(room.occupants) < room.capacity:
                room.occupants.append(person)
                return room
            else:
                if room not in checked_rooms:
                    checked_rooms.append(room)
                #rooms.remove(room)
                return self.assign_office(person, rooms, checked_rooms)
        else:
            return False

    def assign_livingspace(self, person, rooms, checked_rooms):
        if len(rooms) > 0 and len(rooms) > len(checked_rooms):
            room = random.choice(rooms)
            # for room in self.list_rooms
            if isinstance(room, LivingSpace) and len(room.occupants) < room.capacity:
                room.occupants.append(person)
                return room
            else:
                if room not in checked_rooms:
                    checked_rooms.append(room)
                #rooms.remove(room)
                return self.assign_livingspace(person, rooms, checked_rooms)
        else:
            return False

    def print_room(self, room_name):
        room = next((room for room in self.list_rooms if room.room_name == room_name), None)
        return room.occupants

    def print_allocations(self, is_file, filename):
        message = ""
        for room in self.list_rooms:
            message += room.room_name + "\n"
            message += "-----------------------------\n"
            for person in room.occupants:
                message += person.first_name + " " + person.sur_name
                if len(room.occupants) > (room.occupants.index(person) + 1):
                    message += ","
                else:
                    message += "\n\n"
        if is_file:
            text_file = open("files/" + filename, "w")
            text_file.write(message)
            text_file.close()
        return message

    def print_unallocated(self, is_file, filename):
        message = ""
        for person in self.list_people:
            if not person.has_room:
                message += person.first_name + " " + person.sur_name + "\n"
        if is_file:
            text_file = open("files/" + filename, "w")
            text_file.write(message)
            text_file.close()
        return message

    def load_people(self, is_file, filename):
        if is_file and filename is not False:
            counter = 0
            if os.path.isfile("files/"+filename):
                people = [person.rstrip('\n') for person in open("files/"+filename)]
                for person in people:
                    person = person.split()
                    if len(person) == 3:
                        person.append("")
                    if person[3] == "Y":
                        person[3] = True
                    else:
                        person[3] = False
                    add_person = self.add_person(person[0], person[1], person[2], person[3])
                    print(add_person[1])
                    counter += 1
                return [True, "Added " + str(counter) + " people"]
            else:
                return [False, "File does not exist"]

    def reallocate_person(self, first_name, sur_name, new_room_name):
        new_room = next((new_room for new_room in self.list_rooms if new_room.room_name == new_room_name), None)
        if new_room is not None:
            if len(new_room.occupants) < new_room.capacity:
                if self.person_exists(first_name, sur_name):
                    for room in self.list_rooms:
                        for person in room.occupants:
                            if person.first_name == first_name and person.sur_name == sur_name:
                                if room.room_name == new_room_name:
                                    return [False, "Person already in this room"]
                                else:
                                    room.occupants.remove(person)
                                    new_room.occupants.append(person)
                                    return [True, first_name + " " + sur_name + " has been moved to room " + new_room_name]
                else:
                    return [False, "The person does not exist"]
            else:
                return [False, "The room is full"]
        else:
            return [False, "The room does not exist"]

    def save_state(self, sqliteDB):
        if os.path.isfile(sqliteDB):
            conn = sqlite3.connect(sqliteDB)
            cursor = conn.cursor()
            self.create_tables(cursor)
            for room in self.list_rooms:
                room_name = room.room_name
                room_type = room.room_type
                cursor.execute("INSERT INTO rooms VALUES (?, ?)", (room_name, room_type))
                print(cursor.lastrowid)
                occupants = room.occupants

    def load_state(self, sqliteDB):
        if os.path.isfile(sqliteDB):
            conn = sqlite3.connect(sqliteDB)
            c = conn.cursor()

    def create_tables(self, dBcursor):
        dBcursor.execute("""CREATE TABLE IF NOT EXISTS rooms (id INTEGER PRIMARY KEY AUTOINCREMENT, room_name varchar(100) NOT NULL, room_type varchar(20) NOT NULL)""")
        dBcursor.execute("""CREATE TABLE IF NOT EXISTS people (id INTEGER PRIMARY KEY AUTOINCREMENT, first_name varchar(25) NOT NULL, last_name varchar(25) NOT NULL, person_type varchar(20) NOT NULL)""")
        dBcursor.execute("""CREATE TABLE IF NOT EXISTS occupants (id INTEGER PRIMARY KEY AUTOINCREMENT, room_id INTEGER, people_id INTEGER)""")