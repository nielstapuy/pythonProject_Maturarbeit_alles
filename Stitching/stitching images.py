import cv2 as cv
import numpy as np
import glob
import ka
import imutils

#         ### VIDEO IN EINZELNEN FRAMES SPEICHERN ###
#
# cap = cv.VideoCapture('E:/Test_VID.MP4')
# count = 0
# while cap.isOpened():
#     ret,frame = cap.read()
#     #cv.imshow('Video', frame)
#     cv.imwrite("E:/Software_img_processing/Vids/frame%d.jpg" % count, frame)
#     count = count + 1
#     if cv.waitKey(10) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv.destroyAllWindows() # destroy all opened windows

path = glob.glob('E:/Software_img_processing/Buch 20cm/*.jpg')

#path = glob.glob('E:/'NAME DATEI ORDNER'/*.JPG')       #NOTE: Bilder dürfen wohl nicht zu gross sein dann geht das stitchen nicht mehr!!
images = []

for image in path:
    img = cv.imread(image)
    images.append(img)      #append füegt öpis ane tupple ane (bsp. currencies..) da werded die einzelne img id images list kopiert
    re = ka.resize_img(img, scale=0.3)
    cv.imshow('Image', re)
    k = cv.waitKey(0) & 0xff  # press ESC to exit
    if k == 27:
        cv.destroyAllWindows()

print(len(path))

imageStitcher = cv.Stitcher_create()

error, stitched_img = imageStitcher.stitch(images)

if not error:
    re_stitch = ka.resize_img(stitched_img, scale= 0.3)
    cv.imwrite("stitchedOutput2!.png", stitched_img)
    cv.imshow("Stitched Image 2", re_stitch)
    k = cv.waitKey(0) & 0xff  # press ESC to exit
    if k == 27:
        cv.destroyAllWindows()

    stitched_img = cv.copyMakeBorder(stitched_img, 10, 10, 10, 10, cv.BORDER_CONSTANT, (0, 0, 0))

    gray = cv.cvtColor(stitched_img, cv.COLOR_BGR2GRAY)
    thresh_img = cv.threshold(gray, 0, 255, cv.THRESH_BINARY)[1]

    thresh_img_re = ka.resize_img(thresh_img, scale=0.1)

    cv.imshow("Threshold Image", thresh_img_re)
    k = cv.waitKey(0) & 0xff  # press ESC to exit
    if k == 27:
        cv.destroyAllWindows()

    contours = cv.findContours(thresh_img.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    contours = imutils.grab_contours(contours)
    areaOI = max(contours, key=cv.contourArea)

    mask = np.zeros(thresh_img.shape, dtype="uint8")
    x, y, w, h = cv.boundingRect(areaOI)
    cv.rectangle(mask, (x, y), (x + w, y + h), 255, -1)

    minRectangle = mask.copy()
    sub = mask.copy()

    while cv.countNonZero(sub) > 0:
        minRectangle = cv.erode(minRectangle, None)
        sub = cv.subtract(minRectangle, thresh_img)

    contours = cv.findContours(minRectangle.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    contours = imutils.grab_contours(contours)
    areaOI = max(contours, key=cv.contourArea)

    minRectangle_re = ka.resize_img(minRectangle)
    cv.imshow("minRectangle Image", minRectangle_re)
    k = cv.waitKey(0) & 0xff  # press ESC to exit
    if k == 27:
        cv.destroyAllWindows()

    x, y, w, h = cv.boundingRect(areaOI)

    stitched_img = stitched_img[y:y + h, x:x + w]

    stitched_img_re = ka.resize_img(stitched_img, scale=0.1)

    cv.imwrite("E:/Software_img_processing/processed_images/stitchedOutputProcessed.png", stitched_img)

    cv.imshow("Stitched Image Processed", stitched_img_re)
    k = cv.waitKey(0) & 0xff  # press ESC to exit
    if k == 27:
        cv.destroyAllWindows()

else:
    print("Bilder konnten nicht gestitcht werden!\nWahrscheinlich konnten nicht genügend Keypoints gefunden werden!")
