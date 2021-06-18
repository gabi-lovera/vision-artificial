#! /usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import cv2


MIN_MATCH_COUNT = 10
imag1 = cv2.imread("Imagen3.jpg")
imag2 = cv2.imread("Imagen4.jpg")

dscr = cv2.SIFT_create()
kp1, des1 = dscr.detectAndCompute(imag1, None)
kp2, des2 = dscr.detectAndCompute(imag2, None)

matcher = cv2.BFMatcher(cv2.NORM_L2)
matches = matcher.knnMatch(des1, des2, k=2)

good = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good.append(m)
if len(good) > MIN_MATCH_COUNT:
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

    H, mask = cv2.findHomography(dst_pts, src_pts, cv2.RANSAC, 5.0)

wimg2 = warp = cv2.warpPerspective(imag2, H, (560, 420))

alpha = 0.5
blend = np.array(wimg2 * alpha + imag1 * (1 - alpha), dtype=np.uint8)
cv2.imwrite('SIFT.jpg', blend)
cv2.imshow("image", blend)
cv2.waitKey()
