import cv2 as cv
import numpy as np
import glob
import ka
import imutils

#Loop zum d Images einzeln zstitche und hoffentlich es bessers resultat zkriege


list = [10,12,32,19,100,190]
#print(len(list))

num_add_final = []

result_1 = list[0]+list[1]
num_add_final.append(result_1)
#print(num_add_final)

i = 0

while i<=len(list):
    result = num_add_final[i]+ list[2 + i]
    print(result)
    num_add_final.append(result)
    i += 1
    if len(list) == 2 + i:
        break
print("Loop finished")

print(num_add_final)

summe_ende = []
summe_ende.append(num_add_final[-1])
print(summe_ende)

path = glob.glob('E:/123/*.JPG')

image_1_2 = []                                     # Vgl.: list

w = 0

while w <= 1:
    img = cv.imread(path[w])
    image_1_2.append(img)
    re = ka.resize_img(img)
    cv.imshow('Image', re)
    cv.waitKey(0)
    w += 1
else:
    print("Loading Image 1 & 2 out of folder finished")

imageStitcher = cv.Stitcher_create()

error, stitched_img = imageStitcher.stitch(image_1_2)

path_2 = glob.glob('E:/zwischen_stitches/*.png') #Vgl.: num_add_final