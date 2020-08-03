#Latitude-широта-y,Longitude-долгота-x
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
from between_tiff_corners import importMTL
from index_corners import index_corners 
# from offsets_to_png_pix import offsets_to_png_pix

filepath = r'F:\Gis\LC08_L1TP_175021_20200409_20200409_01_RT\LC08_L1TP_175021_20200409_20200409_01_RT_'

path_tiff = filepath + r'B6.TIF'
path_shape = r'E:\GIS\trees_data\two\two.shp'
path_mtl = filepath + r'MTL.txt'
folder = 'result/'
name_png = 'two'
band = 'B6'


#импорт шейпа
sf = shapefile.Reader(path_shape)
shapes = sf.shapes()
s = sf.shape(0)

# расчет крайних координат и высоты-широты пнг
width,height, lon_max, lon_min, lat_min, lat_max = import_shape(path_shape)

##########вывод пнг и массива по пнг
arr = shape_png(path_shape, width, height, folder, name_png)

# открытие и вывод тиффа
this_band_arr = open_and_show_tiff(path_tiff, band)

# расстояние между углами тифф-картинки в градусах
LR_LAT, UR_LON, LL_LON, UL_LAT, LR_LON = importMTL(path_mtl)

t_lon_max = UR_LON
t_lon_min = LL_LON
t_lat_min = LR_LAT 
t_lat_max = UL_LAT
#отступы до снимка
Max_IdX, Min_IdX, Max_IdY, Min_IdY = index_corners(this_band_arr)


t_offset_x = 0
t_offset_y = 0
p_offset_x = 0
p_offset_y = 0
intersect_width  = 0
intersect_height = 0

if(t_lon_min == lon_min):
    p_offset_x = 0
    t_offset_x = 0
    intersect_width = width
elif (t_lon_min < lon_min):
    p_offset_x = 0
    t_offset_x = math.ceil((lon_min - t_lon_min) * (Max_IdX - Min_IdX) / (t_lon_max - t_lon_min) + Min_IdX )
    intersect_width = math.min(width, Max_IdX - t_offset_x)
else:
    t_offset_x = 0
    # proportion
    # intersect_width




for a in range(0,intersect_width):
    for b in range(0,intersect_height):
        if arr[a + p_offset_x][b + p_offset_y][0]==0 and arr[a + p_offset_x][b + p_offset_y][1]==0 and  arr[a + p_offset_x][b + p_offset_y][2]==0:
            this_band_arr[a + t_offset_x][b + t_offset_y] = 0
            
            
print('new band')      
plt.title(band)           
plt.imshow(this_band_arr, cmap = 'gray') 
                