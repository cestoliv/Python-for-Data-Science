from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, first_name: str, is_alive=True):
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        if not isinstance(is_alive, bool):
            raise TypeError("is_alive must be a boolean")
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        self.is_alive = False


class Stark(Character):
    def __init__(self, first_name: str, is_alive=True):
        super().__init__(first_name, is_alive)

    def die(self):
        super().die()
