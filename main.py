import glob
# import numpy as np
from algorithm import calc_vegetation
from landsatToReflectance import landsat_to_reflectance
from calcNDVI import getNDVI
from calcNDVI import show_ndvi

#test_alexandra
#путь до снимка ландсат без последних двух букв названия снимка(В6)
filepath = r'E:/GIS/trees_data/LC08_L1TP_175021_20200409_20200409_01_RT/' 

#2015
# filepath = r'E:/GIS/trees_data/LC08_L1TP_175021_20200409_20200409_01_RT/' 
# reflectance_folder = r'2015' #путь до папки где лежат рефлектансы

#2016
# filepath=r'LC08_L1TP_175020_20160719_20170323_01_T1\LC08_L1TP_175020_20160719_20170323_01_T1_' 
# reflectance_folder = r'2016' #путь до папки где лежат рефлектансы

#2018
# filepath=r'LC08_L1TP_175021_20180623_20180703_01_T1\LC08_L1TP_175021_20180623_20180703_01_T1_' 
# reflectance_folder = r'2018' #путь до папки где лежат рефлектансы

#2020
# filepath=r'LC08_L1TP_175021_20200409_20200409_01_RT\LC08_L1TP_175021_20200409_20200409_01_RT_'
# reflectance_folder = r'2020' #путь до папки где лежат рефлектансы

#поправка на рефлектанс
# reflectance_file = glob.glob(filepath + '*.npy')




# print(reflectance_file)
# print(b4)

# if len(reflectance_file) < 7:
#     landsat_to_reflectance(filepath)

# ndvi_file = glob.glob(filepath + '*ndvi.npy') 
# if len(ndvi_file) == 0:
#     ndvi = getNDVI(filepath)
#     show_ndvi = show_ndvi(ndvi)
#      # посчитать и сохранить на диск ndvi и rgb

# path_shape=r'districts\sovetsky\bigpy.shp'
# path_shape=r'districts\sovetsky\sovetsky.shp' 
    
districs = {'sovetsky': 'sovetsky', 'sormovsky': 'sormovsky', 'prioksky' : 'prioksky', 'nizhegorodsky' : 'nizhegorodsky',
            'moscow' : 'moscow', 'leninsky' : 'leninsky', 'kanavinsky' : 'kanavinsky',
            'avtozavodsky': 'avtozavodsky'}

for name_png in districs:
    
    path_shape=r'districts/'
    shapename = path_shape + name_png + "/" + name_png + ".shp"
    resolution = 30 #разрешение тиффа 
    
    a = calc_vegetation(filepath, shapename, resolution, show_ndvi)