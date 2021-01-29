import tifffile
import numpy as np
import matplotlib.pyplot as plt
import glob
from utilities import getCoordCornersMTL
from calcOffsets import cornersOffset


def calcTIFF(filepath):
    tiff_file = glob.glob(filepath + '*B6.TIF')[0] 
    mtl_file  = glob.glob(filepath + r'*MTL.txt')[0]
    
    B4 = tifffile.imread(tiff_file, key = 0)    
    # расстояние между углами тифф-картинки в градусах
    t_lat_min, t_lat_max, t_lon_min, t_lon_max = getCoordCornersMTL(mtl_file)
    t_max_idx, t_min_idx, t_max_idy, t_min_idy = cornersOffset(B4)
    
    t_corners = {"lon_min": (t_lon_min, t_min_idx), "lon_max": (t_lon_max, t_max_idx), 
               "lat_min": (t_lat_min, t_min_idy), "lat_max": (t_lat_max, t_max_idy)}
    
    print("t_corners", t_corners)
    
    return (B4, t_corners)

def open_and_show_tiff(file_name, band):
    print('работает open_and_show_tiff,\n')  
    
    image = tifffile.imread(file_name, key=0)
    this_band_arr = np.array(image)
    plt.title(band)
    plt.imshow(this_band_arr , cmap = 'gray')
    plt.show()
    return this_band_arr
