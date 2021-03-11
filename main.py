import glob
from landsatToReflectance import landsat_to_reflectance
from calcNDVI import getNDVI, show_ndvi
import numpy as np
from shapeToPNG import shapeToPNG_GDAL
import tifffile
import matplotlib.image as mpimg


#путь до снимка ландсат без последних двух букв названия снимка(В6)

prefix = "E:/GIS/trees_data/"

tiffs = {}
tiffs["test"] = prefix + r'LC08_L1TP_175021_20200409_20200409_01_RT/' 
# tiffs.append(("2015", prefix + r'LC08_L1TP_175021_20200409_20200409_01_RT/' ))
# tiffs.append(("2016", prefix + r'LC08_L1TP_175020_20160719_20170323_01_T1/' ))
# tiffs.append(("2018", prefix + r'LC08_L1TP_175021_20180623_20180703_01_T1/' ))
# tiffs.append(("2020", prefix + r'LC08_L1TP_175021_20200409_20200409_01_RT/'))

# NDVI = (Band 5 – Band 4) / (Band 5 + Band 4)
#  Natural Color (R = 4, G = 3, B = 2)
#  2,3,4,5
bands = [2,3,4,5]
for f in tiffs:
    filepath = tiffs[f]
    
    #поправка на рефлектанс
    reflectance_file = glob.glob(filepath + '*.npy')
    
    if len(reflectance_file) < 4:
        landsat_to_reflectance(filepath, bands)
        
    ndvi_file = glob.glob(filepath + '*ndvi.npy') 
    if len(ndvi_file) == 0:
        ndvi = getNDVI(filepath)
    else:
        ndvi = np.load(ndvi_file[0])
    
    show_ndvi = show_ndvi(ndvi, 0.35)
    
    # посчитать и сохранить на диск ndvi и rgb
    
    tiff_file = glob.glob(filepath + '*B6.TIF')[0] 
    band = tifffile.imread(tiff_file, key = 0)    
    
    
    band = np.copy(band)
    
    resolution = 30 #разрешение тиффа 
    districts = {'sovetsky': 'sovetsky', 'sormovsky': 'sormovsky', 'prioksky' : 'prioksky', 'nizhegorodsky' : 'nizhegorodsky',
                'moscow' : 'moscow', 'leninsky' : 'leninsky', 'kanavinsky' : 'kanavinsky',
                'avtozavodsky': 'avtozavodsky'}
    people = {'sovetsky': 148909, 'sormovsky': 166996, 'prioksky' : 94956, 'nizhegorodsky' : 132425,
                'moscow' : 124515, 'leninsky' : 141738, 'kanavinsky' : 158000,
                'avtozavodsky': 300436 }
    
    import matplotlib.pyplot as plt
    plt.imshow(band[2000:3500, 5900:7500])
    plt.show()
    plt.imshow(show_ndvi[2000:3500, 5900:7500])
    plt.show()
    masks = {}
    i  = 0.2
    for name_png in districts:   
        i += 0.05
        
        path_shape=r'districts/'
        shapename = path_shape + name_png + "/" + name_png + ".shp"
        
        png_arr = shapeToPNG_GDAL(shapename, tiff_file)    
        masks[name_png] =  png_arr
        np.putmask(band, png_arr == 0, np.uint16(i*band))
             
        t = np.copy(show_ndvi)
        np.putmask(t, png_arr == 0, 0)
        mpimg.imsave(name_png + f+ 'ndvi.png', t[2100:3400, 5900:7300])
        
        plt.title(f + '_'+ name_png)
        plt.imshow(t[2100:3400, 5900:7300],'Greys')
        plt.show()
     
        area = np.sum(png_arr)
        ozelenenie = np.sum(t)
        m2 = ozelenenie*resolution*resolution
        print(f, name_png, "pixels = ",ozelenenie ,'в м2 =',m2)
        print(f, name_png, ozelenenie, area, "procent", ozelenenie * 100/area)
        print(f, name_png, "for one person", m2 / people[name_png])
            
        
    # plt.imshow(band[2000:3500, 5900:7800])