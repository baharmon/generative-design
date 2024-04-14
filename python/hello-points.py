#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style = "whitegrid")

# create plot
ax = plt.subplot(projection='3d')

# instantiate random number generator
rng = np.random.default_rng()

# generate random x, y, and z values
n = 100
x = rng.random(n)
y = rng.random(n)
z = rng.random(n)

# print coordinates
for i in range(n):
    print(x[i], y[i], z[i])

# plot points
plot = ax.scatter(x, y, z, c='black', s=100)

# set axes label
ax.set_xlabel('x', labelpad=10)
ax.set_ylabel('y', labelpad=10)
ax.set_zlabel('z', labelpad=10)

# create figure
fig = ax.get_figure()

# save as image
fig.set_size_inches(8.5, 8.5)
fig.savefig('hello-points.png', dpi=300, bbox_inches='tight', pad_inches=0)