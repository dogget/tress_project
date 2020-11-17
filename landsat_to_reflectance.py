import numpy as np
import tifffile
import glob
def landsat_to_reflectance(path_tiff):
    print('работает landsat_to_reflectance,\n')
    #  todo хотим только слои 1-9
    tiff_file = glob.glob(filepath + '*.TIF') 
    mtl_file  = glob.glob(filepath + r'*MTL.txt') 
    
    data={}
    with open(mtl_file[0]) as file:
        for line in file:
            key, *value = line.split()
            data[key] = value
     
    sun = float(data['SUN_ELEVATION'][1])
            
    for  file in tiff_file:
        npy_name = file.split('.')[0] + '.npy'
        image = tifffile.imread(file, key=0)
        arr = np.array(image)
        Mult = float(data['REFLECTANCE_MULT_BAND_'+str(i+1)][1])
        Add  = float(data['REFLECTANCE_ADD_BAND_'+str(i+1)][1])
        c = arr*Mult + Add
        s = c/np.sin(sun)
        band = np.array(s)
        np.save(npy_name, band)

