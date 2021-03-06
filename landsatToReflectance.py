import numpy as np
import tifffile
import glob
def landsat_to_reflectance(path_tiff, bands):
    print('работает landsat_to_reflectance,\n')
    #  todo хотим только слои 1-9
    tiff_file = glob.glob(path_tiff + '*.TIF') 
    mtl_file  = glob.glob(path_tiff + r'*MTL.txt') 
    
    data={}
    with open(mtl_file[0]) as file:
        for line in file:
            key, *value = line.split()
            data[key] = value
     
    sun = float(data['SUN_ELEVATION'][1])
       
    for  file in tiff_file:
        for b in bands:
            if file.find("_B" + str(b))>=0:
                npy_name = file.split('.')[0] + '.npy'
                number= file.split('.')[0][-1:]
                print(number)
        
                arr = tifffile.imread(file, key=0)
                # print(type(image))
                # continue
                # arr = np.array(image)
                
               
                Mult = float(data['REFLECTANCE_MULT_BAND_'+ number][1])
                Add  = float(data['REFLECTANCE_ADD_BAND_'+ number][1])
                c = arr*Mult + Add
                arr=None
                s = c/np.sin(sun)
                c=None
                # band = np.array(s)
                np.save(npy_name, s)
                s = None