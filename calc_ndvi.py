import numpy as np
import matplotlib.pyplot as plt
import glob
    
#1 0.435–0.451 Coastal Aerosol (CA)
#2 0.452–0.512 Blue
#3 0.533–0.590 Green
#4 0.636–0.673 Red
#5 0.851–0.879 Near Infrared (NIR)
#6 1.566–1.651 Shortwave NIR 1 (SWIR1)
#7 2.107–2.294 Shortwave NIR 2 (SWIR2)

""" NDVI = (NIR − RED)/(NIR + RED) """
def getNDVI(filepath):
    b4 = np.load( glob.glob(filepath + '*B4.npy')[0] )
    b5 = np.load(glob.glob(filepath + '*B5.npy')[0])
    
    # print(b4)
    # print(b5)
    a = b5 - b4
    b = b4 + b4
    b[b == 0] = 1
    NDVI = np.divide(a,b)
    a = None
    b = None
    return NDVI

def show_ndvi(just_ndvi):   
    NDVI = np.copy(just_ndvi)
    T = 0.35
    NDVI[NDVI >= T] = 1
    NDVI[NDVI < T] = 0
    np.save("ndvi", NDVI)
        
    plt.figure(figsize=(20,10))
    plt.title("NDVI")
    plt.imshow(NDVI, 'Greys')
    # print(type(NDVI))
    plt.show
    return(NDVI)
    
    # print('ndvi',NDVI[1500:1505,5500:5555])