from load_image import ft_load
from PIL import Image
import numpy as np

image = ft_load('animal.jpeg')

def trim(array, x, y, width, height):
    return array[y:y + height, x:x+width]

print('The shape of image is', image.shape)
print(image)

im_trim = trim(image, 450, 100, 400, 400)

# im_trim = Image.fromarray(im_trim).convert('L')
# im_trim = np.asarray(im_trim)
im_trim = np.dot(im_trim[...,:3], [0.2989, 0.5870, 0.1140])

print("After trimming:",im_trim.shape)

print(im_trim)

Image.fromarray(im_trim).save('animal_zoom.jpeg')