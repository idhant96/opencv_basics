import numpy as np
import cv2


video=cv2.VideoCapture(0)

def track_color():
    while True:
        _, frame=video.read()
        img_hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        lower_b=np.array([100,50,50])
        upper_b=np.array([130,255,255])
        mask=cv2.inRange(frame,lower_b,upper_b)
        res=cv2.bitwise_and(frame,frame,mask=mask)
       # cv2.imshow('base',frame)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

def track_circle():
    while True:
        _,frame=video.read()
       # frame=cv2.medianBlur()
        out=frame.copy()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        circles=cv2.HoughCircles(gray,cv2.cv.CV_HOUGH_GRADIENT,1.2,100)
        if circles is not None:
            circles=np.round(circles[0,:]).astype("int")
            for (x,y,r) in circles:
                cv2.circle(out,(x,y),r,(0,255,0),4)
                cv2.rectangle(out,(x-5,y-5),(x+5,y+5),(0,125,255),-1)
                cv2.imshow("output",out)
                k = cv2.waitKey(5) & 0xFF
                if k == 27:
                    break






#track_color()
track_circle()
video.release()
cv2.destroyAllWindows()


