from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
        Load the image at the given path with Pillow,
        then convert it to a numpy array and return it.
        Can raise Exceptions.
    """
    image = Image.open(path)
    data = np.asarray(image)
    return data
