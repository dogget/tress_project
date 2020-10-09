import numpy as np
import tifffile
def landsat_to_reflectance(path_tiff, path_mtl,index_name):
    print('работает landsat_to_reflectance,\n')

    folder = path_tiff
    folder2 = path_mtl
    data={}
    
    with open(folder2) as file:
        for line in file:
            key, *value = line.split()
            data[key] = value
     
    sun = float(data['SUN_ELEVATION'][1])
            
    for  i in range(9):
        image = tifffile.imread(folder + str(i+1)+'.tif', key=0)
        arr = np.array(image)
        Mult = float(data['REFLECTANCE_MULT_BAND_'+str(i+1)][1])
        Add = float(data['REFLECTANCE_ADD_BAND_'+str(i+1)][1])
        c = arr*Mult + Add
        s = c/np.sin(sun)
        band = np.array(s)
        np.save(index_name + str(i+1), band)

