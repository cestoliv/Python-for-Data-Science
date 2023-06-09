import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """generates a random string id"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass(match_args=True)
class Student:
    """A student"""
    name: str
    surname: str
    active: bool = field(init=False)
    id: str = field(init=False)
    login: str = field(init=False)

    def __post_init__(self):
        """Student post initialization (active, id and login)"""
        self.active: bool = True
        if len(self.name) > 0:
            self.login: str = self.name[0] + self.surname
        self.id: str = generate_id()
