# CONTOUR AND SHAPE DETECTION

import cv2
import numpy as np

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def getContours(img):
    # retr external takes the extreme outer countours ( method of extraction )
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        # finding area for each
        area = cv2.contourArea(cnt)
        #drawing the contour ( imageToDrawOn,Contour,index,color,thickness)
        #cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
        # giving minimum threshold for area to remove noise
        if area > 500 :
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
            # calculate curve length to get approx edge
            per = cv2.arcLength(cnt,closed=True)
            print(per)
            # play around with the resolution value -> this approx gives the corner point
            approx = cv2.approxPolyDP(cnt,0.02*per,True)
            print(len(approx))
            objCor = len(approx)
            # will give us x , y , widht , height of all objects
            x, y, width, height = cv2.boundingRect(approx)
            # drawing bounding boxes around
            if objCor == 3 :ObjectType = "Triangle"
            elif objCor == 4:
                aspRatio = width/float(height)
                if aspRatio >0.95 and aspRatio<1.05:
                    ObjectType = "Square"
                else:
                    ObjectType = "Rectangle"
            elif objCor > 4:
                ObjectType = "Circle"
            else: ObjectType = "none"

            cv2.rectangle(imgContour, (x, y), (x + width, y + height), (0, 20, 255), 3)
            cv2.putText(imgContour, ObjectType,(
                x+(width//2) - 5, y + (height//2) - 5
            ), cv2.FONT_ITALIC, 0.5, (0, 0, 0), 2)
    return ""

path = 'resources/shapes.png'
img = cv2.imread(path)
imgContour = img.copy()

#  pre processing to grayscale
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# higher value of sigma , more the blur
imgBlur = cv2.GaussianBlur(imgGray,ksize=(7,7),sigmaX=1)
#using canny edge detection
imgCanny = cv2.Canny(imgBlur,threshold1=50,threshold2=50)
# from edges we shall find contours
getContours(imgCanny)
imgStack = stackImages(0.7,([img,img,imgGray],[imgBlur,imgCanny,imgContour]))
cv2.imshow("stack",imgStack)
cv2.waitKey(0)