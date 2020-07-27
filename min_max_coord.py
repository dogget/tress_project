import math
import shapefile

#нахождение расстояния между точками
def length(a1,b1,a2,b2):
    
    a1_r = (a1*math.pi)/180
    a2_r = (a2*math.pi)/180
    b1_r = (b1*math.pi)/180
    b2_r = (b2*math.pi)/180
    r = 6372795
    
    l_a = abs((a2_r - a1_r))/2
    l_b = abs((b2_r - b1_r))/2
    x = 2*math.asin( (math.sin(l_a)**2 + math.cos(a1_r)*math.cos(a2_r) * math.sin(l_b)**2 ) **0.5 )
    length = (x*r)/1000 # в км
    return length



#перевод длины-ширины в пиксели
def pix(lon_length,lat_length,coeficient):
    lon_length_m=lon_length*1000
    lat_length_m=lat_length*1000
    
    height=math.ceil(lon_length_m/coeficient) 
    width=math.ceil(lat_length_m/coeficient) 
    return(height,width)

#импорт шейпа
def import_shape(file_name):    
    sf = shapefile.Reader(file_name)
    shapes = sf.shapes()
    s = sf.shape(0)
    
    lon_max=s.points[0][0]
    lon_min=s.points[0][0]
    lat_min=s.points[0][1]
    lat_max=s.points[0][1]
    #мин макс координаты
    for i in range(0,len(s.points)):
        
        if s.points[i][0]>lon_max:
            lon_max=s.points[i][0]
            
        if s.points[i][0]<lon_min:
            lon_min=s.points[i][0] 
            
        if s.points[i][1]<lat_min:
            lat_min=s.points[i][1]
            
        if s.points[i][1]>lat_max:
            lat_max=s.points[i][1]  
            
    print(lon_max)
    print(lon_min)
    print(lat_min)
    print(lat_max)
    
    
    lon_length= length(lon_min,0,lon_max,0)
    lat_length= length(0,lat_min,0,lat_max)
    print('////////////////////////////////////////////////////')
    print(lon_length)
    print(lat_length)
    print('////////////////////////////////////////////////////')
    
    
        
    width,height=pix(lon_length,lat_length,30)   
    print(height,width)
    print('////////////////////////////////////////////////////')

    return(width,height,lat_max,lon_min,lat_min)



# width,height,lat_max,lon_min=import_shape(r'E:\districts\two\two.shp')
# print(width,height,lat_max,lon_min)