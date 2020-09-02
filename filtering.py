import cv2
import numpy as np

filters = {
    'sharpen': np.array([[-1, -1, -1],
                         [-1, 9, -1],
                         [-1, -1, -1]]),
    'emboss': np.array([[0, -1, -1],
                        [1, 0, -1],
                        [1, 1, 0]]),
    'redgreen': np.array([[1, 0, 0],
                          [0, 1, 0],
                          [255, 255, 255]])
}


def filter(image, type, custom_kernel=0):
    if custom_kernel:
        kernel = custom_kernel
    if type is "guassian":
        return cv2.GaussianBlur(image, (35, 35), 0)
    else:
        kernel = filters.get(type, np.identity(3, 'uint8'))

    return cv2.filter2D(image, -1, kernel)
