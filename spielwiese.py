import numpy as np
import cv2 as cv
import pandas as pd

from csv import DictReader

file_handle = open("data.csv", "r", encoding="utf8")
csv_reader = DictReader(file_handle)
for row in csv_reader:
    print(row)

file_handle.close()

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


