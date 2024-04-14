# requirements: numpy
import numpy as np
import rhinoscriptsyntax as rs

if Run:

    # load array
    xyz = np.load(Path)

    # generate point cloud
    Cloud = rs.AddPointCloud(xyz)