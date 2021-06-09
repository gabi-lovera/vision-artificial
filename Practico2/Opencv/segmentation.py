import cv2

img = cv2.imread('hoja.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

while True:
    ret, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    cv2.imwrite('resultado.png ', thresh)
    cv2.imshow('hoja binarizada', thresh)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()


