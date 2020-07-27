import tifffile
import numpy as np
import matplotlib.pyplot as plt

def open_and_show_tiff(file_name,band):
    
    image = tifffile.imread(file_name, key=0)
    this_band_arr = np.array(image)
    plt.title(band)
    plt.imshow(this_band_arr , cmap = 'gray')
    plt.show()
    return(this_band_arr)
