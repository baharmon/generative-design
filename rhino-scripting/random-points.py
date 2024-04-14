"""
Generate a random point cloud in Rhino
"""

__author__ = "Brendan Harmon"
__copyright__ = "Copyright 2023, Brendan Harmon"
__email__ =  "brendan.harmon@gmail.com"
__license__ = "MIT"
__version__ = "1.0.0"

# requirements: numpy
import numpy as np
import rhinoscriptsyntax as rs

# instantiate random number generator
rng = np.random.default_rng()

# generate random x, y, and z values
n = 100
x = rng.random(n)
y = rng.random(n)
z = rng.random(n)

# set points from coordinates
points = np.column_stack((x, y, z))

# generate point cloud
rs.AddPointCloud(points)