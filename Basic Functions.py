import cv2
import numpy as np

img = cv2.imread("resources/Skullz.jpg")

#grayscale
# cv2.cvtColor(img Variable , color change ) -> convert color
# in open cv its not rgb its bgr so we choose bgr2gray
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#blur
# using the GaussianBlur .GaussianBlur(input_img, k_size , )
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)

#edge detector
#.Canny(img , threshold1 , threshold2)
imgCanny = cv2.Canny(img,150,200)

#dilation - sometimes edges are not joined completely , hence dilation
# makes edges thicker
# cv2.dilate(img_var, kernel, iteration) a kernel is a matrix
# iteration helps to set edge width
kernel = np.ones((5,5),np.uint8)
imgDilation = cv2.dilate(imgCanny,kernel=kernel,iterations=1)

# erosion - makes edges thinner
imgEroded = cv2.erode(imgDilation,kernel=kernel,iterations=1)

cv2.imshow("Erosion",imgEroded)
cv2.waitKey(0)