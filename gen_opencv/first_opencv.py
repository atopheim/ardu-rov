#usr/bin/env python3

import numpy as np
import cv2
from matplotlib import pyplot as plt
#Load a color image in grayscale
img = cv2.imread("/home/torbjoern/Pictures/dawg.jpg",0)

# Native cv2
if (3<4):
	cv2.namedWindow("image",cv2.WINDOW_NORMAL)
	cv2.imshow("image",img)

	k = cv2.waitKey(0)
	if k == 27: #ESC key press
		cv2.destroyAllwindows()
	elif k == ord("s"): # s press for saving the picture and exiting
		cv2.imwrite("grayDawg.png", img)
		cv2.destroyAllwindows()

# matplotlib - why doesn't it work
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show

cv2.waitKey(0)
