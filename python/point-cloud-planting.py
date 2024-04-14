# requirements: numpy
import numpy as np
import rhinoscriptsyntax as rs

# instantiate random number generator
rng = np.random.default_rng()

# generate x, y, and z values
n = 10
mu = 0 # mean
sigma = 1.5 # standard deviation
x = rng.normal(mu, sigma, n)
y = rng.normal(mu, sigma, n)
z = np.zeros(n)

# interweave coordinates
coordinates = np.column_stack((x, y, z))

# create points
points = rs.AddPoints(coordinates)

# select objects by layer
layer = "polystichum-acrostichoides-01-s"
obj = rs.ObjectsByLayer(layer, True)
obj = rs.GetObjects(
    "Select point cloud",
    rs.filter.pointcloud,
    preselect=True
    )

# loop
mu = 0.75
sigma = 0.25
for point in points:

    # set variables
    angle = rng.uniform(0.0, 360.0)
    factor = np.absolute(rng.normal(mu, sigma))
    scale = (factor, factor, factor)

    # transform
    transform = rs.CopyObject(obj, point)
    transform = rs.RotateObject(transform, point, angle)
    transform = rs.ScaleObject(transform, point, scale)
