import cv2 as cv
import numpy as np
import ka
import math

rubik = cv.imread('E:/rubiks_cube/pic.JPG')
rubik_re = ka.resize_img(rubik, scale= 0.4)
#cv.imshow('bild', rubik_re)
k = cv.waitKey(0) & 0xff
if k == 27:
    cv.destroyAllWindows()

x = 0
y = 0

dots = np.array([[0,0],[0,0]])              #Zeile 0 für x-Wert und 1 für y-Wert
print(dots)

#contours = np.array( [ [0,0], [150,150], [150, 150], [150,50] ] ) # wie chan ich jetzt da pünkt appende und denn area rechne?

def draw(event, current_x, current_y, flags, params):
    # hook up global variables
    global x, y, drawing

    i = 0

    if event == cv.EVENT_LBUTTONDOWN:
        x = current_x
        y = current_y
        i += 1

        drawing = True
        if drawing:
            x = current_x
            y = current_y
            #dots = np.append(dot_form, [[x], [y]], axis=1)
            dots[0, 0] = x
            dots[1, 0] = y
            print(dots)
            print(dots.shape)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False

cv.imshow('Draw', rubik_re)

cv.setMouseCallback('Draw', draw)

while True:
    cv.imshow('Draw', rubik_re)

    cv.line(rubik_re, (dots[0, -2], dots[1, -2]), (dots[0, -1], dots[1, -1]), (255, 255, 255), thickness=3)

    if cv.waitKey(1) & 0xFF == 27: break
cv.destroyAllWindows()
cv.imwrite("E:/processed_maps/linezszs.png", rubik_re)

#img = np.zeros( (200,200) ) # create a single channel 200x200 pixel black image
#cv.fillPoly(img, pts =[contours], color=(255,255,255))
#cv.imshow("Filled area", img)
#cv.waitKey()


#calculate lines a(=b=c=d) -> rubikcube seiten (siehe papier skizze)

#x_1 = input("Enter x1: ")
#x_2 = input("Enter x2: ")

#x_line = float(x_2) - float(x_1)
#print("x_line is: ")
#print(x_line)

#y_1 = input("Enter y1: ")
#y_2 = input("Enter y2: ")

#y_line = float(y_2) - float(y_1)
#print("y_line is: ")
#print(y_line)

#calculate area)

#a_square = pow(x_line, 2)+ pow(y_line, 2)
#print(a_square)
#a = math.sqrt(a_square)
#print(a)
#A = pow(a, 2)
#print(str(round(A)) + " mm^2?")