# -*- coding: utf-8 -*-
"""
Plot 2D matrix of perlin noise
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

# generate perlin noise
perlin = fns.Noise()
perlin.noiseType = fns.NoiseType.PerlinFractal
perlin.frequency = 0.005
perlin.seed = 1

# set fractal properties
perlin.fractal.fractalType = fns.FractalType.Billow
perlin.fractal.octaves = 2
perlin.fractal.lacunarity = 2.1
perlin.fractal.gain = 0.45

# set perturbation properties
perlin.perturb.perturbType = fns.PerturbType.NoPerturb

# plot perlin noise
grid = perlin.genAsGrid(shape=shape)

# generate heatmap
sns.heatmap(
    grid, 
    cmap='viridis', 
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
    'perlin-fractal-billow-noise.png',
    dpi=300,
    bbox_inches='tight',
    pad_inches=0
    )