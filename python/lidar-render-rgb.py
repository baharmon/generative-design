#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import modules
import pathlib
import os
import numpy as np
import laspy
import pyvista as pv

# set path
datapath = pathlib.Path(__file__).parent.resolve()
data = os.path.join(datapath, 'data', 'magnolia-soulangeana-02-l.laz')

# read lidar
las = laspy.read(data)
xyz = las.xyz

# convert colors
red = (las.red/256).astype('uint8')
green = (las.green/256).astype('uint8')
blue = (las.blue/256).astype('uint8')

# set plot theme
pv.set_plot_theme('document')

# plot with color
rgb = np.column_stack((red, green, blue))
pv.plot(
    xyz,
    scalars=rgb,
    point_size=8,
    window_size=(4000, 4000),
    cpos='xz',
    show_axes=False,
    rgba=True,
    off_screen=True,
    screenshot='magnolia-soulangeana-rgb.png',
    )
