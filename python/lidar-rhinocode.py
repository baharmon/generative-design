# requirements: lazrs, laspy, numpy
import laspy
import numpy as np
import rhinoscriptsyntax as rs

# set path
data = r'D:\generative-design\python\dev\data\laurus-nobilis-01-l.laz'

# read lidar
las = laspy.read(data)

# convert colors
red = (las.red/256).astype('uint8')
green = (las.green/256).astype('uint8')
blue = (las.blue/256).astype('uint8')

# stack colors
rgb = np.column_stack((red, green, blue)).tolist()

# generate colored point cloud
rs.AddPointCloud(las.xyz, rgb)