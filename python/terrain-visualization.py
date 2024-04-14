#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import modules
import pathlib
import os
import rasterio as rio
from rasterio.plot import show
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style = "whitegrid")

# set path
datapath = pathlib.Path(__file__).parent.resolve()
data = os.path.join(datapath, 'elevation.tif')

# read raster
raster = rio.open(data)

# plot raster
show(raster, cmap='cubehelix')

# read raster band as array
band = raster.read(1)
u = band.shape[0]
v = band.shape[1]
w = np.amax(band)

# create plot
ax = plt.subplot(projection='3d')

mesh_x = np.arange(u)
mesh_y = np.arange(v)
x, y = np.meshgrid(mesh_y, mesh_x)
plot = ax.scatter(x, y, band, c=band, s=1, cmap='cubehelix')

# plot settings
fig = ax.get_figure()
ax.set_xticks(np.arange(0, v, step=250))
ax.set_yticks(np.arange(0, u, step=250))
ax.set_zticks((0,100))
# ax.set_zticks(np.arange(0, w, step=50))
ax.elev = 20 # default: 30
ax.azim = -90  # default -60

# set aspect ratio
ax.set_box_aspect(aspect = (v,u,w))

# save as image
fig.set_size_inches(16, 8.5)
fig.savefig('terrain-scatter.png', dpi=300, bbox_inches='tight', pad_inches=0)
