#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""using rasterio"""

# import modules
import pathlib
import os
import rasterio as rio
from rasterio.plot import show

# set path
datapath = pathlib.Path(__file__).parent.resolve()
data = os.path.join(datapath, 'elevation.tif')

# read raster
raster = rio.open(data)

# plot raster
show(raster, cmap='cubehelix')

# color maps: vidiris, inferno, terrain, gist_earth, cubehelix

"""using matplotlib"""

# import modules
import pathlib
import os
import rasterio as rio
from matplotlib import pyplot

# set path
datapath = pathlib.Path(__file__).parent.resolve()
data = os.path.join(datapath, 'elevation.tif')

# read raster
raster = rio.open(data)

# plot raster
pyplot.imshow(raster.read(1), cmap='gist_earth')
pyplot.show()


"""using matplotlib for contours"""

# import modules
import pathlib
import os
import rasterio as rio
from matplotlib import pyplot
from rasterio.plot import show

# set path
datapath = pathlib.Path(__file__).parent.resolve()
data = os.path.join(datapath, 'elevation.tif')

# read raster
raster = rio.open(data)

fig, ax = pyplot.subplots(1, figsize=(12, 12))
show((raster, 1), cmap='gist_earth', ax=ax)
show((raster, 1), contour=True, colors='white', ax=ax)
pyplot.show()