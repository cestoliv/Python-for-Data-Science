from S1E9 import Character


class Baratheon(Character):
    """A Baratheon that inherit from a Character"""
    def __init__(self, first_name: str, is_alive=True):
        """Init a Baratheon"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """The Baratheon die"""
        self.is_alive = False

    def __str__(self) -> str:
        """Return a string representation of the object"""
        return f'Vector: ({self.family_name}, {self.eyes}, {self.hairs})'

    def __repr__(self):
        """Return a string representation of the object"""
        return self.__str__()


class Lannister(Character):
    """A Lannister that inherit from a Character"""
    def __init__(self, first_name: str, is_alive=True):
        """Init a Lannister"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """The Lannister die"""
        self.is_alive = False

    @staticmethod
    def create_lannister(first_name, is_alive=True):
        """Returns a new Lannister"""
        return Lannister(first_name, is_alive)

    def __str__(self) -> str:
        """Return a string representation of the object"""
        return f'Vector: ({self.family_name}, {self.eyes}, {self.hairs})'

    def __repr__(self):
        """Return a string representation of the object"""
        return self.__str__()
