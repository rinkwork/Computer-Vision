import cv2

original_img = cv2.imread('../images/nature_grass.jpg')

edited_img = cv2.resize(original_img, (250, 250))

cv2.imshow('original image', original_img)
cv2.imshow('resized image', edited_img)

cv2.waitKey(0)
cv2.destroyAllWindows()