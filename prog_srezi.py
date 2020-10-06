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
from between_tiff_corners import importMTL
from index_corners import index_corners 
# from calc_indexes import getNDVI
from landsat_to_reflectance import landsat_to_reflectance
# from offsets_to_png_pix import offsets_to_png_pix
from  Images_v2 import getNDVI
from  Images_v2 import show_ndvi

filepath = r'F:\trees_data\districts\LC08_L1TP_175021_20200409_20200409_01_RT\LC08_L1TP_175021_20200409_20200409_01_RT_'
file_reflectance=r'F:\trees_data\districts\LC08_L1TP_175021_20200409_20200409_01_RT\LC08_L1TP_175021_20200409_20200409_01_RT_B'
path_tiff = filepath + r'B6.TIF'
path_shape = r'F:\trees_data\districts\two\two.shp'
index_name='\landsat_B'
index_folder = r'F:\trees_data\indexes' + index_name
# filepath = r'E:\GIS\trees_data\LC08_L1TP_175021_20200409_20200409_01_RT_'

# path_tifilepath + r'B6.TIF'
# path_shape = r'E:\GIS\trees_data\two\two.shp'f = f

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
# arr = np.rollaxis(arr, 1, 0)

plt.title("region")
plt.imshow(arr , cmap = 'gray')
plt.show()

# width = arr.shape[1]
# height = arr.shape[0]
# print(arr.shape)
print( 'NEW','WIDTH',width,"\n",'HEIGHT',height,"\n")
# открытие и вывод тиффа
# this_band_arr = open_and_show_tiff(path_tiff, band)
this_band_arr = tifffile.imread(path_tiff, key=0)
this_band_arr = np.array(this_band_arr)

# расстояние между углами тифф-картинки в градусах
LR_LAT, UR_LON, LL_LON, UL_LAT, LR_LON = importMTL(path_mtl)

t_lon_max = UR_LON
t_lon_min = LL_LON
t_lat_min = LR_LAT 
t_lat_max = UL_LAT

#поправка на рефлекстанс
# q=landsat_to_reflectance(file_reflectance,path_mtl,index_name)


folder = index_folder
    # b1 = np.load(folder + '1.npy')
    # b2 = np.load(folder + '2.npy')
b4 = np.load(folder + '4.npy')
b5 = np.load(folder + '5.npy')
ndvi=getNDVI(b4,b5,index_folder)
show_ndvi=show_ndvi(ndvi)


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
    intersect_width = min(width, Max_IdX - t_offset_x)
else:
    t_offset_x = 0
    p_offset_x = width-math.ceil((lon_min - t_lon_min) * (Max_IdX - Min_IdX) / (t_lon_max - t_lon_min) + Min_IdX )
    intersect_width = min(0, width-p_offset_x)

if(t_lat_max == lat_max):
    p_offset_y = 0
    t_offset_y = 0
    intersect_height = height
elif (t_lat_max < lat_max):
    t_offset_y = 0
    p_offset_y = height -  math.ceil((t_lat_max-lat_max ) * (Max_IdY - Min_IdY) / (t_lat_max - t_lat_min) + Min_IdY )
    intersect_height = min(0, height-p_offset_y)
else:
    p_offset_y = 0
    t_offset_y = math.ceil((t_lat_max-lat_max ) * (Max_IdY - Min_IdY) / (t_lat_max - t_lat_min) + Min_IdY )
    intersect_height = min(height, Max_IdY -t_offset_y)


print( this_band_arr.shape,"\n")
print('p_offset_y=',p_offset_y,"\n"
      't_offset_y=',t_offset_y,"\n"
      'intersect_height=',intersect_height,"\n")
print('t_offset_x=',t_offset_x,"\n"
      'p_offset_x=',p_offset_x,"\n"
      'intersect_width=',intersect_width,"\n")
print('arr.shape=',arr.shape)

# for a in range(0,intersect_width):
#     for b in range(0,intersect_height):
#         if arr[a + p_offset_x][b + p_offset_y][0]==0 and arr[a + p_offset_x][b + p_offset_y][1]==0 and  arr[a + p_offset_x][b + p_offset_y][2]==0:
#             this_band_arr[a + t_offset_x][b + t_offset_y] = 0





# arr_cut=this_band_arr[t_offset_x,t_offset_y:t_offset_x+width,t_offset_y+height]

arr_cut=this_band_arr[t_offset_y:t_offset_y+height,t_offset_x:t_offset_x+width]
np.putmask(arr_cut,arr[::0]==1,1)
print(arr.shape,arr_cut.shape )
# print( this_band_arr.shape)
print('new band')      
plt.title(band)           
plt.imshow(arr_cut, cmap = 'gray') 




















