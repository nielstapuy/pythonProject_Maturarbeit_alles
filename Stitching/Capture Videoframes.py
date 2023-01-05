import cv2 as cv
import numpy as np

        ### VIDEO IN EINZELNEN FRAMES SPEICHERN ###

cap = cv.VideoCapture('E:/Test_VID.MP4')
count = 0
while cap.isOpened():
    ret,frame = cap.read()
    #cv.imshow('Video', frame)
    cv.imwrite("E:/Software_img_processing/Vids/frame%d.jpg" % count, frame)
    count = count + 1
    if cv.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows() # destroy all opened windows