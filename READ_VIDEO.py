import numpy as np
import cv2
import sys
import os

cap = cv2.VideoCapture(sys.argv[1])

while(True):
    ret, frame = cap.read()
    frame_median = cv2.medianBlur(frame,5);
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    equ = cv2.equalizeHist(gray) 

    cv2.imshow('frame',frame)
    cv2.imshow('median_frame',frame_median)
    cv2.imshow('equal_hist',equ)
    
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()