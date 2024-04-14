#!/usr/bin/env python

"""
Plot color gradients
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
import cmocean
from cmcrameri import cm
import cmasher as cmr
sns.set(style = "dark")


def main():

    matplotlib_gradients()
    seaborn_gradients()
    cmocean_gradients()
    scientific_gradients()
    cmasher_gradients()


def matplotlib_gradients():
    """plot a selection of matplotlib color maps"""

    # list color maps
    colormaps = [
        'viridis',
        'inferno',
        'magma',
        'cividis',
        'cubehelix',
        'twilight'
        ]
    
    # loop through color maps
    for colormap in colormaps:
    
        # plot as gradient
        gradient = plt.colormaps[colormap]
        gradient = [gradient(np.arange(gradient.N))]
        ax = plt.subplot()
        ax.set(xticklabels=[], yticklabels=[])
        ax.imshow(gradient, extent=[0, 10, 0, 1])
    
        # save as image
        fig = ax.get_figure()
        fig.savefig(
            f'{colormap}.png',
            dpi=300,
            bbox_inches='tight',
            pad_inches=0
            )


def seaborn_gradients():
    """plot a selection of seaborn color maps"""
    
    # list color maps
    colormaps = [
        'icefire',
        'mako',
        'rocket',
        'flare',
        'crest'
        ]
    
    # loop through color maps
    for colormap in colormaps:

        # plot as gradient
        gradient = sns.color_palette(colormap, as_cmap=True)
        gradient = [gradient(np.arange(gradient.N))]
        ax = plt.subplot()
        ax.set(xticklabels=[], yticklabels=[])
        ax.imshow(gradient, extent=[0, 10, 0, 1])
    
        # save as image
        fig = ax.get_figure()
        fig.savefig(
            f'{colormap}.png',
            dpi=300,
            bbox_inches='tight',
            pad_inches=0
            )


def cmocean_gradients():
    """plot a selection of cmocean color maps"""

    # list color maps
    colormaps = [
        'delta',
        'deep',
        'dense',
        'ice',
        'turbid',
        'rain'
        ]
    
    # loop through color maps
    for colormap in colormaps:

        # plot as gradient
        gradient = getattr(cmocean.cm, colormap)
        gradient = [gradient(np.arange(gradient.N))]
        ax = plt.subplot()
        ax.set(xticklabels=[], yticklabels=[])
        ax.imshow(gradient, extent=[0, 10, 0, 1])
    
        # save as image
        fig = ax.get_figure()
        fig.savefig(
            f'{colormap}.png',
            dpi=300,
            bbox_inches='tight',
            pad_inches=0
            )


def scientific_gradients():
    """plot a selection of scientific color maps"""

    # list color maps
    colormaps = [
        'batlow',
        'glasgow',
        'hawaii',
        'oslo',
        'devon',
        'davos',
        'acton',
        'lipari',
        'buda',
        'lajolla',
        'bilbao',
        'turku',
        'navia',
        'imola',
        'nuuk',
        'bamako',
        'lapaz',
        'tokyo',
        'berlin',
        'roma',
        'managua',
        'oleron',
        'romaO',
        'batlowS'
        ]

    # loop through color maps
    for colormap in colormaps:

        # plot as gradient
        gradient = getattr(cm, colormap)
        gradient = [gradient(np.arange(gradient.N))]
        ax = plt.subplot()
        ax.set(xticklabels=[], yticklabels=[])
        ax.imshow(gradient, extent=[0, 10, 0, 1])
    
        # save as image
        fig = ax.get_figure()
        fig.savefig(
            f'{colormap}.png',
            dpi=300,
            bbox_inches='tight',
            pad_inches=0
            )


def cmasher_gradients():
    """plot a selection of cmasher color maps"""

    # list color maps
    colormaps = [
        'swamp',
        'jungle',
        'rainforest',
        'savanna',
        'ocean',
        'seaweed',
        'freeze',
        'fall',
        'seasons_s',
        'horizon',
        'copper_s',
        'sepia',
        'gothic',
        'ghostlight',
        'toxic',
        'bubblegum',
        'lavender',
        'voltage',
        'redshift',
        'wildfire',
        'infinity',
        'infinity_s'
        ]

    # loop through color maps
    for colormap in colormaps:

        # plot as gradient
        gradient = getattr(cmr, colormap)
        gradient = [gradient(np.arange(gradient.N))]
        ax = plt.subplot()
        ax.set(xticklabels=[], yticklabels=[])
        ax.imshow(gradient, extent=[0, 10, 0, 1])
    
        # save as image
        fig = ax.get_figure()
        fig.savefig(
            f'{colormap}.png',
            dpi=300,
            bbox_inches='tight',
            pad_inches=0
            )


if __name__ == "__main__":
    main()