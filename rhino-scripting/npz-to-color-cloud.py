# requirements: numpy, matplotlib
import numpy as np
import rhinoscriptsyntax as rs

# set path
dataset = r'D:\generative-design\python\dev\data\elevation.npz'

# load array
array = np.load(dataset)
xyz = array['xyz']
rgb = array['rgb'].tolist()

# sort points by elevation
xyz = xyz[xyz[:, 2].argsort()]

# generate colored point cloud
rs.AddPointCloud(xyz, rgb)