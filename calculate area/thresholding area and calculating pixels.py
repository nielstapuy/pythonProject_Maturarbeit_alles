import numpy as np
import cv2 as cv
import ka

img = cv.imread("E:/Software_img_processing/processed_images/filled_image.png", 0)        #0 für RGB -> 0 farbchannels??
img_re = ka.resize_img(img, scale=1)

def nothing(x):
  pass

# cv.namedWindow('trackbars')
# #
# cv.createTrackbar('min','trackbars',0,255,nothing)
# cv.createTrackbar('max','trackbars',0,255,nothing)

while(1):

 # a = cv.getTrackbarPos('min','trackbars')
 # b = cv.getTrackbarPos('max','trackbars')
 ret,thresh=cv.threshold(img,254,255,cv.THRESH_BINARY)
 cv.imshow("output",thresh)
 k = cv.waitKey(10) & 0xFF
 if k == 27:
    break
print(cv.countNonZero(thresh))
cv.destroyAllWindows()