# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 16:33:02 2020

@author: USER
"""


import numpy as np
import matplotlib.pyplot as plt
import gc
# from calc_indexes import *

index_folder = r'F:\trees_data\indexes\Landsat_B'
folder = index_folder
# b1 = np.load(folder + '1.npy')
# b2 = np.load(folder + '2.npy')
b4 = np.load(folder + '4.npy')
b5 = np.load(folder + '5.npy')
# b7 = np.load(folder + '7.npy')
    
#1 0.435–0.451 Coastal Aerosol (CA)
#2 0.452–0.512 Blue
#3 0.533–0.590 Green
#4 0.636–0.673 Red
#5 0.851–0.879 Near Infrared (NIR)
#6 1.566–1.651 Shortwave NIR 1 (SWIR1)
#7 2.107–2.294 Shortwave NIR 2 (SWIR2)

""" NDVI = (NIR − RED)/(NIR + RED) """
def getNDVI(b5, b4,index_folder):
    a = b5 - b4
    b = b4 + b4
    b[b == 0] = 1
    NDVI = np.divide(a,b)
    return NDVI

    # folder = r'F:\trees_data\indexes\Landsat_B'
    # folder = index_folder
    # # b1 = np.load(folder + '1.npy')
    # # b2 = np.load(folder + '2.npy')
    # b4 = np.load(folder + '4.npy')
    # b5 = np.load(folder + '5.npy')
    # b7 = np.load(folder + '7.npy')
NDVI   = getNDVI(b5, b4,index_folder)
T = 0.35
NDVI[NDVI >= T] = 1
NDVI[NDVI < T] = 0
        
        
        
        
plt.figure(figsize=(20,10))
plt.title("NDVI")
plt.imshow(NDVI, 'Greys')



    # return NDVI
# ndvi=getNDVI(b4,b5,index_folder)
# show_ndvi=show_ndvi(ndvi)