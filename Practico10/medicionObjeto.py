import cv2
import numpy as np
from r import reset

i = True
e = True


def function():

    def rectification():
        img = cv2.imread('imagen.jpeg')

        puntos=(204, 0), (217, 551), (690, 571), (715, 2)
        pts1 = np.float32(puntos)
        alt = puntos[1][1] - puntos[0][1]
        anch = puntos[3][0] - puntos[0][0]
        pts2 = np.float32([[0, 0], [0, alt], [anch, alt], [anch, 0]])
        M = cv2.getPerspectiveTransform(pts1, pts2)
        imagen_alineada = cv2.warpPerspective(img, M, (anch, alt))
        cv2.imwrite('result.jpg', imagen_alineada)

    rectification()
    reset()


function()
cv2.destroyAllWindows()
