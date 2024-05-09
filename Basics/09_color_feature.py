import cv2
import numpy as np

img = cv2.imread('../images/nature_grass.jpg')

means = cv2.mean(img)

avgB = int(means[0])
avgG = int(means[1])
avgR = int(means[2])

print(f'avgB = {avgB}')
print(f'avgG = {avgG}')
print(f'avgR = {avgR}')

