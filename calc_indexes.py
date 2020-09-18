# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 18:36:11 2020

@author: Alexandra
"""

import numpy as np

#1 0.435–0.451 Coastal Aerosol (CA)
#2 0.452–0.512 Blue
#3 0.533–0.590 Green
#4 0.636–0.673 Red
#5 0.851–0.879 Near Infrared (NIR)
#6 1.566–1.651 Shortwave NIR 1 (SWIR1)
#7 2.107–2.294 Shortwave NIR 2 (SWIR2)

""" MNDWI = (Blue − NIR)/(Blue + NIR) """
def getMNDWI(b2, b5):
    a = b2 - b5
    b = b2 + b5
    b[b == 0] = 1
    MNDWI = np.divide(a,b)
    return MNDWI

""" NDWI = (Blue − Red)/(Blue + Red) """
def getNDWI(b2, b4):
    a = b2 - b4
    b = b2 + b4
    b[b == 0] = 1
    NDWI = np.divide(a,b)
    return NDWI

""" AWEInsh = 4*(Blue - Near) - (0.25*Red + 2.75*SWIR2) """
def getAWEInsh(b2, b4, b5, b7):    
    AWEInsh = 4*(b2 - b5) - (0.25*b4 + 2.75*b7)
    return AWEInsh

""" AWEIsh = CA + 2.5*Blue - 1.5*(Red + Near) - 0.25*SWIR2 """
def getAWEIsh(b1, b2, b4, b5, b7):
    AWEIsh = b1 + 2.5*b2 - 1.5*(b4 + b5) - 0.25*b7
    return AWEIsh



