class calculator:
    """A calculator class"""

    def __init__(self, vec):
        """Init a calculator"""
        self.vec = vec

    def __add__(self, object):
        """Add a scalar to the vector"""
        for i in range(len(self.vec)):
            self.vec[i] += object
        print(self.vec)

    def __mul__(self, object):
        """Multiply the vector by a scalar"""
        for i in range(len(self.vec)):
            self.vec[i] *= object
        print(self.vec)

    def __sub__(self, object):
        """Substract a scalar to the vector"""
        for i in range(len(self.vec)):
            self.vec[i] -= object
        print(self.vec)

    def __truediv__(self, object):
        """Divide the vector by a scalar"""
        if object == 0:
            raise ZeroDivisionError("division by zero")
        for i in range(len(self.vec)):
            self.vec[i] /= object
        print(self.vec)
