#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import modules
import pathlib
import os
import laspy

# set path
datapath = pathlib.Path(__file__).parent.resolve()
data = os.path.join(datapath, 'data', 'laurus-nobilis-01-l.laz')

# read lidar
las = laspy.read(data)
print(las.xyz)