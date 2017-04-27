"""
Usage:
    dojo create_room <room_type> <room_name>...
    dojo add_person <first_name> <sur_name> <person_type> [<assign_living_space>]
    dojo print_room <room_name>
    dojo print_allocations [-o <filename>]
    dojo print_unallocated [-o <filename>]
    dojo reallocate_person <person_identifier> <new_room_name>
    dojo load_people [-o <filename>]
    dojo save_state [--db=<sqlite_database>]
    dojo load_state <sqlite_database>
    dojo print_rooms
    dojo (-i | --interactive)
    dojo (-h | --help | --version)

Options:
    -h, --help              Show this message
    --version               Print the version
    -o FILE                 Specify file name
    --db=<sqlite_database>  Specify database name
"""

from class_models.the_dojo import Dojo
from docopt import docopt, DocoptExit
import sys
import cmd
import os

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive (cmd.Cmd):
    intro = 'Welcome to the Dojo! Type help for a list of commands.'
    prompt = '(dojo) '
    file = None
    dojo = Dojo()

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>..."""
        room_names = arg["<room_name>"]
        room_type = arg["<room_type>"]
        for room_name in room_names:
            print(self.dojo.create_room(room_name, room_type))
        # print(room_names)

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <first_name> <sur_name> <person_type> [<assign_living_space>]"""
        first_name = arg["<first_name>"]
        sur_name = arg["<sur_name>"]
        person_type = arg["<person_type>"]
        assign_livingspace = arg["<assign_living_space>"]
        if assign_livingspace == "Y":
            assign_livingspace = True
        print(self.dojo.add_person(first_name, sur_name, person_type, assign_livingspace))
        # print(arg)

    @docopt_cmd
    def do_print_room(self, arg):
        """Usage: print_room <room_name>"""
        room_name = arg["<room_name>"]
        room = next((room for room in self.dojo.list_rooms if room.room_name == room_name), None)
        for person in room.occupants:
            print(person.first_name+" "+person.sur_name)

    @docopt_cmd
    def do_print_allocations(self, arg):
        """Usage: print_allocations [-o <filename>]"""
        is_file = arg["-o"]
        filename = arg["<filename>"]
        rooms = self.dojo.list_rooms
        message = ""
        for room in rooms:
            message += room.room_name+"\n"
            message += "-----------------------------\n"
            for person in room.occupants:
                message += person.first_name+" "+person.sur_name
                if len(room.occupants) > (room.occupants.index(person) + 1):
                    message += ","
                else:
                    message += "\n\n"
        if is_file:
            text_file = open("files/"+filename, "w")
            text_file.write(message)
            text_file.close()
        print(message)

    @docopt_cmd
    def do_print_unallocated(self, arg):
        """Usage: print_unallocated [-o <filename>]"""
        is_file = arg["-o"]
        filename = arg["<filename>"]
        people = self.dojo.list_people
        message = ""
        for person in people:
            if not person.has_room:
                message += person.first_name+" "+person.sur_name+"\n"
        if is_file:
            text_file = open("files/"+filename, "w")
            text_file.write(message)
            text_file.close()
        print(message)

    @docopt_cmd
    def do_reallocate_person(self, arg):
        """Usage: reallocate_person <first_name> <sur_name> <new_room_name>"""
        first_name = arg["<first_name>"]
        sur_name = arg["<sur_name>"]
        new_room = arg["<new_room_name>"]
        message = self.dojo.reallocate_person(first_name, sur_name, new_room)
        print(message)

    @docopt_cmd
    def do_load_people(self, arg):
        """Usage: load_people [-o <filename>]"""
        is_file = arg["-o"]
        filename = arg["<filename>"]
        if is_file and filename is not False:
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
                    print(self.dojo.add_person(person[0], person[1], person[2], person[3]))
            else:
                print("File does not exist")

    @docopt_cmd
    def do_save_state(self, arg):
        """Usage: save_state [--db=<sqlite_database>]"""
        print(arg)

    @docopt_cmd
    def do_load_state(self, arg):
        """load_state <sqlite_database>"""
        print(arg)

    @docopt_cmd
    def do_print_rooms(self, args):
        """Usage: print_rooms"""
        rooms = self.dojo.list_rooms
        for room in rooms:
            print(room.room_name+", "+room.room_type)
    @docopt_cmd
    def do_quit(self, arg):
        """Quits out of Interactive Mode."""
        print('Good Bye')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)