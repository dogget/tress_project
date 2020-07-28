import math
from index_corners import index_corners 
from  between_tiff_corners import  between_tiff_corners
from open_and_show_tiff import open_and_show_tiff
from min_max_coord import import_shape


def offsets_to_png_pix(Max_ind_line, Min_ind_line, Max_ind_col, Min_ind_col, lat_max, lon_min, between_ul_lr_lat, between_ll_ur_lon):   
    
    lat_coef = between_ul_lr_lat/(Max_ind_line - Min_ind_line)
    lon_coef = between_ll_ur_lon/(Max_ind_col - Min_ind_col)
        
    
    lat_dif_ul = abs(UL_LAT-lat_max)
    lon_dif_ul = abs(LR_LON-lon_min)
  
    lat_dif_ul_pixels = math.ceil(lat_dif_ul/lat_coef)
    lon_dif_ul_pixels = math.ceil(lon_dif_ul/lon_coef)
    
    print(lat_coef, ' coeficient latitude')
    print(lon_coef, ' coeficient longitude')
    
    
    print('/////////',lat_dif_ul,'//////////')
    print('/////////',lon_dif_ul,'//////////')
    
    # print('/////////')
    
    
    print('/////////',lat_dif_ul_pixels,'//////////')
    print('/////////',lon_dif_ul_pixels,'//////////')
    
    return(lat_dif_ul_pixes, lon_dif_ul_pixes)

# lat_dif_ul_pixes,lon_dif_ul_pixes=offsets_to_png_pix()
# print('//////////////////////////////////////////',lat_dif_ul_pixes,lon_dif_ul_pixes,'///////////////////////////////////////////')