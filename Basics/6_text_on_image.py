import cv2

img = cv2.imread('../images/cat.jpg')

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'AvionicLAB', (50, 50), font, 2, (255, 0, 0), 2)

cv2.imshow('test image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()