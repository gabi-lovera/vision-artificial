import cv2
import numpy as np
from scipy.spatial import distance

i = True
e = True
refPt = []
coord = []

def reset():
    global i, e, refPt, coord
    refPt = []
    coord = []
    i = True
    e = True

    def draw_circle(event, x, y, flags, param):
        global i, e, refPt, coord
        if i == True:
            if event == cv2.EVENT_LBUTTONDOWN:
                if e == True:
                    cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
                    coord.append((x, y))
                    if np.shape(coord) == (2, 2):
                        cv2.line(img, coord[0], coord[1], (0, 0, 255), 2)
                        D = distance.euclidean(coord[0], coord[1])/2.52
                        (mX, mY) = midpoint(coord[0], coord[1])
                        cv2.putText(img, "{:.1f}cm".format(D), (int(mX), int(mY - 10)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 0, 0), 2)
                        e = False

    def midpoint(p1, p2):
        return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2

    cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
    cv2.setMouseCallback('image', draw_circle)
    img = cv2.imread('result.jpg')

    while True:
        cv2.imshow('image', img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27 or k == ord('q'):
            break
        if k == ord('r'):
            cv2.destroyAllWindows()
            reset()
            break
