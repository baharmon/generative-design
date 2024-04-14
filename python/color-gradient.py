# save each as a script

"""matplotlib"""

# import libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# set style
sns.set(style = "dark")

# generate gradient
gradient = plt.colormaps['viridis']
gradient = [gradient(np.arange(gradient.N))]

# plot gradient
ax = plt.subplot()
ax.set(xticklabels=[], yticklabels=[])
ax.imshow(gradient, extent=[0, 10, 0, 1])

"""seaborn"""

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

"""cmocean"""

# import libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import cmocean

# set style
sns.set(style = "dark")

# generate gradient
gradient = cmocean.cm.delta
gradient = [gradient(np.arange(gradient.N))]

# plot gradient
ax = plt.subplot()
ax.set(xticklabels=[], yticklabels=[])
ax.imshow(gradient, extent=[0, 10, 0, 1])

"""colorcet"""

# import libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import colorcet as cc

# set style
sns.set(style = "dark")

# generate gradient
gradient = cc.cm.fire
gradient = [gradient(np.arange(gradient.N))]

# plot gradient
ax = plt.subplot()
ax.set(xticklabels=[], yticklabels=[])
ax.imshow(gradient, extent=[0, 10, 0, 1])

"""scientific colors"""

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

"""cmasher"""

# import libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import cmasher as cmr

# set style
sns.set(style = "dark")

# generate gradient
gradient = cmr.gothic
gradient = [gradient(np.arange(gradient.N))]

# plot gradient
ax = plt.subplot()
ax.set(xticklabels=[], yticklabels=[])
ax.imshow(gradient, aspect=20)
