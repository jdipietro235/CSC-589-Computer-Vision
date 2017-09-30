

# Justin DiPietro
# homework 2


import numpy as np
import cv2
import scipy.ndimage as ndimage
from scipy import misc
import matplotlib.pyplot as plt


'''
Problem 4 (10pts).  Write a function that finds the outline of simple
'''

def Problem4():
    print("Problem 4")

    img = cv2.imread('peppers.png', 0)
    img_sobel = ndimage.filters.sobel(img)

    bn_img = np.zeros([img_sobel.shape[0],img_sobel.shape[1]])
    sbl_max = np.amax(abs(img_sobel))
    bn_img = np.abs(img_sobel) >= (sbl_max/1.0)

    plt.subplot(121),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img_sobel,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    plt.show()
    

Problem4()





