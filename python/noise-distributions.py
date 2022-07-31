# -*- coding: utf-8 -*-
"""
Plot bar chart of perlin noise
"""

__author__ = "Brendan Harmon"
__copyright__ = 'Copyright 20122, Algorithmic Landscapes'
__email__ =  "brendan.harmon@gmail.com"
__license__ = "GPLv3"
__version__ = "0.0.1"

# import libraries
import pyfastnoisesimd as fns
import numpy as np
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

# generate perlin noise
perlin = fns.Noise()
perlin.noiseType = fns.NoiseType.Perlin
perlin.frequency = 0.05
perlin.seed = 1

# plot perlin noise
grid = perlin.genAsGrid(shape=x)

ax = sns.displot(
    x=grid, color='black',
    bins=np.arange(-0.5, 0.5, 0.01),
    height=2,
    aspect=5/1
    )
ax.set(ylabel=None)
plt.savefig(
    'perlin-distribution.pdf',
    dpi=300,
    bbox_inches='tight',
    pad_inches=0
    )





