import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img_laplacian.jpg',0)
kernel = np.ones((1,1),np.uint8)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
blur = cv2.GaussianBlur(opening,(3,3),0)

ret3,th4 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) 
laplacian = cv2.Laplacian(th4,cv2.CV_8UC1)
cst = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
minLineLength = 150
maxLineGap = 30
lines = cv2.HoughLinesP(laplacian,1,np.pi/180,100,minLineLength,maxLineGap)
for line in lines:    
    for x1,y1,x2,y2 in line:
         cv2.line(cst,(x1 + 1000,y1),(x2 - 5000,y2),(0,255,0),1)

cv2.imwrite('linesDetected_laplacian.jpg',cst)