from grass.pygrass.gis.region import Region
from grass.pygrass.raster import raster2numpy
from grass.pygrass.raster import numpy2raster

pygrass_region = Region()

# Show pygrass region
print(pygrass_region)

# Adjust pygrass region
pygrass_region.south = pygrass_region.south * pygrass_region.nsres
pygrass_region.set_raster_region()

# Show changed pygrass region
print(pygrass_region)

np_array = raster2numpy("elevation")

# Check rows and columns in numpy array
print(np_array.shape)

# Try to write np_array back with the changed region
numpy2raster(np_array, "CELL", "testwrite", overwrite=True)

# Fails, however after:
pygrass_region.write()  # WIND file is changed

numpy2raster(np_array, "CELL", "testwrite", overwrite=True)
# writes properly
