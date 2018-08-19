import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
while(1):
    ret, img = cap.read()
    cv.imshow("hello",img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release
cv.destroyAllWindows
