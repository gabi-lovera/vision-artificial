import numpy as np
import cv2
from matplotlib import pyplot as plt
import pylab as pl


def similaridad(angle, tx, ty, scale):
    img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

    # translation
    (h, w) = (img.shape[0], img.shape[1])
    T = np.float32([[1, 0, tx], [0, 1, ty]])
    shifted = cv2.warpAffine(img, T, (w, h))

    # rotation + scaled
    (h, w) = shifted.shape[: 2]
    center = (w / 2, h / 2)
    R = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(shifted, R, (w, h))

    pl.gray(), pl.axis('equal'), pl.axis('off')
    plt.subplot(121), plt.imshow(img), plt.title('Input')
    plt.subplot(122), plt.imshow(rotated), plt.title('Output')
    plt.show()


similaridad(50, 10, 10, 2)
