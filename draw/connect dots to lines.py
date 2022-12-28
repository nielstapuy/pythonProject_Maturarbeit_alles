import cv2 as cv
import numpy as np
import ka
import pandas as pd

bild = cv.imread('E:/Software_img_processing/16cm2_tests/6.JPG')
bild_re = ka.resize_img(bild, scale=0.3)

dot_values_file = open("dot_coordinates", "w") #->json library
dot_values_file.close()

#global coordinates)
x = 0
temp_x = 0
first_x = 0

y = 0
temp_y = 0
first_y = 0

#values = []
values_x = []
values_y = []

#-> eine liste für x eine für y für dot_coordinates ...

# mouse callback function
def draw(event, current_x, current_y, flags, params):
    # hook up global variables
    global temp_x, temp_y, x, y, first_y, first_x

    if event == cv.EVENT_LBUTTONDOWN:
        if x == 0 and y == 0:
            x = current_x
            y = current_y
            values_x.append(x)
            values_y.append(y)
            first_x = x
            first_y = y

        elif x != 0 and y != 0:
            temp_x = x
            temp_y = y
            x = current_x
            y = current_y
            values_x.append(x)
            values_y.append(y)


cv.imshow('Draw', bild_re)

cv.setMouseCallback('Draw', draw)

while True:
    cv.imshow('Draw', bild_re)

    if x != first_x and y != first_y:
        cv.line(bild_re, (temp_x, temp_y), (x, y), (255, 255, 255), thickness=3)

    if cv.waitKey(1) & 0xFF == 27: break
cv.destroyAllWindows()
cv.imwrite("E:/Software_img_processing/processed_images/lines_white.png", bild_re)

#print(values)
# dot_values_file = open("dot_coordinates", "a") ->>> veraltet (jetzt mit csv)
# dot_values_file.write(str(values_x))
# dot_values_file.write(str(values_y))
# dot_values_file.close()

dataframe = pd.DataFrame(
    {
        "x_values": values_x,
        "y_values": values_y
    }
)
dataframe.to_csv("data.csv")
#print(dataframe)

#Problem-> es wird auf resizedem bild gezeichnet aber die daten sollen auf die Originaldatei geschrieben werden..