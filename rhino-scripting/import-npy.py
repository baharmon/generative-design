# requirements: numpy
import numpy as np
import rhinoscriptsyntax as rs

# set path
dataset = r'D:\generative-design\python\dev\data\miniregion\elevation_1ft.npy'

# load array
xyz = np.load(dataset)

# generate point cloud
rs.AddPoints(xyz)
