import cv2
import numpy as np

img = cv2.imread('../images/cat.jpg')
height, width, depth = np.shape(img)

print(f'Height = {height}')
print(f'width = {width}')
print(f'depth = {depth}')

cv2.imshow('test image', img)
cv2.waitKeyEx(0)
cv2.destroyAllWindows()
