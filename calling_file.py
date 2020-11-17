import glob
from prog_srezi import calc_vegetation
from landsat_to_reflectance import landsat_to_reflectance


name_png = 'sovetsky' #название района
name_png = 'sormovsky' #название района
name_png = 'prioksky' #название района
name_png = 'nizhegorodsky' #название района
name_png = 'moscow' #название района
name_png = 'leninsky' #название района
name_png = 'kanavinsky' #название района
name_png = 'avtozavodsky' #название района

path_shape=r'districts\sovetsky\sovetsky.shp' 
path_shape=r'districts\sormovsky\sormovsky.shp' 
path_shape=r'districts\nizhegorodsky\nizhegorodsky.shp' 
path_shape=r'districts\moscow\moscow.shp' 
path_shape=r'districts\leninsky\leninsky.shp' 
path_shape=r'districts\kanavinsky\kanavinsky.shp' 
path_shape=r'districts\avtozavodsky\avtozavodsky.shp' 
path_shape=r'districts\prioksky\prioksky.shp'


#  test
#путь до снимка ландсат без последних двух букв названия снимка(В6)
filepath = r'E:/GIS/trees_data/LC08_L1TP_175021_20200409_20200409_01_RT/' 

#2015
# filepath=r'LC08_L1TP_174021_20150608_20170408_01_T1\LC08_L1TP_174021_20150608_20170408_01_T1_' #путь до снимка ландсат без последних двух букв названия снимка(В6)
# reflectance_folder = r'2015' #путь до папки где лежат рефлектансы

#2016

# filepath=r'LC08_L1TP_175020_20160719_20170323_01_T1\LC08_L1TP_175020_20160719_20170323_01_T1_' #путь до снимка ландсат без последних двух букв названия снимка(В6)
# reflectance_folder = r'2016' #путь до папки где лежат рефлектансы

#2018
# filepath=r'LC08_L1TP_175021_20180623_20180703_01_T1\LC08_L1TP_175021_20180623_20180703_01_T1_' #путь до снимка ландсат без последних двух букв названия снимка(В6)
# reflectance_folder = r'2018' #путь до папки где лежат рефлектансы


#2020
# filepath=r'LC08_L1TP_175021_20200409_20200409_01_RT\LC08_L1TP_175021_20200409_20200409_01_RT_' #путь до снимка ландсат без последних двух букв названия снимка(В6)
# reflectance_folder = r'2020' #путь до папки где лежат рефлектансы

#поправка на рефлектанс
reflectance_file = glob.glob(filepath + '*.npy')  
print(reflectance_file)
if len(reflectance_file) < 6:
    landsat_to_reflectance(filepath)

ndvi_file = glob.glob(filepath + '*ndvi.npy') 
# if len(ndvi_file) == 0:
#     # посчитать и сохранить на диск ndvi и rgb
resolution = 30 #разрешение тиффа 

a = calc_vegetation(filepath, path_shape, name_png, resolution)