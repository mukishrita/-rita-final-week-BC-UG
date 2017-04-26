from class_models.person import Person

class Fellow(Person):
    """
        A type of person in the Dojo
    """
    list_fellows = []

    def __init__(self, person_name):
        super().__init__(person_name)
        self.wants_livingspace = False