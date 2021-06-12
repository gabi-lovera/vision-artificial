import cv2
import numpy as np

refPt = []
i = True


def draw_circle(event, x, y, flags, param):
    global i
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

        refPt.append((x, y))
        if np.shape(refPt) == (4, 2):
            i = False
            rectification(refPt)


def rectification(refPt):
    img = cv2.imread('smartv.jpg')

    # funciona con el siguiente orden: arriba, abajo, derecha y arriba
    input_pts = np.float32(refPt)
    output_pts = np.float32([[0, 0], [0, 500], [800, 500], [800, 0]])
    M = cv2.getPerspectiveTransform(input_pts, output_pts)
    out = cv2.warpPerspective(img, M, (800, 500))
    cv2.imwrite('result.jpg', out)


cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback('image', draw_circle)
img = cv2.imread('smartv.jpg')

while 1:
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if not i:
        break

while True:
    result = cv2.imread('result.jpg')
    cv2.imshow('image', result)
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('q'):
        break

cv2.destroyAllWindows()
