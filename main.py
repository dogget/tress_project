import glob
from landsatToReflectance import landsat_to_reflectance
from calcNDVI import getNDVI, show_ndvi
import numpy as np
from shapeToPNG import shapeToPNG_GDAL
import tifffile
import matplotlib.image as mpimg

area_city_m2 = 460000000
city_area_pix = 0
resolution_m2_for_one_pix = 3.4269091860498424
#путь до снимка ландсат без последних двух букв названия снимка(В6)

# prefix = "E:/GIS/trees_data/"
prefix = "D:\other/tress_project\LC08_L1TP_175021_20180623_20180703_01_T1/"
tiffs = {}
# tiffs["test"] = prefix + r'LC08_L1TP_175021_20200409_20200409_01_RT/'

tiffs["test"] = prefix + r'LC08_L1TP_175021_20180623_20180703_01_T1'
# tiffs.append(("2015", prefix + r'LC08_L1TP_175021_20200409_20200409_01_RT/' ))
# tiffs.append(("2016", prefix + r'LC08_L1TP_175020_20160719_20170323_01_T1/' ))
# tiffs.append(("2018", prefix + r'LC08_L1TP_175021_20180623_20180703_01_T1/' ))
# tiffs.append(("2020", prefix + r'LC08_L1TP_175021_20200409_20200409_01_RT/'))
# LC08_L1TP_174021_20130704_20170503_01_T1
# LC08_L1TP_175021_20190813_20190820_01_T1
# LC08_L1TP_175021_20140714_20170421_01_T1
# LC08_L1TP_175021_20180810_20180815_01_T1
# LC08_L1TP_174021_20150827_20170405_01_T1
# LC08_L1TP_174021_20200925_20201005_01_T1
# LC08_L1TP_175020_20160719_20170323_01_T1
# LC08_L1TP_175021_20200409_20200409_01_RT
# LC08_L1TP_175021_20180623_20180703_01_T1
# LC08_L1TP_174021_20150608_20170408_01_T1

# NDVI = (Band 5 – Band 4) / (Band 5 + Band 4)
#   Natural Color (R = 4, G = 3, B = 2)
#   2,3,4,5
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
    
    tiff_file = glob.glob(filepath + '*B5.TIF')[0] 
    band = tifffile.imread(tiff_file, key = 0)    
    
    
    band = np.copy(band)
    
    resolution = 30 #разрешение тиффа 
    districts = {'sovetsky': 'sovetsky', 'sormovsky': 'sormovsky', 'prioksky' : 'prioksky', 'nizhegorodsky' : 'nizhegorodsky',
                'moscow' : 'moscow', 'leninsky' : 'leninsky', 'kanavinsky' : 'kanavinsky',
                'avtozavodsky': 'avtozavodsky'}
    people = {'sovetsky': 148909, 'sormovsky': 166996, 'prioksky' : 94956, 'nizhegorodsky' : 132425,
                'moscow' : 124515, 'leninsky' : 141738, 'kanavinsky' : 158000,
                'avtozavodsky': 300436 }
    ideal_area_km2 = {'sovetsky':31,'sormovsky':100, 'prioksky' : 23, 'nizhegorodsky' :67,
                      'moscow' : 30, 'leninsky' :27,'kanavinsky' : 48, 'avtozavodsky': 94}
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
        # area_km2=area*resolution*resolution/1000000
        ozelenenie = np.sum(t)
        m2 = ozelenenie*resolution*resolution
        area_km2 = resolution_m2_for_one_pix*area/1000000
        print(f, name_png, "pixels = ",ozelenenie ,'в м2 =',m2)
        print(f, name_png,'whole area pix',area, 'whole area km2',area_km2,'(', ideal_area_km2[name_png],')', "procent", ozelenenie * 100/area)
        print(f, name_png, "for one person", m2 / people[name_png])
            
        
        print('складываю')
        city_area_pix += area
# print('area of the city pix',city_area_pix)
# resolution_m2_for_one_pix = area_city_m2 / city_area_pix
# print('resolution_m2_for_one_pix',resolution_m2_for_one_pix)
# sovet_area_m2 = 
 

    # plt.imshow(band[2000:3500, 5900:7800])