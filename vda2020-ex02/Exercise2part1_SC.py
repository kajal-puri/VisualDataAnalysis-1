#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 17:32:25 2020

@author: Shilpa Chatterjee
Subject: Visual Data Analysis_Summer 2020 
Exercise 2: Color 
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.colors as clr
import numpy as np


img = mpimg.imread('oldtimer.png')
plt.imshow(img)


ROWS = len(img)
COLS = len(img[0])
ELMS = 3

hsv_img = clr.rgb_to_hsv(img)
gray_hsv_img = np.array(hsv_img)

gray_hsv_img = np.delete(gray_hsv_img, 0, axis=2)
gray_hsv_img = np.delete(gray_hsv_img, 0, axis=2)


# insert 'H'=0 and 'S'=0
gray_hsv_img = np.insert(gray_hsv_img, 0, 0, axis=2)
gray_hsv_img = np.insert(gray_hsv_img, 0, 0, axis=2)
plt.imshow(clr.hsv_to_rgb(gray_hsv_img))


hsv_array = np.array(hsv_img)
hsv_array = np.reshape(hsv_array, (-1, 3))
sat50_hsv_array = [[x[0], x[1]/2, x[2]] for x in hsv_array]
sat50_hsv_img = np.reshape(sat50_hsv_array, (ROWS, COLS,3))
plt.imshow(clr.hsv_to_rgb(sat50_hsv_img))

br=[.91, .68, .43]
blended_val=[[x[0]+br[0]/2,x[1]+br[1]/2,x[2]+br[2]/2] for x in hsv_array]
brown_img=np.reshape(blended_val,(ROWS,COLS,3))
plt.imshow(clr.hsv_to_rgb(brown_img))


hsv_array = np.array(hsv_img)
hsv_array = np.reshape(hsv_array, (-1, 3))
blue_val=[[(x[0]+.66)%1,x[1],x[2]] for x in hsv_array]
blue_img=np.reshape(blue_val,(ROWS,COLS,3))
plt.imshow(clr.hsv_to_rgb(blue_img))


hsv_array = np.array(hsv_img)
hsv_array = np.reshape(hsv_array, (-1, 3))
x_val=[[(x[0]+.12)%1,x[1],x[2]] for x in hsv_array]
x_img=np.reshape(x_val,(ROWS,COLS,3))
plt.imshow(clr.hsv_to_rgb(x_img))

