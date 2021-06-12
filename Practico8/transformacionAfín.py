import cv2
import numpy as np
from PIL import Image, ImageDraw

refPt = []
i = True


def draw_circle(event, x, y, flags, param):
    global i
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

        refPt.append((x, y))
        if np.shape(refPt) == (3, 2):
            i = False
            trasnfomacionAfin(refPt)


def trasnfomacionAfin(refPt):
    img = cv2.imread('imgblue.jpg')
    print(refPt)
    pts1 = np.float32(refPt)
    rows, cols, ch = img.shape
    pts2 = np.float32([[0, 0], [0, rows], [cols, rows]])

    matrix = cv2.getAffineTransform(pts1, pts2)
    result = cv2.warpAffine(img, matrix, (cols, rows))
    cv2.imwrite('result.jpg', result)

    im1 = Image.open('imgshelf.jpg')
    im2 = Image.open('result.jpg')

    mask_im = Image.new("L", im2.size, 0)
    draw = ImageDraw.Draw(mask_im)
    # funciona cuando los puntos se hacen arriba primero, abajo y a la derecha

    p4 = (refPt[2][0] - refPt[1][0] + refPt[0][0], refPt[2][1] - refPt[1][1] + refPt[0][1])
    points = (refPt[0], refPt[1], refPt[2], p4)
    draw.polygon(points, fill=255)
    mask_im.save('mask.jpg', quality=95)

    back_im = im1.copy()
    back_im.paste(im2, (0, 0), mask_im)
    back_im.save('final.jpg', quality=95)


cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback('image', draw_circle)
img = cv2.imread('imgshelf.jpg')

while 1:
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if not i:
        break

while True:
    result = cv2.imread('final.jpg')
    cv2.imshow('image', result)
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('q'):
        break

cv2.destroyAllWindows()
