# -*- coding: utf-8 -*-
"""
Plot dampened sinusoidal waves with the form: y = a sin(bx - c) + e^(-f * x)
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
count = 10
minimum = 0.2
maximum = 0.6
t = 4
a = 2
b = 2
c = 0
d = 0

# plot sinusoidal wave
x = np.linspace(0, t * np.pi, steps)
f = np.linspace(maximum, minimum, count)
for i in f:
    y = a * np.sin(b * x - c) * np.e**(-i * x) + d 
    plot = sns.scatterplot(
        x=x,
        y=y,
        size=x,
        hue=i,
        hue_norm=(minimum, maximum),
        palette='magma',
        legend=False
        )
    fig = plot.get_figure()
    fig.set_size_inches(8.5, 2)
    fig.savefig(
        'dampened-waves.png',
        dpi=300,
        bbox_inches='tight',
        pad_inches=0)