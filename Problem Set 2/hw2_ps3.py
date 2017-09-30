
# Justin DiPietro
# homework 2

import numpy as np
import cv2
import scipy.ndimage as ndimage
from scipy import misc
import matplotlib.pyplot as plt

    
'''
Problem 3 (20pts) Separable filters.
'''

def Problem3():
    print("Problem 3")
    img = cv2.imread('peppers.png',0)
    img_guas = ndimage.filters.gaussian_filter(img,3)
    #img_box = ndimage.filters.box_filter(img)
    img_sobel = ndimage.filters.sobel(img)

    kernel_hor = np.array([1.,0.,-1.])
    kernel_ver = np.array([-1.,0.,1.])

    np.convolve(kernel_hor,kernel_ver, mode='full')
    

Problem3()
