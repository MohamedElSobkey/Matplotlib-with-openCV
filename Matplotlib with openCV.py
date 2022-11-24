import cv2 
from matplotlib import pyplot as plt


img = cv2.imread('lena.jpg', -1)
print(cv2.imshow('image', img))

#rgb
img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB) 

plt.imshow(img)  #bgr


cv2.waitKey(0)
cv2.destroyAllWindows()



#==================*========================#

import cv2 
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('gradient.png', 0)

_,Th1 = cv2.threshold(img, 55, 255, cv2.THRESH_BINARY)
_,Th2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
_,Th3 = cv2.threshold(img, 127 , 255, cv2.THRESH_TRUNC)
_,Th4 = cv2.threshold(img , 127, 255, cv2.THRESH_TOZERO)
_,Th5 = cv2.threshold(img , 127, 255, cv2.THRESH_TOZERO_INV)

Titles = [ 'Original Image', 'BINARY', 'BINARY_INV' , 'TRUNC', 'TOZERO', 'TOZERO_INV']
Images = [img,Th1,Th2,Th3,Th4,Th5]


for i in range(6) :
    plt.subplot (2,3,i+1), plt.imshow(Images[i], 'gray')
    plt.title(Titles[i])
    plt.xticks([]), plt.yticks([])
    
    
    
    
plt.show()
#cv2.waitKey(0)
#cv2.destroyAllWindows()
    
