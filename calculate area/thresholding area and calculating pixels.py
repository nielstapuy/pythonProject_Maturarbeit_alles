import numpy as np
import cv2 as cv
import ka
import pandas as pd

#img = cv.imread("E:/Software_img_processing/processed_images/filled_image.png", 0)        #0 für RGB -> 0 farbchannels??
img = cv.imread("E:/Software_img_processing/processed_images/filled_image.png", 0)
img_re = ka.resize_img(img, scale=1)
area_px = []

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
 cv.imwrite('E:/Thresh.png', thresh)
 k = cv.waitKey(10) & 0xFF
 if k == 27:
    break
print(cv.countNonZero(thresh))
area_px.append(cv.countNonZero(thresh))
cv.destroyAllWindows()

if __name__ == '__main__':
    data_frame = pd.read_csv('E:\Programmiere\pythonProject_Maturarbeit\draw\data.csv')

    x_values = data_frame["x_values"].to_numpy(dtype=int)
    y_values = data_frame["y_values"].to_numpy(dtype=int)
    print(f"{x_values=}, {y_values=}")

img_end = cv.imread("E:/Software_img_processing/processed_images/lines_white.png")


        ##UMRECHNUNG###

def umrechnung(h):
    return 316938*h**-1.854

h = (int(input("Enter Number: ")))

Pixel = umrechnung(h)

FINAL_RECHNUNG = round(area_px[0] / Pixel,2)
# area_m = area_cm * 0.0001
print(FINAL_RECHNUNG)
img_end_text = cv.putText(img_end, "A: {}cm^2".format(FINAL_RECHNUNG), (x_values[0], y_values[0]), cv.FONT_HERSHEY_PLAIN, 3, (255,255,255), 5)
cv.imshow('Area', img_end_text)
cv.imwrite('E:/Endprodukt.jpg', img_end_text)
k = cv.waitKey(0) & 0xff
if k == 27:
    cv.destroyAllWindows()