#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import modules
import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style = "whitegrid")

# instantiate random number generator
rng = np.random.default_rng(9)

# generate random points
low = 0
high = 10
n = 100
x = rng.integers(low=low, high=high, size=n)
y = rng.integers(low=low, high=high, size=n)
z = rng.integers(low=low, high=high, size=n)
points = np.column_stack((x, y, z))
print(points)

# plot points
ax = plt.subplot(projection='3d')
plot = ax.scatter(x, y, z, c=z, cmap='viridis', alpha=1, s=100)
ax.set_xlabel('x', labelpad=10)
ax.set_ylabel('y', labelpad=10)
ax.set_zlabel('z', labelpad=10)
fig = ax.get_figure()

# save scatterplot as image
fig.set_size_inches(8.5, 8.5)
fig.savefig('points.png', dpi=300, bbox_inches='tight', pad_inches=0)

# generate grid
spacing = 1
u = np.arange(low, high, spacing)
v = np.arange(low, high, spacing)
grid_x, grid_y = np.meshgrid(u, v)

# interpolate points
grid = griddata(
    np.column_stack((x, y)),
    z,
    (grid_x, grid_y),
    method='cubic')

# heatmap
ax = plt.subplot()
sns.heatmap(
    grid,
    cmap='viridis',
    cbar=True,
    cbar_kws={"shrink": 0.82},
    yticklabels=False,
    xticklabels=False,
    square=True
    )

# save heatmap as image
fig = ax.get_figure()
fig.set_size_inches(8.5, 8.5)
fig.savefig('grid.png', dpi=300, bbox_inches='tight', pad_inches=0)

# surface
ax = plt.subplot(projection='3d')
plot = ax.plot_surface(grid_x, grid_y, grid, cmap='viridis', linewidth=0.25)
# set axes label
ax.set_xlabel('x', labelpad=10)
ax.set_ylabel('y', labelpad=10)
ax.set_zlabel('z', labelpad=10)

# save surface as image
fig = ax.get_figure()
fig.colorbar(plot, shrink=0.5, aspect=16)
fig.set_size_inches(8.5, 8.5)
fig.savefig('surface.png', dpi=300, bbox_inches='tight', pad_inches=0)

# triangulated mesh
import matplotlib.tri as tri
mesh = tri.Triangulation(x, y)
ax = plt.subplot(projection='3d')
ax.set_aspect('equal')
ax.plot_trisurf(mesh, z, cmap='viridis', linewidth=0)

# save mesh as image
fig = ax.get_figure()
fig.set_size_inches(8.5, 8.5)
fig.savefig('mesh.png', dpi=300, bbox_inches='tight', pad_inches=0)
