# requirements: lazrs, laspy
import laspy
import rhinoscriptsyntax as rs

if Run:

    # read lidar
    las = laspy.read(Path)

    # generate point cloud
    Points = rs.AddPoints(las.xyz)