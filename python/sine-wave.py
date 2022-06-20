# -*- coding: utf-8 -*-
"""
Plot a sine wave with the form y=sin(x)
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

# plot sine wave
x = np.linspace(0, 6 * np.pi, 100)
y = np.sin(x)
plot = sns.scatterplot(x=x, y=y, size=x, hue=x, palette='flare', legend=False)
fig = plot.get_figure()
fig.set_size_inches(8.5, 2)
fig.savefig('sine-wave.png', dpi=300, bbox_inches='tight', pad_inches=0)