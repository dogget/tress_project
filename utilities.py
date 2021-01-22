# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 23:20:42 2020

@author: Alexandra
"""

def getMTL(mtl):
    data={}
    
    with open(mtl) as file:
        for line in file:
            if line.find("GROUP", 0) == -1 and line.find("END", 0) == -1:
                l = line.replace("=","").split()
                data[l[0]] = l[1]
    return data

def getCoordCornersMTL(file_name_mtl): 
    print('работает between_tiff_corner,\n')

    
    data = getMTL(file_name_mtl)
    UR_LAT = float(data['CORNER_UR_LAT_PRODUCT'])
    UR_LON = float(data['CORNER_UR_LON_PRODUCT'])
    UL_LAT = float(data['CORNER_UL_LAT_PRODUCT'])
    UL_LON = float(data['CORNER_UL_LON_PRODUCT'])
    LL_LAT = float(data['CORNER_LL_LAT_PRODUCT'])
    LL_LON = float(data['CORNER_LL_LON_PRODUCT'])
    LR_LAT = float(data['CORNER_LR_LAT_PRODUCT'])
    LR_LON = float(data['CORNER_LR_LON_PRODUCT'])
    
    lat = [UR_LAT, UL_LAT, LL_LAT, LR_LAT]
    
    min_lat = min(lat)
    max_lat = max(lat)
    
    lon = [UR_LON, UL_LON, LL_LON, LR_LON]
    
    min_lon = min(lon)
    max_lon = max(lon)
    
    # print("min lat", min_lat,"\n")
    # print("min_lon",min_lon,"\n")
    # print("max_lat",max_lat,"\n")
    # print("max lon",max_lon,"\n")
    
    return(min_lat, max_lat, min_lon, max_lon)