


#Justin DiPietro
# homework 2



import numpy as np
import cv2
import scipy.ndimage as ndimage
from scipy import misc
import matplotlib.pyplot as plt
 

'''
Problem 1 (20pts). Warm up.
'''
def Problem1():
    print('Problem 1')
    print('Image 1: cheetah')
    img1 = cv2.imread('cheetah.png', 0)
    cv2.imshow('image 1', img1)
    k = cv2.waitKey(0)
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()

    img1_blur = ndimage.filters.gaussian_filter(img1,3)
    misc.imsave('cheetah_gaussian_blur.png', img1_blur) 
    plt.figure()
    plt.imshow(img1_blur,cmap=plt.cm.gray)
    plt.show()

    img1_fft = np.fft.fft2(img1_blur)
    magnitude_spectrum1 =  np.log(np.abs(img1_fft))

    print('Image 2: zebra')
    img2 = cv2.imread('zebra.png', 0)
    cv2.imshow('image 2', img2)
    k = cv2.waitKey(0)
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()

    img2_blur = ndimage.filters.gaussian_filter(img2,3)
    misc.imsave('cheetah_gaussian_blur.png', img2_blur) 
    plt.figure()
    plt.imshow(img2_blur,cmap=plt.cm.gray)
    plt.show()

    img2_fft = np.fft.fft2(img2_blur)
    magnitude_spectrum2 =  np.log(np.abs(img2_fft))

    plt.subplot(121),plt.imshow(magnitude_spectrum1, cmap = 'gray')
    plt.title('Image 1'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(magnitude_spectrum2, cmap = 'gray')
    plt.title('Image 2'), plt.xticks([]), plt.yticks([])
    plt.show()

 

Problem1()
    

