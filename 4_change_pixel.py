import cv2
import numpy as np

img = cv2.imread('images/cat.jpg')
height, width, depth = np.shape(img)

for i in range(0, width):
    for j in range(0,height):
        img[j][i][0] = 0
        img[j][i][1] = 0
        img[j][i][2] = 0

cv2.imshow('test image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()