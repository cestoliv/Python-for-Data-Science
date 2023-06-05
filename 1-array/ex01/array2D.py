import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    if type(family) != list:
        raise ValueError('Family must be a list')
    family = np.asarray(family)
    print(family.shape)