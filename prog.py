#########Latitude-широта-х,Longitude-долгота-у!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Latitude-широта-y,Longitude-долгота-x
import math
import shapefile
from PIL import Image
from PIL import ImageDraw
import tifffile
import numpy as np
import matplotlib.pyplot as plt
from min_max_coord import import_shape
from shape_png import shape_png
from open_and_show_tiff import open_and_show_tiff
# from mtl_data import mtl_data
from between_tiff_corners import between_tiff_corners
from index_corners import index_corners 
# from offsets_to_png_pix import offsets_to_png_pix

filepath = r'F:\Gis\LC08_L1TP_175021_20200409_20200409_01_RT\LC08_L1TP_175021_20200409_20200409_01_RT_'

path_tiff = filepath + r'B6.TIF'
path_shape = r'F:\Gis\two\two.shp'
path_mtl = filepath + r'MTL.txt'
folder = 'result/'
name_png = 'two'
band = 'B6'


#импорт шейпа
sf = shapefile.Reader(path_shape)
shapes = sf.shapes()
s = sf.shape(0)

##########рассчет крайних координат и высоты-широты пнг
width,height,lon_max,lon_min,lat_min,lat_max = import_shape(path_shape)

##########вывод пнг и массива по пнг
arr = shape_png(path_shape, width, height, folder, name_png)

##########открытие и вывод тиффа
this_band_arr = open_and_show_tiff(path_tiff, band)

########расстояние между углами тифф-картинки в градусах
LR_LAT,UR_LON,LL_LON,UL_LAT,LR_LON,between_ul_lr_lat,between_ll_ur_lon = between_tiff_corners(path_mtl)


#########отступы до снимка
Max_ind_line,Min_ind_line,Max_ind_col,Min_ind_col = index_corners(this_band_arr)



id_x=math.ceil((((lon_min-LL_LON)*(Max_ind_col-Min_ind_col))/(UR_LON-LL_LON)) + Min_ind_col)
id_y=math.ceil((((UL_LAT-lat_max)*(Max_ind_line-Min_ind_line))/(UL_LAT-LR_LAT)) + Min_ind_line)

print(id_x)
print(id_y)


for a in range(0,height ):
    for b in range(0,width):
        if arr[a][b][0]==0 and arr[a][b][1]==0 and  arr[a][b][2]==0:
                        
            this_band_arr[a+id_y][b+id_x]=0
            
            
print('new band')      
plt.title(band)           
plt.imshow(this_band_arr, cmap = 'gray') 
                