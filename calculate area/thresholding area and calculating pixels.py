import numpy as np
import cv2 as cv
import ka

img = cv.imread("E:/processed_images/filled_image.png", 0)        #0 für RGB -> 0 farbchannels??
img_re = ka.resize_img(img, scale=0.8)

def nothing(x):
  pass

cv.namedWindow('image')

cv.createTrackbar('min','image',0,255,nothing)
cv.createTrackbar('max','image',0,255,nothing)

while(1):

 a = cv.getTrackbarPos('min','image')
 b = cv.getTrackbarPos('max','image')
 ret,thresh=cv.threshold(img_re,a,b,cv.THRESH_BINARY_INV)
 cv.imshow("output",thresh)
 k = cv.waitKey(10) & 0xFF
 if k == 27:
    break
print(cv.countNonZero(thresh))
cv.destroyAllWindows()