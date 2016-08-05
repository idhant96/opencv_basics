import cv2
import numpy as np

img=cv2.imread("6_circles.jpg",0)


def detect(img):
    out = img.copy()
    gray = img
    circles = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT, 1.8, 1)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(out, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(out, (x - 5, y - 5), (x + 5, y + 5), (0, 125, 255), -1)
            cv2.imshow("output", out)
            cv2.waitKey(0)



detect(img)
cv2.destroyAllWindows()