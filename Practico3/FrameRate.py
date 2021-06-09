#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import time

cap = cv2.VideoCapture('video.mp4')

fps = cap.get(cv2.CAP_PROP_FPS)
fps = int(fps)
print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
while cap.isOpened():
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if (cv2.waitKey(fps) & 0xFF) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
