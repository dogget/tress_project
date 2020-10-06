from utilities import getMTL

def importMTL(file_name_mtl): 
    
    data = getMTL(file_name_mtl)
    UR_LAT= float(data['CORNER_UR_LAT_PRODUCT'])
    UR_LON= float(data['CORNER_UR_LON_PRODUCT'])
    UL_LAT= float(data['CORNER_UL_LAT_PRODUCT'])
    UL_LON= float(data['CORNER_UL_LON_PRODUCT'])
    LL_LAT= float(data['CORNER_LL_LAT_PRODUCT'])
    LL_LON= float(data['CORNER_LL_LON_PRODUCT'])
    LR_LAT= float(data['CORNER_LR_LAT_PRODUCT'])
    LR_LON= float(data['CORNER_LR_LON_PRODUCT'])
    
    print(UR_LAT,UR_LON,"\n")
    print(UL_LAT,UL_LON,"\n")
    print(LL_LAT,LL_LON,"\n")
    print(LR_LAT,LR_LON,"\n")
    
    return(LR_LAT,UR_LON,LL_LON,UL_LAT,LR_LON)
