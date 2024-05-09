import cv2
import numpy as np

img = cv2.imread('../images/cat.jpg')

print(img[250][312])  # Output = [B G R] values of RGB

img[1][1][0] = 0
img[1][1][1] = 0
img[1][1][2] = 0

cv2.imshow('test image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
