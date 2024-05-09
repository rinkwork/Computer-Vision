import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('../images/nature_grass.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Compute the histogram
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

# Plot the histogram
plt.plot(hist)
plt.xlabel('Pixel Value')
plt.ylabel('Number of Pixels')
plt.show()
