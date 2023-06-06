from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> np.ndarray:
    invTransform = np.vectorize(lambda x: 255 - x)
    invert = invTransform(array)
    return invert

def ft_red(array) -> np.ndarray:
    red = array.copy()
    for i in range(len(red)):
        for j in range(len(red[i])):
            red[i][j][1] = 0
            red[i][j][2] = 0

    return red

def ft_green(array) -> np.ndarray:
    green = array.copy()
    for i in range(len(green)):
        for j in range(len(green[i])):
            green[i][j][0] = 0
            green[i][j][2] = 0

    return green

def ft_blue(array) -> np.ndarray:
    blue = array.copy()
    for i in range(len(blue)):
        for j in range(len(blue[i])):
            blue[i][j][0] = 0
            blue[i][j][1] = 0

    return blue

def ft_grey(array) -> np.ndarray:
    grey = array.copy()
    for i in range(len(grey)):
        for j in range(len(grey[i])):
            # val = 0.2989 * grey[i][j][2] + 0.5870 * grey[i][j][1] + 0.1140 * grey[i][j][0]
            val = 0
            if (grey[i][j][2] > 0):
                val += 0.2989 / (1 / grey[i][j][2])
            if (grey[i][j][1] > 0):
                val += 0.5870 / (1 / grey[i][j][1])
            if (grey[i][j][0] > 0):
                val += 0.1140 / (1 / grey[i][j][0])
            grey[i][j][0] = grey[i][j][1] = grey[i][j][2] = val
    return grey

def display_image(array):
    array = np.squeeze(array)
    plt.imshow(array, cmap='gray')
    plt.axis('off')
    plt.show()

def main():
    """
        Open the image and display it with differents color filters
    """

    try:
        image = ft_load('landscape.jpg')
    except Exception as e:
        print(e)
        exit()

    print(f'The shape of the image is: {image.shape}')
    print(image)

    display_image(image)
    display_image(ft_invert(image))
    display_image(ft_red(image))
    display_image(ft_green(image))
    display_image(ft_blue(image))
    display_image(ft_grey(image))


if __name__ == "__main__":
    main()
