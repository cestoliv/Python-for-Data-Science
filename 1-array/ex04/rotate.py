from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def trim(array, x, y, width, height, depth=3):
    """
        Trim an array using the given parameters
    """
    return array[y:y+width, x:x+height, :depth]


def rotate(array):
    """
        Rotate an array
    """
    return list(list(x) for x in zip(*array))[::-1]


def main():
    """
        Open the image, trim it and convert it to grayscale,
        then display it.
    """

    try:
        image = ft_load('animal.jpeg')
    except Exception as e:
        print(e)
        exit()

    image = trim(image, 450, 100, 400, 400, 1)

    print(f'The shape of the image is: {image.shape}', end='')
    print(f' or ({image.shape[0]}, {image.shape[1]})')
    print(image)

    image = rotate(image)

    print(f'New shape after Transpose: ({image.shape[0]}, {image.shape[1]})')
    print(image)

    # Display the image
    image = np.squeeze(image)
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    main()
