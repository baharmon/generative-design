# import modules
import pathlib
import os
import open3d as o3d

# set path
datapath = pathlib.Path(__file__).parent.resolve()
data = os.path.join(datapath, 'data', 'laurus-nobilis-01-l.pcd')

# read point cloud
cloud = o3d.io.read_point_cloud(data, format='pcd')

# render point cloud
o3d.visualization.draw_geometries([cloud])
