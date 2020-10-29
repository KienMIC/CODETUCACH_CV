# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 23:36:35 2020

@author: KIENMIC
"""

import cv2
import os
import sys

img = cv2.imread(sys.argv[1])
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()