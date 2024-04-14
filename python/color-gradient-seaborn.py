#!/usr/bin/env python

"""
Plot color gradient from Seaborn
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

# set style
sns.set(style = "dark")

# generate gradient
gradient = sns.color_palette("icefire", as_cmap=True)
gradient = [gradient(np.arange(gradient.N))]

# plot gradient
ax = plt.subplot()
ax.set(xticklabels=[], yticklabels=[])
ax.imshow(gradient, aspect=20)