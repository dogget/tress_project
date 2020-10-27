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
from landsat_to_reflectance import landsat_to_reflectance
from  Images_v2 import getNDVI
from  Images_v2 import show_ndvi

def raschet_procenta_ozelenenia(filepath,path_shape,reflectance_folder,name_png,resolution):
    # filepath = r'F:\trees_data\districts\LC08_L1TP_175021_20200409_20200409_01_RT\LC08_L1TP_175021_20200409_20200409_01_RT_' #путь до снимка ландсат без последних двух букв названия снимка(В6)
    # file_reflectance = filepath + r'B' # не изменяется
    # path_tiff = filepath + r'B6.TIF' #не изменяется
    # path_shape = r'F:\trees_data\districts\seven\seven.shp' #путь до шейпа района( в названии слова,а не цифры)
    # reflectance_name='\landsat_B' #не изменяется
    # reflectance_folder = r'F:\trees_data\indexes' + reflectance_name #путь до папки где лежат рефлектансы
    
    
    filepath =  filepath #путь до снимка ландсат без последних двух букв названия снимка(В6)
    
    file_reflectance = filepath + r'B' # не изменяется
    path_tiff = filepath + r'B6.TIF' #не изменяется
    path_shape = path_shape #путь до шейпа района( в названии слова,а не цифры)
    reflectance_name='\landsat_B' #не изменяется
    reflectance_folder_name =reflectance_folder + reflectance_name #путь до папки где лежат рефлектансы
    
    # filepath = r'E:\GIS\trees_data\LC08_L1TP_175021_20200409_20200409_01_RT_'
    
    # path_tifilepath + r'B6.TIF'
    # path_shape = r'E:\GIS\trees_data\two\two.shp'f = f
    
    path_mtl = filepath + r'MTL.txt' # не изменяется
    folder = 'result/' # не изменяется
    name_png = 'seven' #
    band = 'B6'# не изменяется  
    
    
    #импорт шейпа
    sf = shapefile.Reader(path_shape)
    shapes = sf.shapes()
    s = sf.shape(0)
    
    # расчет крайних координат и высоты-широты пнг
    width,height, lon_max, lon_min, lat_min, lat_max = import_shape(path_shape,resolution)
    
    #вывод пнг и массива по пнг
    png_arr = shape_png(path_shape, width, height, folder, name_png)
    # arr = np.rollaxis(arr, 1, 0)
    
    plt.title("region")
    plt.imshow(png_arr , cmap = 'gray')
    plt.show()
    
    print( 'WIDTH',width,"\n",'HEIGHT',height,"\n")
    
    
    # открытие и вывод тиффа
    # this_band_arr = open_and_show_tiff(path_tiff, band)
    tiff_arr = tifffile.imread(path_tiff, key=0)
    tiff_arr = np.array(tiff_arr)
    
    # расстояние между углами тифф-картинки в градусах
    LR_LAT, UR_LON, LL_LON, UL_LAT, LR_LON = importMTL(path_mtl)
    
    t_lon_max = UR_LON
    t_lon_min = LL_LON
    t_lat_min = LR_LAT 
    t_lat_max = UL_LAT
    
    #поправка на рефлектанс
    # q=landsat_to_reflectance(file_reflectance,path_mtl,reflectance_name,reflectance_folder)
    
    #вызов В4 и В5 из рефлектанса 
    refolder = reflectance_folder_name
    b4 = np.load(refolder + '4.npy')
    b5 = np.load(refolder + '5.npy')
    ndvi=getNDVI(b5,b4)
    arr_ndvi=show_ndvi(ndvi)
    print(type(arr_ndvi))
    np.save('ndvi-prog',arr_ndvi)
    #отступы до снимка
    Max_IdX, Min_IdX, Max_IdY, Min_IdY = index_corners(tiff_arr)
    
    #наложение снимка ndvi и пнг
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
    
    
    print( tiff_arr.shape,"\n")
    print('p_offset_y=',p_offset_y,"\n"
          't_offset_y=',t_offset_y,"\n"
          'intersect_height=',intersect_height,"\n")
    print('t_offset_x=',t_offset_x,"\n"
          'p_offset_x=',p_offset_x,"\n"
          'intersect_width=',intersect_width,"\n")
    print('png_arr.shape=',png_arr.shape)
    
    
    
    
    tiff_arr_cut=arr_ndvi[t_offset_y:t_offset_y+height,t_offset_x:t_offset_x+width]
    np.putmask(tiff_arr_cut,png_arr[:,:,0]!=0,0)
    print(png_arr.shape,tiff_arr_cut.shape )
    # print( this_band_arr.shape)
    print('new band')      
    plt.title(band)           
    plt.imshow(tiff_arr_cut, cmap = 'gray') 
    ozelenenie=np.sum(tiff_arr_cut)
    print("количество зеленых пикселей",'|','количество зелени в м2 ','|','год ','\n',ozelenenie,'|',ozelenenie*resolution*resolution,'|',reflectance_folder)
    return(ozelenenie)


















