# requirements: numpy
import numpy as np
import rhinoscriptsyntax as rs

# set path
dataset = r'D:\generative-design\python\dev\data\laurus-nobilis-01.npz'

# load array
array = np.load(dataset)

# generate colored point cloud
rs.AddPointCloud(array['xyz'], array['rgb'].tolist())