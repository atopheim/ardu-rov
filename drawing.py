#usr/bin/env python3

import numpy as np
import cv2
from matplotlib import pyplot as plt
#Load a color image in grayscale
img = cv2.imread("/home/torbjoern/Pictures/dawg.jpg",0)

#Native cv2

cv2.namedWindow("image",cv2.WINDOW_NORMAL)
cv2.imshow("image",img)

# Create a black image
img1 = np.zeros((512,512,3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px
cv2.line(img1,(0,0),(511,511),(255,0,0),5) 
cv2.circle(img1,(447,63), 63, (0,0,255), -1)
cv2.circle(img1,(512-447,63),63,(0,255,0), -1)
cv2.rectangle(img1,(0,0),(128,128),(0,0,255),3)
cv2.rectangle(img1,(384,0),(510,128),(0,255,0),3)
cv2.ellipse(img1,(256,256),(100,50),0,0,180,255,-1)
pts = np.array([[10,460],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))

cv2.polylines(img1,[pts],True,(0,255,255))
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img1,"OpenCv",(10,500),font,4,(255,255,255),2,cv2.LINE_AA)

cv2.imshow("image2",img1)

# end choice
k = cv2.waitKey(0)
if k == 27: #ESC key press
	cv2.destroyAllwindows()
elif k == ord("s"): # s press for saving the picture and exiting
	cv2.imwrite("grayDawg.png", img)
	cv2.imwirte("image2.png", img1)
	cv2.destroyAllwindows()

# matplotlib
#plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#plt.show

