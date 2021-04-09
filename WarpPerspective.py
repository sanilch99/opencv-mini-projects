# WARP PERSPECTIVE
import cv2
import numpy as np


img = cv2.imread('resources/cards.jpg')

width , height = 250,350
# pt1 are the points on the actual image
# pt2 are the points that u want to map pt1 to
pt1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
pt2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
# here we make the perspective matrix using the above points
matrix = cv2.getPerspectiveTransform(pt1,pt2)
# finally do the perspective warp based on the matrix
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("image",img)
cv2.imshow("output",imgOutput)

cv2.waitKey(0)