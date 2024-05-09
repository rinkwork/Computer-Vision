import cv2

img = cv2.imread('../images/cat.jpg')

# for line
cv2.line(img, (50, 50), (100, 105), (255, 0, 0), 3)

# for rectangle
cv2.rectangle(img, (270, 20), (500, 500), (0, 255, 0), 3)

# for circle
cv2.circle(img, (50, 250), 25, (0, 0, 255), 3)

cv2.imshow('test image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()