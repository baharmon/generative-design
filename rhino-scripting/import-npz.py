# requirements: numpy
import numpy as np
import rhinoscriptsyntax as rs

# set path
dataset = r'D:\generative-design\python\dev\data\miniregion\ground-1.npz'

# load array
array = np.load(dataset)

# generate colored point cloud
rs.AddPoints(array['xyz'])