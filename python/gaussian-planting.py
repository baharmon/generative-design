"""Gaussian Planting"""
#! python 3

# requirements: numpy
import numpy as np
import rhinoscriptsyntax as rs
import scriptcontext as sc
sc.doc = Rhino.RhinoDoc.ActiveDoc

if Run:

    # create empty array
    coordinates = np.empty(shape=[0, 3])

    # loop
    for point in Points:

        # instantiate random number generator
        rng = np.random.default_rng()

        # generate random x, y, and z values
        n = int(Count)
        sigma = float(Deviation) # standard deviation
        x = rng.normal(point[0], sigma, n)
        y = rng.normal(point[1], sigma, n)
        z = np.zeros(n)

        # interweave coordinates
        xyz = np.column_stack((x, y, z))

        # append arrays
        coordinates = np.append(coordinates, xyz, axis=0)

    # create points
    Points = rs.AddPoints(coordinates)

    # loop
    Clouds = []
    for point in Points:

        # set variables
        angle = rng.uniform(0.0, 360.0)
        s = rng.uniform(0.5, 1.0)
        scaling = (s, s, s)

        # transform
        transform = rs.CopyObject(Cloud, point)
        transform = rs.RotateObject(transform, point, angle)
        transform = rs.ScaleObject(transform, point, scaling)
        Clouds.append(transform)