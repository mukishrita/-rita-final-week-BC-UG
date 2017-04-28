import unittest
from class_models.the_dojo import Dojo


class TestDojo(unittest.TestCase):
    """Dojo allocates rooms to staff and fellow"""

    #@unittest.skip("if you want to skip test")
    def test_create_room_successfully(self):
        dojo_instance = Dojo()
        initial_room_count = len(dojo_instance.list_rooms)
        blue_office = dojo_instance.create_room("Blue", "office")
        self.assertTrue(blue_office[0])
        new_room_count = len(dojo_instance.list_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_room_already_exists(self):
        dojo_instance = Dojo()
        blue_office = dojo_instance.create_room("Blue", "office")
        blue_exists = dojo_instance.room_exists("Blue")
        red_exists = dojo_instance.room_exists("Red")
        self.assertTrue(blue_exists)
        self.assertFalse(red_exists)

    def test_add_person_successfully(self):
        dojo_instance = Dojo()
        dojo_instance.create_room("Blue", "office")
        initial_people_count = len(dojo_instance.list_people)
        rita_fellow = dojo_instance.add_person("Rita","Mukimba", "fellow", True)
        self.assertTrue(rita_fellow[0])
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

    def test_print_allocations(self):
        dojo_instance = Dojo()
        dojo_instance.create_room("Blue", "office")
        dojo_instance.add_person("Rita", "Mukimba", "staff", False)
        message = "Blue\n"
        message += "-----------------------------\n"
        message += "Rita Mukimba\n\n"
        self.assertEquals(dojo_instance.print_allocations(False, ""), message)

    def test_print_room(self):
        dojo_instance = Dojo()
        dojo_instance.create_room("Blue", "office")
        add_staff = dojo_instance.add_person("Rita", "Mukimba", "staff", False)
        add_fellow = dojo_instance.add_person("John", "Musoke", "fellow", True)
        occupants = dojo_instance.print_room("Blue")
        self.assertEquals(occupants, [add_staff[2], add_fellow[2]])

    def test_print_unallocated(self):
        dojo_instance = Dojo()
        add_staff = dojo_instance.add_person("Rita", "Mukimba", "staff", False)
        add_fellow = dojo_instance.add_person("John", "Musoke", "fellow", True)
        occupants = dojo_instance.print_unallocated(False, "")
        self.assertEquals(occupants, "Rita Mukimba\nJohn Musoke\n")

    def test_reallocate_person_success(self):
        dojo_instance = Dojo()
        dojo_instance.create_room("Blue", "office")
        dojo_instance.add_person("Rita", "Mukimba", "staff", False)
        dojo_instance.create_room("Red", "office")
        is_realocated = dojo_instance.reallocate_person("Rita","Mukimba","Red")[0]
        self.assertTrue(is_realocated)

    def test_reallocate_person_room_full(self):
        dojo_instance = Dojo()
        dojo_instance.create_room("Blue", "office")
        dojo_instance.add_person("Rita", "Mukimba", "staff", False)
        dojo_instance.add_person("John", "Musoke", "staff", False)
        dojo_instance.add_person("Peter", "Kasule", "staff", False)
        dojo_instance.add_person("Joseph", "Museveni", "staff", False)
        dojo_instance.add_person("Peter", "Musoke", "staff", False)
        dojo_instance.add_person("Officer", "Kasule", "staff", False)
        dojo_instance.create_room("Red", "office")
        dojo_instance.add_person("Rita", "Karungi", "staff", False)
        realocated = dojo_instance.reallocate_person("Rita", "Karungi", "Blue")
        self.assertFalse(realocated[0], realocated[1])


if __name__ == '__main__':
    unittest.main()
