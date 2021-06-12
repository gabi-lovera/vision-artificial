#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np

def funtion():
    def draw_circle(event, x, y, flags, param):
        global ix, iy, drawing, mode, crop_img
        drawing = False  # true if mouse is pressed

        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            ix, iy = x, y
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            crop_img = img[iy:y, ix:x]
            cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), 0)

    cv2.namedWindow('Output', cv2.WINDOW_AUTOSIZE)
    cv2.setMouseCallback('Output', draw_circle)
    img = cv2.imread('imagen.jpg')

    while 1:
        cv2.imshow('Output', img)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('g'):
            cv2.imwrite('resultado.png', crop_img)
            break
        if k == ord('r'):
            cv2.destroyAllWindows()
            funtion()
            break
        elif k == ord('q'):
            break
    cv2.destroyAllWindows()

funtion()