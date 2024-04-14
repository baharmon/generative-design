#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import modules
import pathlib
import os
import rasterio as rio
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style = "whitegrid")

# set path
datapath = pathlib.Path(__file__).parent.resolve()
dataset = os.path.join(datapath, 'data', 'subregion', 'elevation-1ft.tif')

# read raster
raster = rio.open(dataset)

# read raster band as array
z = raster.read(1)
z = np.nan_to_num(z)
u = z.shape[0]
v = z.shape[1]
w = np.nanmax(z)

# create plot
ax = plt.subplot(projection='3d')
mesh_x = np.arange(u)
mesh_y = np.arange(v)
x, y = np.meshgrid(mesh_y, mesh_x)
plot = ax.plot_surface(
    x,
    y,
    z,
    rstride=5,
    cstride=5,
    linewidth=0,
    antialiased=False,
    cmap='cubehelix'
    )

# plot settings
fig = ax.get_figure()
ax.set_xticks(np.arange(0, v, step=250))
ax.set_yticks(np.arange(0, u, step=250))
ax.set_zticks((0,100))
ax.elev = 40 
ax.azim = -45

# # set aspect ratio
ax.set_box_aspect(aspect = (v,u,w))

# save as image
fig.set_size_inches(16, 16)
fig.savefig(
    'raster-surface-1.png',
    dpi=600,
    bbox_inches='tight',
    pad_inches=1
    )



