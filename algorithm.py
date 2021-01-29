#Latitude-широта-y, Longitude-долгота-x
import tifffile
import math
import numpy as np
import glob
import matplotlib.pyplot as plt
from shapeToPNG import shapeToPNG, import_shape
from calcOffsets import calcIntersection

# from  calc_ndvi import getNDVI, show_ndvi

def calc_vegetation(B4, t_corners, path_shape, resolution, show_ndvi):
    '''
        filepath #путь до снимка ландсат без последних двух букв названия снимка(В6)
        path_shape #путь до шейпа района( в названии слова,а не цифры)
    '''
    
    res_folder = 'result/' # не изменяется  
    
    # расчет крайних координат и высоты-широты пнг
    width, height, p_lon_min, p_lon_max, p_lat_min, p_lat_max = import_shape(path_shape, resolution) 
    png_arr = shapeToPNG(path_shape, width, height, res_folder)
    
    p_corners = {"lon_min": p_lon_min, "lon_max": p_lon_max, 
               "lat_min": p_lat_min, "lat_max": p_lat_max}
    
    print("p_corners", p_corners)

    t_offset_x, t_offset_y = calcIntersection(t_corners, p_corners)

    print('final t_offset_x =',t_offset_x,"\n"
          'final t_offset_y =',t_offset_y,"\n")
   
    print('png_arr.shape=', png_arr.shape)
    
    k = B4[t_offset_y:t_offset_y + height, t_offset_x:t_offset_x + width]
    np.putmask(k, png_arr[:,:,0] == 0, np.uint16(0.5*B4[t_offset_y:t_offset_y + height, t_offset_x:t_offset_x + width]))
    # B4[t_offset_y:t_offset_y + height, t_offset_x:t_offset_x + width] = 2*B4[t_offset_y:t_offset_y + height, t_offset_x:t_offset_x + width]
    plt.title(path_shape)
    plt.imshow(B4[t_offset_y:t_offset_y + height, t_offset_x:t_offset_x + width], cmap = 'gray')
    plt.show()

    B4[t_offset_y:t_offset_y + height, t_offset_x:t_offset_x + width] = k
    
    plt.title(path_shape)
    plt.imshow(B4, cmap = 'gray')
    plt.show()
    
    # reflectance_file = glob.glob(filepath + '*.npy')   
    # tiff_arr_cut = show_ndvi[t_offset_y:t_offset_y + height, t_offset_x:t_offset_x + width]
    # np.putmask(tiff_arr_cut, png_arr[:,:,0] != 0,0)
    # print(png_arr.shape,tiff_arr_cut.shape )
    # # print( this_band_arr.shape)
    # print('new band')      
    # plt.title("band")           
    # plt.imshow(tiff_arr_cut, cmap = 'gray') 
    # ozelenenie = np.sum(tiff_arr_cut)
    # print("количество зеленых пикселей",'|','количество зелени в м2 ','|','\n',ozelenenie,'|',ozelenenie*resolution*resolution)
    # return(ozelenenie)


















