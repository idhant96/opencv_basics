import cv2
import numpy as np

vid=cv2.VideoCapture(0)

while True:
    _,frame =vid.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_red=np.array([0,48,80])
    u_red=np.array([20,255,255])

    mask=cv2.inRange(hsv,l_red,u_red)
    res=cv2.bitwise_and(frame,frame,mask=mask)

    kernal=np.ones((15,15),np.float32)/225
    skinMask = cv2.GaussianBlur(mask, (3, 3), 0)
    skin = cv2.filter2D(res, -1, kernal)

    cv2.imshow('frame',frame)
    #cv2.imshow('skinmask',skinMask)
    cv2.imshow('Filter',skin)
    k=cv2.waitKey(8) & 0xFF
    if k==27:
        break

cv2.destroyAllWindows()
vid.release()