# -*- coding: utf-8 -*-
"""
Plot sinusoidal waves
"""

__author__ = "Brendan Harmon"
__copyright__ = 'Copyright 20122, Algorithmic Landscapes'
__email__ =  "brendan.harmon@gmail.com"
__license__ = "GPLv3"
__version__ = "0.0.1"

# import libraries
import numpy as np
import seaborn as sns
sns.set_theme(context='paper', style='darkgrid')

# set variables
steps = 200
count = 12
t = 6
a = 1
b = 1
c = 0.5
d = 0

# plot sinusoidal wave
x = np.linspace(0, t * np.pi, steps)
for i in range(1, count):
    y = (count - i) * np.sin(b * x - i * c) #* np.e**(-i**-1.5 * x) + d
    plot = sns.scatterplot(
        x=x,
        y=y,
        size=x,
        hue=i,
        hue_norm=(1, count),
        palette='flare',
        legend=False
        )
    fig = plot.get_figure()
    fig.set_size_inches(8.5, 2)
    fig.savefig(
        'sinusoidal-waves.png',
        dpi=300,
        bbox_inches='tight',
        pad_inches=0)