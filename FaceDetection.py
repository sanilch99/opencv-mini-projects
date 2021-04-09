# FaceDetection

# method proposed viola and jones

import  cv2

# bringing our face cascade
faceCascade = cv2.CascadeClassifier("resources/haarcascade_frontalface_default.xml")
img = cv2.imread('resources/group.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# these parameters should be finetuned
faces = faceCascade.detectMultiScale(imgGray,1.1,4)
for (x,y,w,h) in faces:
    # we will automatically get x , y , width , height
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("result",img)
cv2.waitKey(0)