from PIL import Image
import numpy as np


def read_img(path):
    img = Image.open(path, "r")
    img_array = np.array(img)
    img_array = np.pad(img_array, ((1, 1), (1, 1), (0, 0)), 'constant', constant_values=0)
    return img_array


def convolution(path, core, num):
    img_array = read_img(path)
    for _ in range(num):
        new_array = np.zeros((img_array.shape[0] - 2, img_array.shape[1] - 2, img_array.shape[2]))
        for i in range(1, img_array.shape[0] - 1):
            for j in range(1, img_array.shape[1] - 1):
                for k in range(img_array.shape[2]):
                    new_array[i - 1][j - 1][k] = np.sum(img_array[i - 1:i + 2, j - 1:j + 2, k] * core, dtype=np.int16)
        new_array = np.clip(new_array, 0, 255)
        img_array = np.pad(new_array, ((1, 1), (1, 1), (0, 0)), 'constant', constant_values=0)

        new_img = Image.fromarray(new_array.astype(np.uint8))
        new_img.show()


if __name__ == "__main__":
    my_core = np.array(
        [[0.0947416, 0.118318, 0.0947416],
         [0.118318, 0.147761, 0.118318],
         [0.0947416, 0.118318, 0.0947416]]
    )
    # my_core = np.array(
    #     [[-1, -1, -1],
    #      [-1, 8, -1],
    #      [-1, -1, -1]]
    # )
    my_img = Image.open("target.jpg", "r")
    my_img.show()

    convolution("target.jpg", my_core, 4)
