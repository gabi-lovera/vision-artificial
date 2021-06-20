import cv2
import numpy as np
from r import reset

i = True
e = True


def function():
    puntos = []
    coord = []

    def draw_circle(event, x, y, flags, param):
        global i, e
        if i == True:
            if event == cv2.EVENT_LBUTTONDOWN:
                cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

                puntos.append((x, y))
                if np.shape(puntos) == (4, 2):
                    i = False
                    rectification(puntos)

    def rectification(puntos):
        img = cv2.imread('imagen.jpeg')

        # funciona con el siguiente orden: arriba, abajo, derecha y arriba
        # la puerta mide 1.89 de altura y 80 de ancho aprox
        pts1 = np.float32(puntos)
        alt = puntos[1][1] - puntos[0][1]
        anch = puntos[3][0] - puntos[0][0]
        pts2 = np.float32([[0, 0], [0, alt], [anch, alt], [anch, 0]])
        M = cv2.getPerspectiveTransform(pts1, pts2)
        imagen_alineada = cv2.warpPerspective(img, M, (anch, alt))
        cv2.imwrite('result.jpg', imagen_alineada)

    cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
    cv2.setMouseCallback('image', draw_circle)
    img = cv2.imread('imagen.jpeg')
    global i
    while 1:
        cv2.imshow('image', img)
        k = cv2.waitKey(1) & 0xFF
        if not i:
            break
    reset()


function()
cv2.destroyAllWindows()
