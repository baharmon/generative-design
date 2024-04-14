# r: rasterio, numpy

# import modules
import os
import rasterio as rio
import numpy as np
import rhinoscriptsyntax as rs

# set path
data = os.path.normpath('X:\python\dev\elevation.tif')

# read raster
raster = rio.open(data)

# read raster band as array
band = raster.read(1)




# # generate point cloud
# rs.AddPointCloud(points)

# conda update conda
# conda install -c conda-forge rasterio
