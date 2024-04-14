#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import modules
import pathlib
import os
import numpy as np
import rasterio as rio
from rasterio.plot import show
from matplotlib import pyplot
from matplotlib import colors, cm
from mpl_toolkits.axes_grid1 import make_axes_locatable
import seaborn as sns

# set style
sns.set_style("white")

# set path
datapath = pathlib.Path(__file__).parent.resolve()
dataset = os.path.join(datapath, 'data', 'elevation.tif')

# read raster
elevation = rio.open(dataset)
z = elevation.read()
z = np.nan_to_num(z)
minimum = 0
maximum = int(np.nanmax(z))
interval = 3
levels = np.arange(minimum, maximum, interval)

# plot raster
fig, ax = pyplot.subplots(figsize=(12, 12))
show(elevation, cmap='cubehelix', ax=ax)
show(
     elevation,
     colors='white',
     contour=True,
     levels=levels,
     linewidths=1,
     ax=ax
     )

# create legend
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="2%", pad=0.1)   
fig.colorbar(
    cm.ScalarMappable(
        norm=colors.Normalize(
            vmin=np.nanmin(z),
            vmax=np.nanmax(z)
            ),
        cmap='cubehelix'),
    cax=cax,
    ax=ax
    )

# save as image
fig.set_size_inches(16, 8.5)
fig.savefig(
    'raster-contours.png',
    dpi=300,
    bbox_inches='tight',
    pad_inches=0.2
    )

ax_list = fig.axes
print(ax_list)

