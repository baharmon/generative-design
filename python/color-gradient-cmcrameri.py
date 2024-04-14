#!/usr/bin/env python

"""
Plot color gradient from Scientific Colours
"""

__author__ = "Brendan Harmon"
__copyright__ = "Copyright 2023, Brendan Harmon"
__email__ =  "brendan.harmon@gmail.com"
__license__ = "MIT"
__version__ = "1.0.0"

# import libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import cmcrameri.cm as cmc

# set style
sns.set(style = "dark")

# generate gradient
gradient = cmc.romaO
gradient = [gradient(np.arange(gradient.N))]

# plot gradient
ax = plt.subplot()
ax.set(xticklabels=[], yticklabels=[])
ax.imshow(gradient, aspect=10)