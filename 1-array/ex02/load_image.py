from PIL import Image
import numpy as np

def ft_load(path: str) -> np.ndarray: 
    image = Image.open(path)
    data = np.asarray(image)
    return data