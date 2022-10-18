import cv2 as cv
import numpy as np
import ka

bild = cv.imread('E:/processed_maps/stitchedOutputProcessed.png')
bild_re = ka.resize_img(bild)

#global coordinates)
global_x = 0
global_y = 0

x = 0
temp_x = 0
first_x = 0

y = 0
temp_y = 0
first_y = 0


# mouse callback function
def draw(event, current_x, current_y, flags, params):
    # hook up global variables
    global temp_x, temp_y, x, y, first_y, first_x

    if event == cv.EVENT_LBUTTONDOWN:
        if x == 0 and y == 0:
            x = current_x
            y = current_y
            first_x = x
            first_y = y

        elif x != 0 and y != 0:
            temp_x = x
            temp_y = y
            x = current_x
            y = current_y


cv.imshow('Draw', bild_re)

cv.setMouseCallback('Draw', draw)

while True:
    cv.imshow('Draw', bild_re)

    if x != first_x and y != first_y:
        cv.line(bild_re, (temp_x, temp_y), (x, y), (255, 255, 255), thickness=3)

    if cv.waitKey(1) & 0xFF == 27: break
cv.destroyAllWindows()
cv.imwrite("E:/processed_maps/lines_white.png", bild_re)


