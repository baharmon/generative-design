#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import modules
import pathlib
import os
import laspy
import pyvista as pv

# set path
datapath = pathlib.Path(__file__).parent.resolve()
dataset = os.path.join(datapath, 'data', 'subregion', 'ground.laz')

# read lidar
las = laspy.read(dataset)
xyz = las.xyz

# set plot theme
pv.set_plot_theme('document')

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