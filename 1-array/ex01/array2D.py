import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
        Slice an array using the given start and end.
        Display informations about the shape after before
        and after slicing.
    """
    if type(family) != list:
        raise ValueError('Family must be a list')
    family = np.asarray(family)
    print("My shape is", family.shape)
    family = family[start:end]
    print("My new shape is", family.shape)
    return family
