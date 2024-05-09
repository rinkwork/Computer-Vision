import cv2

img = cv2.imread('../images/nature_grass.jpg')

# [starting point Y:End point Y, starting point X:End point X]
img = img[0:50, 0:600]

cv2.imshow('test image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
