# -*- coding: utf-8 -*-
"""
Plot textured sinusoidal waves with the form: y = a sin(bx - c) + d + sin(x)
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
steps = 100
count = 4
minimum = 0.001
maximum = 1.000
t = 2
c = 0
d = 0

# plot sinusoidal wave
x = np.linspace(0, t * np.pi, steps)
a = np.linspace(minimum, maximum, count)
for i in a:
    y = i * np.sin(i**-1 * x - c) + d + np.sin(x)
    plot = sns.scatterplot(
        x=x,
        y=y,
        size=x,
        hue=i,
        hue_norm=(minimum, maximum),
        palette='flare',
        legend=False
        )
    fig = plot.get_figure()
    fig.set_size_inches(8.5, 2)
    fig.savefig(
        'textured-waves.png',
        dpi=300,
        bbox_inches='tight',
        pad_inches=0)