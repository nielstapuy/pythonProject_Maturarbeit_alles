import cv2 as cv
import numpy as np


img = cv.imread("E:/processed_images/lines_white.png")

cv.imshow('img', img)
k = cv.waitKey(0) & 0xff  # press ESC to exit
if k == 27:
    cv.destroyAllWindows()

points = np.array([[545, 144],[1048, 152],[1026, 495],[536, 471],[545, 144]])

img_filled = cv.fillPoly(img, [points], (255,255,255))
cv.imshow('fill', img_filled)
k = cv.waitKey(0) & 0xff  # press ESC to exit
if k == 27:
    cv.destroyAllWindows()

cv.imwrite("E:/processed_images/filled_image.png", img_filled)

#Frage: dot_coordinates in array einfügen wie? und wie kann die array soviele slots erstellen wie punkte erstellt wurden?