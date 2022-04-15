"""Hops Server for Numpy"""
import ghhops_server as hs
import numpy as np
# import rhino3dm

hops = hs.Hops()


@hops.component(
    "/randominteger",
    name="RandomInteger",
    nickname="RandomInteger",
    description="Print a random integer with Numpy",
    inputs=[hs.HopsInteger("Range", "Range", "Input Range")],
    outputs=[hs.HopsInteger("Integer", "Integer", "Output Integer")]
)
def hello(a):
    x = np.random.randint(a)
    return x


@hops.component(
    "/randomarray",
    name="Array",
    nickname="Array",
    description="Generate a random array with Numpy",
    inputs=[hs.HopsInteger("Range", "Range", "Input Range")],
    outputs=[hs.HopsInteger("Output", "Output", "Output")]
)
def hello(z):
    x = np.random.randint(z, size=(10))
    return x.tolist()

# points from 2D array

# points from 3D array

# mesh from 3D array

# surface from 3D array

if __name__ == "__main__":
    hops.start(debug=True)
