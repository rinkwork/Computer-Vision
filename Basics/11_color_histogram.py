import cv2
import matplotlib.pyplot as plt

image1 = cv2.imread('../images/nature_grass.jpg')

for i, col in enumerate(['b', 'g', 'r']):
    hist = cv2.calcHist([image1], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()
