# SHAPES AND TEXT

import cv2
import numpy as np

#creating a matrix with zeros

img = np.zeros((512,512,3),np.uint8)

# line starting from 0 , 0 going all the way till its x = width and y = height
cv2.line(img=img,pt1=(0,0),pt2=(img.shape[1],img.shape[0])
         ,thickness=3,color=(0,255,0))

# rectangle
cv2.rectangle(img, (0, 0), (250, 350),(255, 0, 0), cv2.FILLED)
# this will give a rectangle boundary , to make it filled
# add cv2.FILLED argument to above declaration after color
# and remove thickness

# circle
cv2.circle(img,(400,400),30,(0,0,255),4)

# put text
# scale increase text size , thickness increases font weight
cv2.putText(img,"opencv tut",(100,200),cv2.FONT_ITALIC,2,(150,2,123),5)

cv2.imshow("img", img)
cv2.waitKey(0)
