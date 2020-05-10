# -*- coding: utf-8 -*-
"""
Created on Sat May  2 18:53:54 2020

@author: anirbanhp

Team: 
    Anirban Ghosh
    Kajal Puri
    Shilpa Chatterjee
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from sklearn.neighbors import KernelDensity


import seaborn as sns
import pandas as pd



#########################################
#Exercise 1

#a)

p1 = np.random.normal(0,2,500)
p2 = np.random.normal(9,2,1500)

#print(p1.shape)
#print(p2.shape)

p = np.concatenate((p1,p2))

#b)
#print (p.shape)
#count, bins, ignored = plt.hist(p, 30, normed=True)

#plt.plot(bins, 1/(2 * np.sqrt(2 * np.pi)) * 
#         np.exp( - (bins - 6.75)**2 / (2 * 2**2) ), 
#         linewidth=2, color='r')

#plt.show()

#c)
gaussian = KernelDensity(bandwidth=1.0, kernel='gaussian')
gaussian.fit(p[:,None])

x_d = np.linspace(-4, 8, 1000)

logprob = gaussian.score_samples(x_d[:, None])
#plt.fill_between(x_d, np.exp(logprob), alpha=0.5)
#plt.plot(p, np.full_like(p, -0.01), '|k', markeredgewidth=1)
#plt.ylim(-0.02, 0.22)

linear = KernelDensity(bandwidth=1, kernel='linear')
linear.fit(p[:,None])

x_d = np.linspace(-4, 8, 1000)

logprob = linear.score_samples(x_d[:, None])
plt.fill_between(x_d, np.exp(logprob), alpha=0.8)
plt.plot(p, np.full_like(p, -0.01), '|k', markeredgewidth=1)
plt.ylim(-0.02, 0.22)


#The Difference are observed because gausian kde tries to fit a more normalized curve vs 
#linear where the curve consists of straighter lines 

#d)

gaussian1 = KernelDensity(bandwidth=1.0, kernel='gaussian')
gaussian2 = KernelDensity(bandwidth=2.0, kernel='gaussian')
gaussian3 = KernelDensity(bandwidth=0.5, kernel='gaussian')
gaussian4 = KernelDensity(bandwidth=0.1, kernel='gaussian')
gaussian5 = KernelDensity(bandwidth=3, kernel='gaussian')

gaussian1.fit(p[:,None])
gaussian2.fit(p[:,None])
gaussian3.fit(p[:,None])
gaussian4.fit(p[:,None])
gaussian5.fit(p[:,None])



logprob = linear.score_samples(x_d[:, None])
plt.fill_between(x_d, np.exp(logprob), alpha=0.8)
plt.plot(p, np.full_like(p, -0.01), '|k', markeredgewidth=1)
plt.ylim(-0.02, 0.22)


#e)
# The bandwidth of the KDE gives a distance or the scope for the data to normalize and thus we see smoother curves as we increase
# the bandwidth. Different Kernel functions in turn helps in representing for better analysis. 

'''
#########################################
#Exercise 2

#a)
xl = pd.read_csv("winequality-red.csv", delimiter=';')
#print(xl.head(10))

#b)
quality = xl['quality']
#print(quality)
sns.distplot(quality, kde=False, rug=True);


'''




