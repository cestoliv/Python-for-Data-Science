class calculator:
    def __init__(self, vec):
        self.vec = vec

    def __add__(self, object):
        for i in range(len(self.vec)):
            self.vec[i] += object
        print(self.vec)
    
    def __mul__(self, object):
        for i in range(len(self.vec)):
            self.vec[i] *= object
        print(self.vec)

    def __sub__(self, object):
        for i in range(len(self.vec)):
            self.vec[i] -= object
        print(self.vec)

    def __truediv__(self, object):
        if object == 0:
            raise ZeroDivisionError("division by zero")
        for i in range(len(self.vec)):
            self.vec[i] /= object
        print(self.vec)