# requirements: numpy, matplotlib
import numpy as np
import matplotlib as mpl
import rhinoscriptsyntax as rs

# set color map
colormap = 'cubehelix'

# set path
dataset = r'D:\generative-design\python\dev\data\elevation.npy'

# load array
xyz = np.load(dataset)

# generate color gradient
z = xyz[:, 2]
gradient = mpl.colormaps[colormap].resampled(z.size)
rgba = (gradient(range(z.size)) * 255).astype('uint8')
rgb = rgba[:,:-1].tolist()

# sort points by elevation
xyz = xyz[xyz[:, 2].argsort()]

# generate colored point cloud
rs.AddPointCloud(xyz, rgb)
