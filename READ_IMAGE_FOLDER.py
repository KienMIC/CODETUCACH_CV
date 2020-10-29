import numpy
import cv2
import os
import sys
from glob import glob
img_mask = sys.argv[1]+"/*.JPG"
img_names = glob(img_mask)
for img_path in img_names: 
    img = cv2.imread(img_path)
    print(img_path)
    cv2.imshow("Original Image",img) 
    
    img_gray = cv2.imread(img_path,0)
    cv2.imshow("Grayscale Image",img_gray)
    
    img_median = cv2.medianBlur(img_gray,5)
    cv2.imshow("Median Filter Image",img_median)
    
    img_gauss = cv2.GaussianBlur(img_gray,(5,5),0)
    cv2.imshow("Gauss Image",img_gauss)
    
    ret,img_binary = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
    cv2.imshow("Binary Image",img_binary)
    
    key = cv2.waitKey(0)
    if key == 27:
        break