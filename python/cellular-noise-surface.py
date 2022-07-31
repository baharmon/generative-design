# -*- coding: utf-8 -*-
"""
Plot cellular noise as 3D surface
"""

__author__ = "Brendan Harmon"
__copyright__ = 'Copyright 20122, Algorithmic Landscapes'
__email__ =  "brendan.harmon@gmail.com"
__license__ = "GPLv3"
__version__ = "0.0.1"

# import libraries
import pyfastnoisesimd as fns
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# set theme
sns.set_theme(style="whitegrid")

# create plot
ax = plt.subplot(projection='3d')

# set threads
threads = fns.num_virtual_cores()

# set dimensions
i = threads * 100
j = threads * 100
shape = [i, j]

# generate perlin noise
cellular = fns.Noise()
cellular.seed = 1
cellular.noiseType = fns.NoiseType.Cellular
cellular.frequency = 0.01

# set cellular properties
cellular.cell.returnType = fns.CellularReturnType.Distance
cellular.cell.distanceFunc = fns.CellularDistanceFunction.Euclidean
cellular.cell.jitter = 0.45

# set perturbation properties
cellular.perturb.perturbType = fns.PerturbType.Gradient
cellular.perturb.amp = 1.0
cellular.perturb.frequency = 0.5

# plots cellular noise
z = cellular.genAsGrid(shape=shape)
u = np.arange(0, i)
v = np.arange(0, j)
x, y = np.meshgrid(u, v)
plot = ax.plot_surface(x, y, z, cmap='inferno', linewidth=0)

# set axes label
ax.set_xlabel('x', labelpad=10)
ax.set_ylabel('y', labelpad=10)
ax.set_zlabel('z', labelpad=10)
ax.set_zlim3d(-4, 4)

# create legend
fig = ax.get_figure()
ax.view_init(elev=50, azim=45, vertical_axis='z')
fig.colorbar(plot, shrink=0.5, aspect=16)

# save as image
fig.set_size_inches(8.5, 8.5)
fig.savefig(
    'cellular-noise-surface.png',
    dpi=300,
    bbox_inches='tight',
    pad_inches=0
    )
