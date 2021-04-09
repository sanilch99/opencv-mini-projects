# in open cv the y axis is towards the south unlike the populator convention
# of y axis pointing towars north

import cv2
import numpy as np

img = cv2.imread("resources/Skullz.jpg")
print(img.shape)
# will return (height , width , channels )
cv2.imshow("image",img)

# use cv2.imresize(ogimage,(h,w))
imgResize = cv2.resize(img,(640,360))
print(imgResize.shape)
cv2.imshow("resize",imgResize)

#crop image , here height comes first then width
# og_image[start_height:end_height , start_width:end_width
imgCropped = img[0:1000,400:2000]
cv2.imshow("Cropped",imgCropped)

cv2.waitKey(0)