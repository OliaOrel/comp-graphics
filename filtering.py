from PIL import Image
from PIL import ImageFilter
from pylab import *

im0 = Image.open('images/kim.jpg')
figure(figsize =(15,15))

subplot(2, 3, 1)
imshow(im0)
title('Original')

subplot(2, 3, 2)
im1 =  im0.filter(ImageFilter.CONTOUR)
imshow(im1)
title('Contour')

subplot(2, 3, 3)
im2 =  im0.filter(ImageFilter.DETAIL)
imshow(im2)
title('Detail')

subplot(2, 3, 4)
im3 = im0.filter(ImageFilter.EMBOSS)
imshow(im3)
title('Emboss')

subplot(2, 3, 5)
im4 =  im0.filter(ImageFilter.SMOOTH_MORE)
imshow(im4)
title('Smooth')

subplot(2, 3, 6)
im5 =  im0.filter(ImageFilter.FIND_EDGES)
plt.imshow(im5)
plt.title('Find Edges')

show()
