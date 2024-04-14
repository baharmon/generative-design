# requirements: lazrs, laspy
import laspy
import rhinoscriptsyntax as rs

if Run:

    # read lidar
    las = laspy.read(Path)

    # decimate point cloud
    xyz = las.xyz[::10]

    # generate point cloud
    cloud = rs.AddPointCloud(xyz)

    # scale point cloud
    origin = xyz[0]
    scale = (1, 1, 2)
    cloud = rs.ScaleObject(cloud, origin, scale)

    # return points
    Points = rs.PointCloudPoints(cloud)