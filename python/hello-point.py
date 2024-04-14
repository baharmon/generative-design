#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import libraries
import matplotlib.pyplot as plt

# set coordinates
x = 0
y = 0
z = 0

# print coordinates
print(x, y, z)

# create plot
ax = plt.subplot(projection='3d')

# plot coordinates
plot = ax.scatter(x, y, z, c='black', s=100)

# set axes label
ax.set_xlabel('x', labelpad=10)
ax.set_ylabel('y', labelpad=10)
ax.set_zlabel('z', labelpad=10)

# create figure
fig = ax.get_figure()

# save as image
fig.set_size_inches(8.5, 8.5)
fig.savefig('point.png', dpi=300, bbox_inches='tight', pad_inches=0)