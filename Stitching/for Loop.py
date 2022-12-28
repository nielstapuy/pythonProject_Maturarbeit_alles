import cv2 as cv
import numpy as np
import glob
import ka
import imutils

# #Loop zum d Images einzeln zstitche und hoffentlich es bessers resultat zkriege
#
#
# list = [10,12,32,19,100,190]
# #print(len(list))
#
# num_add_final = []
#
# result_1 = list[0]+list[1]
# num_add_final.append(result_1)
# #print(num_add_final)
#
# i = 0
#
# while i<=len(list):
#     result = num_add_final[i]+ list[2 + i]
#     print(result)
#     num_add_final.append(result)
#     i += 1
#     if len(list) == 2 + i:
#         break
# print("Loop finished")
#
# print(num_add_final)
#
# summe_ende = []
# summe_ende.append(num_add_final[-1])
# print(summe_ende)

path = glob.glob('E:/123/*.JPG')

images = []                                     # Vgl.: list

stitched_images = []

w = 0

for image in path:
    img = cv.imread(image)
    images.append(img)
    re = ka.resize_img(img)
    cv.imshow('Image', re)
    k = cv.waitKey(0) & 0xff
    if k == 27:
        cv.destroyAllWindows()
else:
    print("Loading Images out of folder finished")

stitched_images.append(images[0])

imageStitcher = cv.Stitcher_create()

# for i in [range(len(images[]))]:
for i in [2,3,4]:
    a = stitched_images[-1]
    b= images[i]
    error, stitched_img = imageStitcher.stitch([a, b])
    stitched_images.append(stitched_img)

if not error:
    #re_stitch = ka.resize_img(stitched_images[-1])
    #cv.imwrite("stitchedOutput2!.png", stitched_img)
    cv.imshow("Stitched Image 2", stitched_images[-1])
    k = cv.waitKey(0) & 0xff  # press ESC to exit
    if k == 27:
        cv.destroyAllWindows()