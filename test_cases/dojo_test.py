import unittest
from the_dojo import Dojo

class TestCreateRoom(unittest.TestCase):

    """Dojo allocates rooms to staff and fellow"""

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
        self.assertTrue(blue_exists)

    def test_add_person_successfully(self):
        dojo_instance = Dojo()
        initial_people_count = len(dojo_instance.list_people)
        rita_fellow = dojo_instance.add_person("Rita", "Mukimba", "fellow")
        self.assertTrue(rita_fellow)
        new_people_count = len(dojo_instance.list_people)
        self.assertEqual(new_people_count - initial_people_count, 1)

    # def test_person_name_str():
    #     pass

if __name__ == '__main__':
    unittest.main()