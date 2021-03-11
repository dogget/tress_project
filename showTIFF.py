import tifffile
import numpy as np
import matplotlib.pyplot as plt
import glob

def openTIFF(filepath):
    tiff_file = glob.glob(filepath + '*B4.TIF')[0] 
    
    B4 = tifffile.imread(tiff_file, key = 0)    
    plt.imshow(B4)
    plt.show()
    
    return B4

def open_and_show_tiff(file_name, band):
    print('работает open_and_show_tiff,\n')  
    
    image = tifffile.imread(file_name, key=0)
    this_band_arr = np.array(image)
    plt.title(band)
    plt.imshow(this_band_arr , cmap = 'gray')
    plt.show()
    return this_band_arr
