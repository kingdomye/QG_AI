from PIL import Image
import numpy as np


def read_img(file_path):
    result = [[True for _ in range(128)] for _ in range(128)]
    img = Image.open(file_path)
    img = img.resize((128, 128))
    for col in range(128):
        for row in range(128):
            r, g, b = img.getpixel((col, row))
            if r < 128 and g < 128 and b < 128:
                result[row][col] = False
            else:
                result[row][col] = True
    return np.array(result)


if __name__ == "__main__":
    img_array = read_img("data/img/4-4.jpg")
    print(img_array)
