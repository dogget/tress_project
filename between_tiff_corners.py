from mtl_data import mtl_data
data = mtl_data(r'F:\districts\LC08_L1TP_175021_20200409_20200409_01_RT\LC08_L1TP_175021_20200409_20200409_01_RT_MTL.txt')
def between_tiff_corners(file_name_mtl): 
    with open(file_name_mtl) as file:
        for line in file:
            if line.find("GROUP", 0) == -1 and line.find("END", 0) == -1:
                l = line.replace("=","").split()
                data[l[0]] = l[1]
    
    
    UR_LAT= float(data['CORNER_UR_LAT_PRODUCT'])
    UR_LON= float(data['CORNER_UR_LON_PRODUCT'])
    UL_LAT= float(data['CORNER_UL_LAT_PRODUCT'])
    UL_LON= float(data['CORNER_UL_LON_PRODUCT'])
    LL_LAT= float(data['CORNER_LL_LAT_PRODUCT'])
    LL_LON= float(data['CORNER_LL_LON_PRODUCT'])
    LR_LAT= float(data['CORNER_LR_LAT_PRODUCT'])
    LR_LON= float(data['CORNER_LR_LON_PRODUCT'])
    
    print(UR_LAT,UR_LON)
    print(UL_LAT,UL_LON)
    print(LL_LAT,LL_LON)
    print(LR_LAT,LR_LON)
    

    
    
    
    between_ul_lr_lat=abs(UL_LAT-LR_LAT)
    between_ll_ur_lon=abs(UR_LON-LL_LON)
    
    return(LR_LAT,UR_LON,LL_LON,UL_LAT,LR_LON,between_ul_lr_lat,between_ll_ur_lon)
