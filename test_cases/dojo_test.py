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

    #def test_room_already_exists(self):
               

    # def test_person_name_str(self):
        

    # def test_person_name_str():
    #     pass

if __name__ == '__main__':
    unittest.main()