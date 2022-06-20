# -*- coding: utf-8 -*-
"""
Plot sinusoidal wave field as voxels
"""

__author__ = "Brendan Harmon"
__copyright__ = 'Copyright 20122, Algorithmic Landscapes'
__email__ =  "brendan.harmon@gmail.com"
__license__ = "GPLv3"
__version__ = "0.0.1"

# import libraries
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style = "whitegrid")

# set variables
u = 10
v = 10
w = 10

# plot voxels
x, y, z = np.indices((u, v, w))
volume = z < w/2 * np.sin(x)*np.cos(y) + w/2
axes = plt.subplot(projection='3d')
norm = mpl.colors.Normalize(vmin=z.min(), vmax=z.max())
colors = plt.cm.inferno(norm(z))
axes.voxels(volume, facecolors=colors, edgecolor='w', linewidth=0.5)

# create legend
legend = plt.cm.ScalarMappable(cmap=plt.cm.inferno, norm=norm)
legend.set_array([])
plt.colorbar(legend, shrink=0.5, aspect=16)

# save as image
fig = axes.get_figure()
fig.set_size_inches(8.5, 8.5)
fig.savefig('wave-voxels.png', dpi=300, bbox_inches='tight', pad_inches=0)