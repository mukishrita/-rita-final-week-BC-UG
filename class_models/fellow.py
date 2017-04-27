from class_models.person import Person

class Fellow(Person):
    """
        A type of person in the Dojo
    """
    list_fellows = []

    def __init__(self, first_name, sur_name):
        super().__init__(first_name, sur_name)
        self.wants_livingspace = False
        self.livingspace = None