import cv2
import numpy as np

img = cv2.imread("E:/Software_img_processing/processed_images/filled_image.png")
overlay = img.copy()

# Rectangle parameters
x, y, w, h = 10, 10, 300, 300
# A filled rectangle
cv2.rectangle(overlay, (x, y), (x+w, y+h), (0, 200, 0), -1)

alpha = 0.2  # Transparency factor.

# Following line overlays transparent rectangle
# over the image
image_new = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)

cv2.imshow("some", image_new)
cv2.waitKey(0)

cv2.destroyAllWindows()

# from csv import DictReader
#
# file_handle = open("data.csv", "r", encoding="utf8")
# csv_reader = DictReader(file_handle)
# for row in csv_reader:
#     print(row)
#
# file_handle.close()

#a = np.array([[0,1],[3,4]]) # row then column!
#print(a)
#print(a.shape)

#b = np.append(a, [[7,1],[2,6]], axis= 1)
#print(b)
#print(b.shape)

#NEUE IDEE: Koordinaten erst in normaler Liste speichern mit append und dann zu numpy umformen für Line
#Problem wenn Anfangsliste den Punkt (0,0) enthält ist, dass dann der erste Strich aus dem Ursprung gezogen wird..

#a[1,0] = 9
#print(a)

#a[0,1:3] = [5]   #index 1-2 werded überschriebe, 3 nüme!?
#print(a)



#i = 0

#while i<= 0:
    #if (i % 2) == 0:
        #print("Number is even")
    #else:
        #print("Number is uneven")
    #i += 1

#
# with open('data.csv') as csvfile:
#     with open('data.csv', 'w', newline='') as new_file:
#         csv_reader = csv.DictReader(csvfile)
#         fieldnames = ['firstname', 'lastname', 'email', 'age']
#         csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
#         for row in csv_reader:
#             csv_writer.writerow(row)

# img = cv.imread('E:/Software_img_processing/processed_images/filled_image.png', 0)
# print(img)

