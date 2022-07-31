# -*- coding: utf-8 -*-
"""
Plot 2D matrix of cellular noise with gradient perturbation
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

# set theme
sns.set_theme(style="white")

# create plot
ax = plt.subplot()

# set threads
threads = fns.num_virtual_cores()

# set dimensions
x = threads * 100
y = threads * 100
shape = [x, y]

# generate cellular noise
cellular = fns.Noise()
cellular.seed = 1
cellular.noiseType = fns.NoiseType.Cellular
cellular.frequency = 0.02

# set cellular properties
cellular.cell.returnType = fns.CellularReturnType.Distance
cellular.cell.distanceFunc = fns.CellularDistanceFunction.Euclidean
cellular.cell.jitter = 0.45

# set perturbation properties
cellular.perturb.perturbType = fns.PerturbType.Gradient
cellular.perturb.amp = 1.0
cellular.perturb.frequency = 0.7

# plots cellular noise
grid = cellular.genAsGrid(shape=shape)

# generate heatmap
sns.heatmap(
    grid, 
    cmap='inferno', 
    linewidths=0, 
    annot=False, 
    cbar=False, 
    yticklabels=False, 
    xticklabels=False, 
    square=True
    )

# save as image
fig = ax.get_figure()
fig.set_size_inches(8.5, 8.5)
fig.savefig(
    'cellular-gradient-noise.png',
    dpi=300,
    bbox_inches='tight',
    pad_inches=0
    )