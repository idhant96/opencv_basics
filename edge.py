import cv2
import numpy as np

vid=cv2.VideoCapture(0)

while True:
    _,frame=vid.read()

    edges=cv2.Canny(frame,100,200)

    cv2.imshow('Result',edges)

    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break

cv2.destroyAllWindows()
vid.relaese()