import math
import shapefile

#нахождение расстояния между точками а,б-широта-долгота
def length(a1,b1,a2,b2):
    print('работает length,\n')
    a1_r = (a1*math.pi)/180
    a2_r = (a2*math.pi)/180
    b1_r = (b1*math.pi)/180
    b2_r = (b2*math.pi)/180
    r =6371302
    # 6372795 
    
    l_a = abs((a2_r - a1_r))/2
    l_b = abs((b2_r - b1_r))/2
    x = 2*math.asin( (math.sin(l_a)**2 + math.cos(a1_r)*math.cos(a2_r) * math.sin(l_b)**2 ) **0.5 )
    length = x*r # в м
    return length



#перевод длины-ширины в пиксели
def pix(lon_length_m,lat_length_m,resolution_m):
    print('работает pix,\n')
    width=math.ceil(lon_length_m/resolution_m) 
    height=math.ceil(lat_length_m/resolution_m) 
    
    return(width,height)

#импорт шейпа
def import_shape(file_name,resolution):
    print('работает pix,\n')    
    sf = shapefile.Reader(file_name)
    s = sf.shape(0)
    
    lon_max=s.points[0][0]
    lon_min=s.points[0][0]
    lat_min=s.points[0][1]
    lat_max=s.points[0][1]
    #мин макс координаты
    for i in range(0,len(s.points)):
        
        if s.points[i][0] > lon_max:
            lon_max=s.points[i][0]
            
        if s.points[i][0] < lon_min:
            lon_min=s.points[i][0] 
            
        if s.points[i][1] < lat_min:
            lat_min=s.points[i][1]
            
        if s.points[i][1] > lat_max:
            lat_max=s.points[i][1]  
            
    # print(lon_max,"\n")
    # print(lon_min,"\n")
    # print(lat_min,"\n")
    # print(lat_max,"\n")
    
    
    lon_length = length(0, lon_min, 0, lon_max)
    lat_length = length(lat_min, 0, lat_max, 0)
    
    print( ' Length Longitude',lon_length,"\n")
    print( ' Length Latitude',lat_length,"\n")
    
    print( ' lon_min',lon_min,"\n")
    print( ' lon_max',lon_max,"\n")
    print( ' lat_min',lat_min,"\n")
    print( ' lat_max',lat_max,"\n")
    
    
    resolution_m = resolution
    width,height = pix(lon_length, lat_length, resolution_m)   
    # print(width, height,"\n")

    return(width, height, lon_min, lon_max, lat_min, lat_max)



# width,height,lat_max,lon_min=import_shape(r'E:\districts\two\two.shp')
# print(width,height,lat_max,lon_min)