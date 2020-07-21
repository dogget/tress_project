import math
from index_corners import index_corners 
from  between_tiff_corners import  between_tiff_corners
from open_and_show_tiff import open_and_show_tiff
from min_max_coord import import_shape

width,height,lat_max,lon_min=import_shape(r'E:\districts\two\two.shp')
this_band_arr=open_and_show_tiff(r'F:\districts\LC08_L1TP_175021_20200409_20200409_01_RT\LC08_L1TP_175021_20200409_20200409_01_RT_B6.TIF')
a=index_corners(this_band_arr )
UL_LAT,LR_LON,between_ul_lr_lat,between_ll_ur_lon=between_tiff_corners(r'F:\districts\LC08_L1TP_175021_20200409_20200409_01_RT\LC08_L1TP_175021_20200409_20200409_01_RT_MTL.txt')

def offsets_to_png_pix():   
    
    Max_ind_line=a[0]
    Min_ind_line=a[1]
    Max_ind_col=a[2]
    Min_ind_col=a[3]
    
    
    lat_coef=between_ul_lr_lat/(Max_ind_line-Min_ind_line)
    lon_coef=between_ll_ur_lon/(Max_ind_col-Min_ind_col)
        
    
    lat_dif_ul=abs(UL_LAT-lat_max)
    lon_dif_ul=abs(LR_LON-lon_min)
  
    lat_dif_ul_pixes=math.ceil(lat_dif_ul/lat_coef)
    lon_dif_ul_pixes=math.ceil(lon_dif_ul/lon_coef)
    
    print(lat_coef)
    print(lon_coef)
    
    
    print('/////////',lat_dif_ul,'//////////')
    print('/////////',lon_dif_ul,'//////////')
    
    # print('/////////')
    
    
    print('/////////',lat_dif_ul_pixes,'//////////')
    print('/////////',lon_dif_ul_pixes,'//////////')
    return(lat_dif_ul_pixes,lon_dif_ul_pixes)

# lat_dif_ul_pixes,lon_dif_ul_pixes=offsets_to_png_pix()
# print('//////////////////////////////////////////',lat_dif_ul_pixes,lon_dif_ul_pixes,'///////////////////////////////////////////')