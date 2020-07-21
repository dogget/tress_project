#########Latitude-широта-х,Longitude-долгота-у
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
from mtl_data import mtl_data
from between_tiff_corners import between_tiff_corners
from index_corners import index_corners 
from offsets_to_png_pix import offsets_to_png_pix
#импорт шейпа
sf = shapefile.Reader(r'E:\districts\two\two.shp')
shapes = sf.shapes()
s = sf.shape(0)

##########рассчет крайних координат и высоты-широты пнг
width,height,lat_max,lon_min=import_shape(r'E:\districts\two\two.shp')

##########вывод пнг и массива по пнг
arr=shape_png(r'E:\districts\two\two.shp')

##########открытие и вывод тиффа
this_band_arr=open_and_show_tiff(r'F:\districts\LC08_L1TP_175021_20200409_20200409_01_RT\LC08_L1TP_175021_20200409_20200409_01_RT_B6.TIF')

#########открыть текстовый файл тиф

data = mtl_data(r'F:\districts\LC08_L1TP_175021_20200409_20200409_01_RT\LC08_L1TP_175021_20200409_20200409_01_RT_MTL.txt')


########расстояние между углами тифф-картинки в градусах
UL_LAT,LR_LON,between_ul_lr_lat,between_ll_ur_lon=between_tiff_corners(r'F:\districts\LC08_L1TP_175021_20200409_20200409_01_RT\LC08_L1TP_175021_20200409_20200409_01_RT_MTL.txt')


#########отступы до пнг
lat_dif_ul_pixes,lon_dif_ul_pixes=offsets_to_png_pix()




for a in range(0,height ):
    for b in range(0,width):
        if arr[a][b][0]==0 and arr[a][b][1]==0 and  arr[a][b][2]==0:
                        
            this_band_arr[a+lon_dif_ul_pixes][b+lat_dif_ul_pixes]=0
            
            
print('new band')      
plt.title('this_band_arr_new')           
plt.imshow(this_band_arr, cmap = 'gray') 
                