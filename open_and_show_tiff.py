import tifffile
import numpy as np
import matplotlib.pyplot as plt

def open_and_show_tiff(file_name):
    
    image = tifffile.imread(file_name, key=0)
    this_band_arr = np.array(image)
    plt.title('this_band')
    plt.imshow(this_band_arr , cmap = 'gray')
    return(this_band_arr)
