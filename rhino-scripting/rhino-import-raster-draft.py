# -*- coding: utf-8 -*-

#! python3

# requirements: locale, numpy, plyfile, lidario

# import modules
import locale
print(locale.getlocale())
locale.setlocale(locale.LC_ALL, 'en_US')
print(locale.getlocale())
import numpy as np
import plyfile
import lidario as lio
import rhinoscriptsyntax as rs

# set path
dataset = r'D:\generative-design\python\dev\data\elevation.tif'

# lidario
translator = lio.Translator("geotiff", "numpy")
xyz = translator.translate(dataset)

# generate point cloud
rs.AddPointCloud(xyz)
