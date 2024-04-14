# -*- coding: utf-8 -*-
"""
Plot fullpage random matrix
"""

__author__ = "Brendan Harmon"
__copyright__ = 'Copyright 20122, Algorithmic Landscapes'
__email__ =  "brendan.harmon@gmail.com"
__license__ = "GPLv3"
__version__ = "0.0.1"

# import libraries
import seaborn as sns
import matplotlib.pyplot as plt
from numpy.random import default_rng

# set theme
sns.set_theme(style="white")

# create plot
ax = plt.subplot()

# generate random matrix
width = 8.25
height = 11
u = int(height * 20)
v = int(width * 20)
rng = default_rng(1234)
z = rng.random((u, v))
# z = rng.laplace(0, 1,(u, v))

# generate heatmap
sns.heatmap(
    z, 
    cmap='viridis',  
    cbar=False, 
    yticklabels=False, 
    xticklabels=False,
    square=True
    )

# save as image
fig = ax.get_figure()
fig.set_size_inches(width, height)
fig.savefig('random-page-xl.png', dpi=1600, bbox_inches='tight', pad_inches=0)

