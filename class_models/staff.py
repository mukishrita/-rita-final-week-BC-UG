from class_models.person import Person

class Staff(Person):
    """
        A type of person in the Dojo
    """
    list_staff = []

    def __init__(self, first_name, sur_name):
        super().__init__(first_name, sur_name)
        self.wants_livingspace = False
