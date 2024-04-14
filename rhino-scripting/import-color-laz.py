# requirements: lazrs, laspy, numpy
import laspy
import numpy as np
import rhinoscriptsyntax as rs

# set path
data = r'D:\generative-design\python\dev\data\miniregion\ground-1.laz'

# read lidar
las = laspy.read(data)

# stack colors
rgb = np.column_stack((las.red, las.green, las.blue))

# convert color array to list
rgb = rgb.tolist()

# generate colored point cloud
rs.AddPointCloud(las.xyz, rgb)