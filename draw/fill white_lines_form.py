import cv2 as cv
import numpy as np

img = cv.imread("E:/processed_images/lines_white.png")

cv.imshow('img', img)
k = cv.waitKey(0) & 0xff  # press ESC to exit
if k == 27:
    cv.destroyAllWindows()