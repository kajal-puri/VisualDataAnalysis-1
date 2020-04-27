# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 16:13:24 2020

@author: anirbanhp

Team: 
    Anirban Ghosh
    Kajal Puri
    Shilpa Chatterjee
"""

import matplotlib.image as mpimg
import matplotlib.colors as clr
import matplotlib.pyplot as plt


img = mpimg.imread("oldtimer.png")
#print(img)
plt.imshow(img)
img_hsv = clr.rgb_to_hsv(img)
plt.imshow(img_hsv)
img_gray = clr.colorConverter(img_hsv, cv.COLOR_BGR2GRAY)
#cv.imwrite("gray.png", img_gray)

#plt.savefig("hsv.png")