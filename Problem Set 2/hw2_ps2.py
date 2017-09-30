

# Justin DiPietro
# homework 2



import numpy as np
import cv2
import scipy.ndimage as ndimage
from scipy import misc
import matplotlib.pyplot as plt
 

    
'''
Problem 2 (20 pts). Histogram equalization.
'''
def Problem2():
    print("Problem 2")
    img = cv2.imread('cheetah.png', 0)

    plt.subplot(2,1,1)
    plt.imshow(img, cmap='gray')
    plt.title('Original image')
    plt.axis('off')

    pixels = img.flatten()

    plt.subplot(2,1,2)
    pdf = plt.hist(pixels, bins=64, range=(0,256), normed=False, color='red', alpha=0.4)
    plt.grid('off')

    plt.twinx()

    cdf = plt.hist(pixels, bins=64, range=(0,256), normed=True, cumulative=True,
                   color='blue', alpha=0.4)

    plt.xlim((0,256))
    plt.grid('off')
    plt.title('PDF & CDF (original image)')
    plt.show()
 

Problem2()
