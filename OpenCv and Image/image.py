import cv2
import numpy as np


image = cv2.imread("1.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_image = cv2.bitwise_not(gray_image)
cv2.imwrite('gray_image.png',gray_image)
image2 = np.array(gray_image, copy=True)
row, col = image2.shape
for i in range(row):
    for j in range(col):
        print('{} '.format(image2[i][j]), end="")
    print()