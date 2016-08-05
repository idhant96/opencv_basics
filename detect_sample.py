import numpy as np
import cv2

clock_cascade= cv2.CascadeClassifier("hand_cascade")
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap=cv2.VideoCapture('video.avi')

while True:

    ret,img =cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    clock = clock_cascade.detectMultiScale(gray, 1.3, 5)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in clock:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)


    cv2.imshow('facedetector',img)
   # cv2.imshow('clock', img)
    k = cv2.waitKey(10) & 0xFF
    if k == 27:
        break


cap.release()
cv2.destroyAllWindows()
