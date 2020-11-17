import shapefile
from PIL import Image
from PIL import ImageDraw
import numpy as np
from min_max_coord import import_shape
import matplotlib.pyplot as plt

def shape_png(file_name, width, height, res_folder, name_png):
    print('работает shape_png,\n')  
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
    
    
    img.save(res_folder+name_png+'.png')
    img = Image.open(res_folder+name_png+'.png')
 
    arr = np.asarray(img, dtype='uint8')
    print(arr.shape)
   
  
    return arr



