import cv2

img = cv2.imread('hoja.png', 0)
thr = 200
img[img >= thr] = 255
img[img < thr] = 0
cv2.imwrite('resultado.png', img)
cv2.imshow('resultado', img)

cv2.waitKey(0)

