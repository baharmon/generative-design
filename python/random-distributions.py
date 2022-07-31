# -*- coding: utf-8 -*-
"""
Plot barchart of random numbers
"""

__author__ = "Brendan Harmon"
__copyright__ = 'Copyright 20122, Algorithmic Landscapes'
__email__ =  "brendan.harmon@gmail.com"
__license__ = "GPLv3"
__version__ = "0.0.1"

# import libraries
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# set theme
sns.set_theme(style="darkgrid")

# initialize random number generator
rng = np.random.default_rng(1234)

# plot random integers
z = rng.integers(1, 100, 1000)
ax = sns.displot(
    x=z, color='black',
    discrete=True,
    height=2,
    aspect=5/1
    )
# ax.set(ylabel=None)
plt.savefig(
    'random-integer-distribution.pdf',
    dpi=300,
    bbox_inches='tight',
    pad_inches=0
    )

# plot normal distribution
z = rng.normal(0, 10, 1000) 
ax = sns.displot(
    x=z, color='black',
    discrete=True,
    height=2,
    aspect=5/1
    )
# ax.set(ylabel=None)
plt.savefig(
    'random-normal-distribution.pdf',
    dpi=300,
    bbox_inches='tight',
    pad_inches=0
    )

# plot normal distribution
z = rng.poisson(10, 100)
ax = sns.displot(
    x=z, color='black',
    discrete=True,
    height=2,
    aspect=5/1
    )
# ax.set(ylabel=None)
plt.savefig(
    'random-poisson-distribution.pdf',
    dpi=300,
    bbox_inches='tight',
    pad_inches=0
    )

# plot laplace distribution
z = rng.laplace(0, 10, 1000)
ax = sns.displot(
    x=z, color='black',
    discrete=True,
    height=2,
    aspect=5/1
    )
# ax.set(ylabel=None)
plt.savefig(
    'random-laplace-distribution.pdf',
    dpi=300,
    bbox_inches='tight',
    pad_inches=0
    )




