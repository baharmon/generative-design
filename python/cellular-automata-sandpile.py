import cellpylib as cpl
import numpy as np
np.random.seed(0)

n_rows = 50
n_cols = 50
sandpile = cpl.Sandpile(n_rows, n_cols)

initial = np.random.randint(7, size=n_rows*n_cols).reshape((1, n_rows, n_cols))
# closed boundary with cells 0
initial[0, 0, :], initial[0, n_rows-1, :], initial[0, :, 0], initial[0, :, n_cols-1] = 0, 0, 0, 0

ca = cpl.evolve2d(
    initial, 
    # timesteps=10,
    timesteps=cpl.until_fixed_point(),
    apply_rule=sandpile, neighbourhood="von Neumann") # "Moore"

print("Number of timesteps to reach fixed point: %s" % len(ca))

cpl.plot2d_animate(ca, colormap='viridis', dpi=300, save=True) ## to save evolve.gif

# cpl.plot2d_slice(ca, colormap='viridis')
