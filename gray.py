from PIL import Image
from pylab import *

im = array(Image.open('images/min.jpg').convert('L'))

gray()

negative_im = 255 - im
clamped_im = (100.0 / 255) * im + 100
contrast_im = 255.0 * (im / 255.0)**2

subplot(2, 2, 1)
imshow(im)
title('Original')

subplot(2, 2, 2)
imshow(negative_im)
title('Negative')

subplot(2, 2, 3)
imshow(clamped_im)
title('Clamped')

subplot(2, 2, 4)
imshow(contrast_im)
title('High contrast')

show()
