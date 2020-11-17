import numpy as np
import matplotlib.pyplot as plt
import gc
    
#1 0.435–0.451 Coastal Aerosol (CA)
#2 0.452–0.512 Blue
#3 0.533–0.590 Green
#4 0.636–0.673 Red
#5 0.851–0.879 Near Infrared (NIR)
#6 1.566–1.651 Shortwave NIR 1 (SWIR1)
#7 2.107–2.294 Shortwave NIR 2 (SWIR2)

""" NDVI = (NIR − RED)/(NIR + RED) """
def getNDVI(b5, b4):
    a = b5 - b4
    b = b4 + b4
    b[b == 0] = 1
    NDVI = np.divide(a,b)
    return NDVI

def show_ndvi(ndvi):   
    NDVI = np.copy(ndvi)
    T = 0.35
    NDVI[NDVI >= T] = 1
    NDVI[NDVI < T] = 0
        
    plt.figure(figsize=(20,10))
    plt.title("NDVI")
    plt.imshow(NDVI, 'Greys')
    print(type(ndvi))
    plt.show
    # print('ndvi',NDVI[1500:1505,5500:5555])