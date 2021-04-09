import cv2
print("package imported")

## READ IMAGES
img = cv2.imread("resources/Skullz.jpg")

##show image imshow(Name, img variable)
#cv2.imshow("Output",img)

#To create a delay so that image doesnt close on you
#cv2.waitKey(0)

##show video

# create a video capture object
#cap = cv2.VideoCapture("resources/video.wmv")

# for using webcam as source
cap = cv2.VideoCapture(0)

#setting width with id 3 and height with id 4 and brightness with id 10
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

#video is a sequence of images
while True:
    success , img = cap.read()
    # success will store true or false
    cv2.imshow("video",img)
    # waits for delay and waits for q to exit
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break