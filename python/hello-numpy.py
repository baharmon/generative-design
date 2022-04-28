"""Hops Server for Numpy"""
import ghhops_server as hs
import numpy as np
import rhino3dm

hops = hs.Hops()

# random generator
@hops.component(
    "/random_integer",
    name="RandomInteger",
    nickname="RandomInteger",
    description="Print a random integer with Numpy",
    inputs=[hs.HopsInteger("Range", "Range", "Input Range")],
    outputs=[hs.HopsInteger("Integer", "Integer", "Output Integer")]
)
def random_integer(a):
    x = np.random.randint(a)
    return x

# 1D array
@hops.component(
    "/random_array",
    name="Array",
    nickname="Array",
    description="Generate a random array with Numpy",
    inputs=[hs.HopsInteger("Range", "Range", "Input Range")],
    outputs=[hs.HopsInteger("Output", "Output", "Output")]
)
def random_array(z):
    x = np.random.randint(z, size=(10))
    return x.tolist()

# 2D array
@hops.component(
    "/random_array_2D",
    name="Array",
    nickname="Array",
    description="Generate a random 2D array with Numpy",
    inputs=[hs.HopsInteger("Range", "Range", "Input Range")],
    outputs=[hs.HopsInteger("Output", "Output", "Output")]
)
def random_array_2D(i):
    u = np.random.randint(i, size=(4, 4))
    v = np.ravel(u).tolist()
    return v
# add size x and y inputs
# try numbers instead of integers
# add random seed


# points from 2D array
@hops.component(
    "/random_points",
    name="randomPoints",
    nickname="randomPoints",
    description="Generate a random 2D array with Numpy",
    inputs=[
        hs.HopsInteger("Range", "Range", "Input Range"),
        hs.HopsInteger("X", "X", "X Size"),
        hs.HopsInteger("Y", "Y", "Y Size")
    ],
    outputs=[hs.HopsPoint("Points", "Points", "Output Points")]
)
def random_points(i, u , v):
    # xyz values from 2D array
    w = np.random.randint(i, size=(u, v))
    a, b = np.mgrid[:u, :v]
    xyz = np.column_stack((a.ravel(),b.ravel(), w.ravel()))
    x, y, z = np.split(xyz, 3, 1)
    x = (x.ravel().tolist())
    y = (y.ravel().tolist())
    z = (z.ravel().tolist())
    points = rhino3dm.Point3d(x, y, z)
    return points

# x, y, z values should be floats

# 1. Exception occured in handler:
# __init__(): incompatible constructor arguments. The following argument types are supported:
#     1. rhino3dm._rhino3dm.Point3d(x: float, y: float, z: float)
#
# Invoked with: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [89, 73, 21, 27, 36, 47, 98, 43, 26, 37, 76, 73, 68, 29, 76, 4, 87, 37, 74, 45, 45, 72, 55, 93, 94, 34, 16, 80, 60, 90, 73, 28, 5, 62, 40, 72, 18, 86, 75, 29, 82, 34, 17, 4, 89, 82, 63, 52, 0, 6, 93, 82, 66, 20, 4, 42, 82, 46, 54, 86, 1, 70, 73, 84, 46, 81, 26, 21, 44, 12, 3, 43, 9, 6, 54, 78, 66, 18, 56, 93, 40, 66, 83, 79, 41, 7, 71, 14, 46, 84, 21, 5, 23, 33, 70, 65, 0, 26, 33, 77]
#   File "D:\generative-design\python\hello-numpy.py", line 74, in random_points
#     points = rhino3dm.Point3d(x, y, z)




# points from 2D array

# points from 3D array

# mesh from 3D array

# surface from 3D array

# n.b.: path, name, and definition should match

if __name__ == "__main__":
    hops.start(debug=True)
