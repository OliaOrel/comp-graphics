import cv2
from pylab import *

img = cv2.imread('images/chon.jpg', 0)

sobel_x = cv2.Sobel(img, -1, 1, 0, ksize = 5)
sobel_y = cv2.Sobel(img, -1, 0, 1, ksize = 5)

subplot(1, 2, 1)
imshow(img, cmap = 'gray')
title('Original')

subplot(1, 2, 2)
imshow(sobel_y, cmap = 'gray')
title('Sobel edge detection')

show()
