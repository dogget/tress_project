import numpy as np
import math

def cornersOffset(b):
    shape = b.shape
    mask = np.zeros(shape)

    np.putmask(mask, b != b[0][0], 1)

    ind_lines = []
    for i in range(shape[0]):
       if np.sum(mask[i,:]) > 0:
           ind_lines.append(i)
           break
       
    for i in range(shape[0]):
       if np.sum(mask[shape[0] - i - 1,:]) > 0:
           ind_lines.append(shape[0] - i - 1)
           break

    ind_columns = []
    for j in range(shape[1]):
       if np.sum(mask[:,j]) > 0:
           ind_columns.append(j)
           break
           
    for j in range(shape[1]):
       if np.sum(mask[:, shape[1] - j - 1]) > 0:
           ind_columns.append(shape[1] - j - 1)
           break

    max_line = max(ind_lines)
    min_line = min(ind_lines)
    max_col = max(ind_columns)
    min_col = min(ind_columns)
    
    print("x: [", min_line,",", max_line,"]; y: [", min_col,",", max_col, "] \n")

    return  (max_line, min_line, max_col, min_col)


def calcIntersection(t_corners, png_corners):
    #наложение снимка ndvi и пнг
    t_lon_min = t_corners["lon_min"][0]
    t_lon_max = t_corners["lon_max"][0]
    t_lat_min = t_corners["lat_min"][0]
    t_lat_max = t_corners["lat_max"][0]
    
    t_width  = t_lon_max - t_lon_min
    t_height = t_lat_max - t_lat_min 
    
    t_minX = t_corners["lon_min"][1]
    t_maxX = t_corners["lon_max"][1]
    t_minY = t_corners["lat_min"][1]
    t_maxY = t_corners["lat_max"][1]
    
    t_width_pix  = t_maxX - t_minX
    t_height_pix = t_maxY - t_minY
    
    print("band width pix:", t_width_pix, ", band height pix:", t_height_pix)
    
    p_lon_min = png_corners["lon_min"]
    p_lon_max = png_corners["lon_max"]
    p_lat_min = png_corners["lat_min"]
    p_lat_max = png_corners["lat_max"]
    
    t_offset_x = t_minX
    t_offset_y = t_minY
    
    px = p_lon_min
    py = p_lat_max
    
    
    #  добавить assert если png не помещается в снимке
    t_offset_x = math.ceil((px - t_lon_min) * t_width_pix / t_width + t_minX )
    t_offset_y = math.ceil((t_lat_max - py) * t_height_pix / t_height + t_minY )
        
    
    return (t_offset_x, t_offset_y)

