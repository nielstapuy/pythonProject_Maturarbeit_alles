import cv2 as cv
import numpy as np
import pandas as pd

if __name__ == '__main__':
    data_frame = pd.read_csv('E:\Programmiere\pythonProject_Maturarbeit\draw\data.csv')

    x_values = data_frame["x_values"].to_numpy(dtype=int)
    y_values = data_frame["y_values"].to_numpy(dtype=int)
    print(f"{x_values=}, {y_values=}")


img = cv.imread("E:/Software_img_processing/processed_images/lines_white.png")

# cv.imshow('img', img)
# k = cv.waitKey(0) & 0xff  # press ESC to exit
# if k == 27:
#     cv.destroyAllWindows()

points = np.array([[x_values[0], y_values[0]],[x_values[1], y_values[1]],[x_values[2], y_values[2]],[x_values[3], y_values[3]],[x_values[0], y_values[0]]])
#print(points)

img_filled = cv.fillPoly(img, [points], (255,255,255))
cv.imshow('filled', img_filled)
k = cv.waitKey(0) & 0xff  # press ESC to exit
if k == 27:
    cv.destroyAllWindows()

cv.imwrite("E:/Software_img_processing/processed_images/filled_image.png", img_filled)