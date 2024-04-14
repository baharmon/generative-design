import matplotlib as mpl
import seaborn as sns # for extended palette of color maps

palette = 'icefire'
count = 11
colormap = mpl.colormaps[palette].resampled(count)
colors = (colormap.colors * 255).astype('uint8')
colors = colors[:,:3].tolist()
print(colors)