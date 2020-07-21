import shapefile
from PIL import Image
from PIL import ImageDraw
import numpy as np
from min_max_coord import import_shape

def shape_png(file_name):
    width,height,lat_max,lon_min=import_shape(file_name)
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
    draw.polygon(pixels, outline="rgb(0, 0, 0)", 
                    fill="rgb(0, 0, 0)")
    
    
    img.save("two.png")
    
    img = Image.open(r'C:\Users\USER\Desktop\two.png')
    img.show()
  
    img = Image.open('two.png')
    arr = np.asarray(img, dtype='uint8')
    return(arr)



