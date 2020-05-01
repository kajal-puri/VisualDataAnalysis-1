
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 16:13:24 2020

@author: anirbanhp

Team: 
    Anirban Ghosh
    Kajal Puri
    Shilpa Chatterjee
"""

import matplotlib.cm as cm
import matplotlib.image as mpimg
import matplotlib.colors as clr
import matplotlib.pyplot as plt
import numpy as np

#Exercise 1
#a)
img = mpimg.imread("oldtimer.png")
#b)
img_hsv = clr.rgb_to_hsv(img)
plt.imshow(img_hsv)
print(img_hsv.shape)
img_gray = img_hsv[:,:,2]
plt.imshow(img_gray,cmap='gray')
#c)
img_gray_new = np.dot(img[...,:3], [0.2989, 0.5870, 0.1140] )
plt.imshow(img_gray_new, cmap = 'gray')
#When translating a color image to black and white (mode “L”), the library uses the ITU-R 601-2 luma transform:
#L = R * 299/1000 + G * 587/1000 + B * 114/1000

#d)
img_hsv[:,:,1] = img_hsv[:,:,1]/ 2 
#print(img_sat.shape)
img_sat = clr.hsv_to_rgb(img_hsv)
plt.imshow(img_sat)

#e)
top = cm.get_cmap('Oranges_r', 128)
bottom = cm.get_cmap('Blues', 128)
brown = np.zeros((img.shape[0],img.shape[1],img.shape[2]))
#newcolors = np.array((top(np.linspace(0, 1, 128)), bottom(np.linspace(0, 1, 128))))
brown[:, :, 0] = 210/256
brown[:, :, 1] = 105/256
brown[:, :, 2] = 30/256
img_blend = img_sat * brown
plt.imshow(img_blend)

#f)
img_hsv = clr.rgb_to_hsv(img)
img_hsv[:,:,0] = img_hsv[:,:,0] / 1.55
img_hue = clr.hsv_to_rgb(img_hsv)
plt.imshow(img_hue)

img_hsv = clr.rgb_to_hsv(img)
img_hsv[:,:,0] = img_hsv[:,:,0] / 5.5
img_hue = clr.hsv_to_rgb(img_hsv)
plt.imshow(img_hue)

#Exercise 3

###########
#a)


 

###########
#b)

def covert_hsv_to_rgb(hsv):
    hue = hsv [:,:,0]
    sat = hsv [:,:,1]
    val = hsv [:,:,2]
    
    r = np.empty_like(hue)
    g = np.empty_like(hue)
    b = np.empty_like(hue)
    
    if (sat == 0.0) : r,g,b= val,val,val
    idx = (hue*6.0).astype(int)
    
    state = (hue*6.0)-idx
    p = val * (1.0 - sat)
    q = val * (1.0 - sat * state)
    t = val * (1.0 - sat * (1.0 - state))
    idx %=6
    if idx == 0: r,g,b = val,t,p
    if idx == 1: r,g,b = q,val,p
    if idx == 2: r,g,b = p,val,t
    if idx == 3: r,g,b = p,q,val
    if idx == 4: r,g,b = t,p,val
    if idx == 5: r,g,b = val,p,q
        
    rgb = np.stack([r, g, b], axis=-1)
    return rgb.reshape(hsv.shape)
   
#3)

'''
Photo editing softwares/applications should have HSV color space over CIEluv. 
Since CIEluv color spaces are closer to human vision applications like monitors or screens preferably should use CIEluv.
'''


