#Latitude-широта-y, Longitude-долгота-x
import math
import shapefile
import tifffile
import numpy as np
import glob
import matplotlib.pyplot as plt
from min_max_coord import import_shape
from shape_png import shape_png
from between_tiff_corners import importMTL
from index_corners import index_corners 
from  calc_ndvi import getNDVI, show_ndvi

def calc_vegetation(filepath, path_shape, name_png, resolution):
    '''
        filepath #путь до снимка ландсат без последних двух букв названия снимка(В6)
        path_shape #путь до шейпа района( в названии слова,а не цифры)
    '''
    tiff_file = glob.glob(filepath + '*.TIF')
    reflectance_file = glob.glob(filepath + '*.npy')   
    mtl_file = glob.glob(filepath + r'*MTL.txt')[0]
    print(tiff_file)
    print(reflectance_file)
    print(mtl_file)
    
    res_folder = 'result/' # не изменяется  
    
    # расчет крайних координат и высоты-широты пнг
    width, height, p_lon_min, p_lon_max, p_lat_min, p_lat_max = import_shape(path_shape, resolution)
    
    # вывод пнг и массива по пнг
    png_arr = shape_png(path_shape, width, height, res_folder, name_png)
    # arr = np.rollaxis(arr, 1, 0)
    
    plt.title("region")
    plt.imshow(png_arr , cmap = 'gray')
    plt.show()
    
    print( 'WIDTH',width,"\n",'HEIGHT',height,"\n")
    
    # расстояние между углами тифф-картинки в градусах
    LR_LAT, UR_LON, LL_LON, UL_LAT, LR_LON = importMTL(mtl_file)
    
    t_lon_max = UR_LON
    t_lon_min = LL_LON
    t_lat_min = LR_LAT 
    t_lat_max = UL_LAT

    
    #вызов В4 и В5 из рефлектанса 
    b4_n = reflectance_file[0].split('.')[0][:-1] + '4.npy'
    b5_n = reflectance_file[0].split('.')[0][:-1] + '5.npy'
    print(b4_n)
    b4 = np.load(b4_n)
    b5 = np.load(b5_n)
    ndvi = getNDVI(b5,b4)
    show_ndvi(ndvi)
    print("ndvi_0_0", ndvi[0,0])
    print("b4_0_0", b4[0,0])
    #отступы до снимка
    t_max_idx, t_min_idx, t_max_idy, t_min_idy = index_corners(b4)
    
    #наложение снимка ndvi и пнг
    t_offset_x = t_min_idx
    t_offset_y = t_min_idy
    p_offset_x = 0
    p_offset_y = 0
    intersect_width  = 0
    intersect_height = 0
    
    if(t_lon_min == p_lon_min):
        intersect_width = width
    elif (t_lon_min < p_lon_min):
        t_offset_x = math.ceil((p_lon_min - t_lon_min) * (t_max_idx - t_min_idx) / (t_lon_max - t_lon_min) + t_min_idx )
        intersect_width = min(width, t_max_idx - t_offset_x)
    else:
        p_offset_x = width-math.ceil((lon_min - t_lon_min) * (t_max_idx - t_min_idx) / (t_lon_max - t_lon_min) + t_min_idx )
        intersect_width = min(0, width-p_offset_x)
    
    if(t_lat_max == p_lat_max):
        intersect_height = height
    elif (t_lat_max < p_lat_max):
        p_offset_y = height -  math.ceil((t_lat_max-lat_max ) * (t_max_idy - t_min_idy) / (t_lat_max - t_lat_min) + t_min_idy )
        intersect_height = min(0, height-p_offset_y)
    else:
        t_offset_y = math.ceil((t_lat_max-p_lat_max ) * (t_max_idy - t_min_idy) / (t_lat_max - t_lat_min) + t_min_idy )
        intersect_height = min(height, t_max_idy - t_offset_y)
    
    
    print( b4.shape,"\n")
    print('p_offset_y=',p_offset_y,"\n"
          't_offset_y=',t_offset_y,"\n"
          'intersect_height=',intersect_height,"\n")
    print('t_offset_x=',t_offset_x,"\n"
          'p_offset_x=',p_offset_x,"\n"
          'intersect_width=',intersect_width,"\n")
    print('png_arr.shape=',png_arr.shape)
    
    
    
    
    tiff_arr_cut = ndvi[t_offset_y:t_offset_y+height,t_offset_x:t_offset_x+width]
    np.putmask(tiff_arr_cut,png_arr[:,:,0]!=0,0)
    print(png_arr.shape,tiff_arr_cut.shape )
    # print( this_band_arr.shape)
    print('new band')      
    plt.title("band")           
    plt.imshow(tiff_arr_cut, cmap = 'gray') 
    ozelenenie = np.sum(tiff_arr_cut)
    print("количество зеленых пикселей",'|','количество зелени в м2 ','|','год ','\n',ozelenenie,'|',ozelenenie*resolution*resolution)
    return(ozelenenie)


















