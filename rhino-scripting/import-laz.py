# requirements: lazrs, laspy
import laspy
import rhinoscriptsyntax as rs

# set path
data = r'D:\generative-design\python\dev\data\miniregion\ground-1.laz'

# read lidar
las = laspy.read(data)

# generate point cloud
rs.AddPointCloud(las.xyz)