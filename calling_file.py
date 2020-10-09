from prog_srezi import raschet_procenta_ozelenenia

filepath=r'F:\trees_data\districts\LC08_L1TP_175021_20200409_20200409_01_RT\LC08_L1TP_175021_20200409_20200409_01_RT_' #путь до снимка ландсат без последних двух букв названия снимка(В6)
path_shape=r'F:\trees_data\districts\seven\seven.shp' #путь до шейпа района( в названии буквы,а не цифры)
reflectance_folder = r'F:\trees_data\indexes' #путь до папки где лежат рефлектансы
name_png = 'seven' #название района

a=raschet_procenta_ozelenenia(filepath,path_shape,reflectance_folder,name_png)