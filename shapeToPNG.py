import shapefile
from PIL import Image
from PIL import ImageDraw
import numpy as np

import math
import shapefile

#нахождение расстояния между точками а,б-широта-долгота в МЕТРАХ
def length(a1, b1, a2, b2):
    a1_r = (a1*math.pi)/180
    a2_r = (a2*math.pi)/180
    b1_r = (b1*math.pi)/180
    b2_r = (b2*math.pi)/180
    r = 6371302
    # 6372795 
    
    l_a = abs((a2_r - a1_r))/2
    l_b = abs((b2_r - b1_r))/2
    x = 2*math.asin( (math.sin(l_a)**2 + math.cos(a1_r)*math.cos(a2_r) * math.sin(l_b)**2 ) **0.5 )
    length = x*r # в м
    return length

#импорт шейпа
def import_shape(file_name,resolution):  
    sf = shapefile.Reader(file_name)
    s = sf.shape(0)
    
    lon_max = s.points[0][0]
    lon_min = s.points[0][0]
    lat_min = s.points[0][1]
    lat_max = s.points[0][1]
    #мин макс координаты
    for i in range(0,len(s.points)):
        
        if s.points[i][0] > lon_max:
            lon_max = s.points[i][0]
            
        if s.points[i][0] < lon_min:
            lon_min = s.points[i][0] 
            
        if s.points[i][1] < lat_min:
            lat_min = s.points[i][1]
            
        if s.points[i][1] > lat_max:
            lat_max = s.points[i][1]  
            
    # print(lon_max,"\n")
    # print(lon_min,"\n")
    # print(lat_min,"\n")
    # print(lat_max,"\n")
    
    
    lon_length = length(0, lon_min, 0, lon_max)
    lat_length = length(lat_min, 0, lat_max, 0)
    
    print( 'shape width in meters',  lon_length)
    print( 'shape height in meters', lat_length,"\n")
    
    # print( ' lon_min',lon_min)
    # print( ' lon_max',lon_max)
    # print( ' lat_min',lat_min)
    # print( ' lat_max',lat_max)
    
    width = math.ceil(lon_length/resolution) 
    height = math.ceil(lat_length/resolution)
    
    # print(width, height,"\n")
    print( 'shape width in pixels',  width)
    print( 'shape height in pixels', height,"\n")

    return(width, height, lon_min, lon_max, lat_min, lat_max)



# width,height,lat_max,lon_min=import_shape(r'E:\districts\two\two.shp')
# print(width,height,lat_max,lon_min)

def shapeToPNG(file_name, width, height, res_folder, name_png):  
    # Read in a shapefile
    r = shapefile.Reader(file_name)
    # Geographic x & y distance
    xdist = r.bbox[2] - r.bbox[0]
    ydist = r.bbox[3] - r.bbox[1]
    # Image width & height
    iwidth =  width
    iheight = height
    xratio = iwidth/xdist
    yratio = iheight/ydist
    pixels = []
    for x,y in r.shapes()[0].points:
      px = int(iwidth - ((r.bbox[2] - x) * xratio))
      py = int((r.bbox[3] - y) * yratio)
      pixels.append((px,py))
    img = Image.new("RGB", (iwidth, iheight), "white")
    draw = ImageDraw.Draw(img)
    draw.polygon(pixels, outline="rgb(0, 0, 0)", fill="rgb(0, 0, 0)")
     
    img.save(res_folder + name_png + '.png')
    img = Image.open(res_folder + name_png + '.png')
 
    arr = np.asarray(img, dtype = 'uint8') 
  
    return arr



