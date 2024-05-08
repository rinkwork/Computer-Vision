import cv2
import numpy as np

img = cv2.imread('images/nature_grass.jpg')
cv2.imshow('test image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
