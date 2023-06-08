from abc import ABC, abstractmethod


class Character(ABC):
    """A Character with a first_name and a is_alive property"""
    def __init__(self, first_name: str, is_alive=True):
        """Init a character"""
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        if not isinstance(is_alive, bool):
            raise TypeError("is_alive must be a boolean")
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Abstract die class"""
        pass


class Stark(Character):
    """A Stark that inherit from a Character"""

    def die(self):
        """The Stark die"""
        self.is_alive = False
