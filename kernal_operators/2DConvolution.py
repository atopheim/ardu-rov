import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("salmon.jpg")

#---- Types of blurs ----#

# An average filter can be applied by convoluting a Kernal with ones and divided by the sum of the matrix
average = cv2.blur(img, (5,5))

kernelAverage = np.ones(5)

# Gaussian blurring will blur while perserving the edges.

kernel3 = np.matrix("1 2 1; \
                    2 4 2;  \
                    1 2 1")/16

kernel5 = np.matrix("1 1 2 1 1; \
                    1 1 4 1 1;  \
                    2 4 8 4 2;  \
                    1 1 4 1 1;  \
                    1 1 2 1 1")/48


#print ("This is the kernel being used \n", kernel5)


dst5 = cv2.filter2D(img, -1, kernel5)
dst3 = cv2.filter2D(img, -1, kernel3)

# Median blur
median = cv2.medianBlur(img,5)

# Bilateral Filtering
blur = cv2.bilateralFilter(img,9,75,75)

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
sobel_kernel = 3
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=sobel_kernel )
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=sobel_kernel )

abs_sobelx = np.absolute(sobelx)
abs_sobely = np.absolute(sobely)

absgraddir = np.arctan2(abs_sobely, abs_sobelx)

print(absgraddir)

# 5) Create a binary mask where direction thresholds are met
thresh = (0, np.pi/2)
binary_output = np.zeros_like(absgraddir)
binary_output[(absgraddir >= thresh[0]) & (absgraddir <= thresh[1])] = 1

plt.plot(121), plt.imshow(binary_output), plt.title("Sobel")
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(dst5), plt.title("Gaussian Blurred5")
plt.xticks([]), plt.yticks([])

#plt.subplot(224), plt.imshow(absgraddir), plt.title("")
#plt.xticks([]), plt.yticks([])

plt.show()

