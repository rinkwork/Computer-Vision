import cv2

img = cv2.imread('images/nature_grass.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cv2.imshow('RGB image', img)
cv2.imshow('Gray image', gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
