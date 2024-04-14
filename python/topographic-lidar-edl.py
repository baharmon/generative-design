#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import modules
import pathlib
import os
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
