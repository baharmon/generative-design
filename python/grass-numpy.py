import grass.script as grass
import grass.script.array as garray

map = "elevation"

# read map
a = garray.array(map)

# get raster map info
print(grass.raster_info(map)['datatype'])
i = grass.raster_info(map)

# get computational region info
c = grass.region()
print("rows: %d" % c['rows'])
print("cols: %d" % c['cols'])
