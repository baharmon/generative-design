# requirements: lazrs, laspy
import laspy
import rhinoscriptsyntax as rs

# set path
data = r'D:\generative-design\python\dev\data\white-sands\points.laz'

# read lidar
las = laspy.read(data)

# decimate point cloud
xyz = las.xyz[::10]

# generate point cloud
cloud = rs.AddPointCloud(xyz)

# scale point cloud
origin = xyz[0]
scale = (1, 1, 2)
rs.ScaleObject(cloud, origin, scale)