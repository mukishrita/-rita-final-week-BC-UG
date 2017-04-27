import unittest
from class_models.the_dojo import Dojo


class TestCreateRoom(unittest.TestCase):
    """Dojo allocates rooms to staff and fellow"""

    #@unittest.skip("if you want to skip test")
    def test_create_room_successfully(self):
        dojo_instance = Dojo()
        initial_room_count = len(dojo_instance.list_rooms)
        blue_office = dojo_instance.create_room("Blue", "office")
        self.assertTrue(blue_office)
        new_room_count = len(dojo_instance.list_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_room_already_exists(self):
        dojo_instance = Dojo()
        blue_office = dojo_instance.create_room("Blue", "office")
        blue_exists = dojo_instance.room_exists("Blue")
        red = dojo_instance.room_exists("Red")
        self.assertTrue(blue_exists)
        self.assertFalse(red)

    def test_add_person_successfully(self):
        dojo_instance = Dojo()
        dojo_instance.create_room("Blue", "office")
        initial_people_count = len(dojo_instance.list_people)
        rita_fellow = dojo_instance.add_person("Rita","Mukimba", "fellow", True)
        self.assertTrue(rita_fellow)
        new_people_count = len(dojo_instance.list_people)
        self.assertEqual(new_people_count - initial_people_count, 1)

    def test_person_already_exists(self):
        dojo_instance = Dojo()
        dojo_instance.create_room("Blue", "office")
        rita = dojo_instance.add_person("Rita", "Mukimba", "staff", False)
        rita_exists = dojo_instance.person_exists("Rita", "Mukimba")
        self.assertTrue(rita_exists)
        Jane = dojo_instance.person_exists("Jane", "Doe")
        self.assertFalse(Jane)

    def test_assign_office(self, person, rooms):



    # def test_people_allocated_successfully(self):
    #     dojo_instance = Dojo()
    #     dojo_instance.create_room("Blue", "office")
    #     rita = dojo_instance.add_person("Rita", "Mukimba", "fellow", True)
    #     room_assigned =
    #     new_people_count = len(dojo_instance.occupants)
    #     self.assertEqual(new_room_count - initial_room_count, 1)
    # def test_assign_office(self):


if __name__ == '__main__':
    unittest.main()
