# r: rasterio, numpy

# import modules
import os
import rasterio as rio
import numpy as np
import rhinoscriptsyntax as rs

# set path
data = os.path.normpath('D:\generative-design\python\dev\data\elevation.tif')

# read raster
raster = rio.open(data)

# # window or resample

# from scipy.interpolate import griddata

# # read raster band as array
# band = raster.read(1)
# # print(band)

# # raster x and y
# band = raster.read(1)
# print('Band has shape', raster.shape)
# height = band.shape[0]
# width = band.shape[1]
# cols, rows = np.meshgrid(np.arange(width), np.arange(height))
# xs, ys = rio.transform.xy(raster.transform, rows, cols)
# lons= np.array(xs)
# lats = np.array(ys)
# print('lons shape', lons.shape)


# # generate grid
# spacing = 1
# u = np.arange(low, high, spacing)
# v = np.arange(low, high, spacing)
# grid_x, grid_y = np.meshgrid(u, v)

# # interpolate points
# grid = griddata(
#     np.column_stack((x, y)),
#     z,
#     (grid_x, grid_y),
#     method='cubic')