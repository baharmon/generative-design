#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import modules
import pathlib
import os
import numpy as np
import laspy

# set laz path
directory = pathlib.Path(__file__).parent.resolve()
basename = os.path.join(directory, 'point-cloud')
dataset = r'D:\generative-design\python\dev\data\miniregion\ground-1.laz'

# read lidar
las = laspy.read(dataset)

# convert colors
red = (las.red/256).astype('uint8')
green = (las.green/256).astype('uint8')
blue = (las.blue/256).astype('uint8')
rgb = np.column_stack((red, green, blue))

# export binary
np.savez_compressed(basename, xyz=las.xyz, rgb=rgb)
