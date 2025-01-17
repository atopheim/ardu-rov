#usr/bin/env python3

import cv2
import numpy as np

#img_rgb = cv2.imread('/home/torbjoern/Professional/Sealab/all_data/images/train_wound/normal_20180416_151150_008429.jpg')

filename = "/home/torbjoern/Projects/Prosjektoppgave2018/vlcsnap-2018-07-11-10h00m23s047.jpg"
img = cv2.imread(filename)
cv2.imshow("IMAGE!", img)

if filename is None: 
    raise Exception("Could not load image !")
cv2.imshow("image", img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# find Harris corners
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)
dst = cv2.dilate(dst,None)
ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
dst = np.uint8(dst)

# find centroids0 in second parameter while loading image using cv2.imread than no need to convert image using
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

# define the criteria to stop and refine the corners
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)

# Now draw them
res = np.hstack((centroids,corners))
res = np.int0(res)
img[res[:,1],res[:,0]]=[0,0,255]
img[res[:,3],res[:,2]] = [0,255,0]

cv2.imwrite('subpixel5.png',img)