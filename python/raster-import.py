#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import modules
import pathlib
import os
import rasterio as rio
from rasterio.plot import show

# set path
datapath = pathlib.Path(__file__).parent.resolve()
dataset = os.path.join(datapath, 'data', 'elevation.tif')

# read raster
elevation = rio.open(dataset)

# print coordinate reference system
print(elevation.crs)

# plot raster
show(elevation, cmap='cubehelix')