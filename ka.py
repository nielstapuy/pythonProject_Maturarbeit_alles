import cv2 as cv
import numpy as np


def resize_img (frame, scale = 0.2):
    new_width = int(frame.shape[1] * scale)      # [1] steht für width und [0] für height
    new_height = int(frame.shape[0] * scale)    # convert to int!!

    dimensions = (new_width, new_height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

