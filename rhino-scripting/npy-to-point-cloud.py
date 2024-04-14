# requirements: numpy
import numpy as np
import rhinoscriptsyntax as rs

# set path
dataset = r'D:\generative-design\python\dev\data\elevation.npy'

# load array
xyz = np.load(dataset)

# generate point cloud
rs.AddPointCloud(xyz)
