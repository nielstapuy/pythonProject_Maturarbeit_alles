import cv2 as cv
import numpy as np
import ka

bild = cv.imread('E:/processed_images/stitchedOutputProcessed.png')
bild_re = ka.resize_img(bild, scale=0.5)

dot_values_file = open("dot_coordinates", "w")
dot_values_file.close()

#global coordinates)
x = 0
temp_x = 0
first_x = 0

y = 0
temp_y = 0
first_y = 0

values = []


# mouse callback function
def draw(event, current_x, current_y, flags, params):
    # hook up global variables
    global temp_x, temp_y, x, y, first_y, first_x

    if event == cv.EVENT_LBUTTONDOWN:
        if x == 0 and y == 0:
            x = current_x
            y = current_y
            values.append(x)
            values.append(y)
            first_x = x
            first_y = y

        elif x != 0 and y != 0:
            temp_x = x
            temp_y = y
            x = current_x
            y = current_y
            values.append(x)
            values.append((y))


cv.imshow('Draw', bild_re)

cv.setMouseCallback('Draw', draw)

while True:
    cv.imshow('Draw', bild_re)

    if x != first_x and y != first_y:
        cv.line(bild_re, (temp_x, temp_y), (x, y), (255, 255, 255), thickness=3)

    if cv.waitKey(1) & 0xFF == 27: break
cv.destroyAllWindows()
cv.imwrite("E:/processed_images/lines_white.png", bild_re)

#print(values)
dot_values_file = open("dot_coordinates", "a")
dot_values_file.write(str(values))
dot_values_file.close()
