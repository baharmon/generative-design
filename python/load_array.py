#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 22:45:04 2022

@author: brendanharmon
"""

import pathlib
import os
import numpy as np

# set path
dirpath = pathlib.Path(__file__).parent.resolve()
binary = os.path.join(dirpath, 'elevation.npy')

# load numpy binary
data = np.load(binary)

# print array properties
dim = data.ndim
shape = data.shape
datatype = data.dtype
print(f"dimensions: {dim}" )
print(f"shape: {shape}")
print(f"dtype: {datatype}")

