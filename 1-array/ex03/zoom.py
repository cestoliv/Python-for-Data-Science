from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image = ft_load('animal.jpeg')

def trim(array, x, y, width, height, depth=3):
	return array[y:y+width, x:x+height, :depth]

print('The shape of image is', image.shape)
print(image)

im_trim = trim(image, 450, 100, 400, 400, 1)
# im_trim = image[:400, :400, :1]

# im_trim = Image.fromarray(im_trim).convert('L')
# im_trim = np.asarray(im_trim)
# im_trim = np.dot(im_trim[...,:3], [0.2989, 0.5870, 0.1140])

print("After trimming:",im_trim.shape, 'or', im_trim.shape[0], 'x', im_trim.shape[1])

print(im_trim)

# Image.fromarray(im_trim).show()


sliced_image = np.squeeze(im_trim)
# print(sliced_image)

# Display the image
plt.imshow(sliced_image, cmap='gray')
plt.axis('off')  # Remove the axes
plt.show()
