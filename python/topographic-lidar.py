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
dataset = os.path.join(datapath, 'data', 'subregion', 'all.laz')

# read lidar
las = laspy.read(dataset)
xyz = las.xyz

# set plot theme
pv.set_plot_theme('document')

# plot with eye dome lighting
pv.plot(
    xyz,
    point_size=5,
    color='white',
    window_size=(2000, 2000),
    show_axes=False,
    eye_dome_lighting=True,
    off_screen=True,
    screenshot='lidar-edl'
    )

# plot with hypsometric tinting
pv.plot(
    xyz,
    scalars=xyz[:, 2],
    cmap='cubehelix',
    point_size=5,
    ambient=0.4,
    window_size=(2000, 2000),
    eye_dome_lighting=True,
    show_scalar_bar=False,
    show_axes=False,
    off_screen=True,
    screenshot='lidar-hypso.png'
    )

# plot with color
rgb = np.column_stack((las.red, las.green, las.blue))
pv.plot(
    xyz,
    scalars=rgb,
    point_size=5,
    ambient=0.4,
    window_size=(2000, 2000),
    show_axes=False,
    eye_dome_lighting=True,
    rgba=True,
    off_screen=True,
    screenshot='lidar-rgb.png',
    )