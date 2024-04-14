# import cellpylib as cpl
# import numpy as np
# np.random.seed(0)

# n_rows = 50
# n_cols = 50
# sandpile = cpl.Sandpile(n_rows, n_cols)

# initial = np.random.randint(7, size=n_rows*n_cols).reshape((1, n_rows, n_cols))
# # closed boundary with cells 0
# initial[0, 0, :], initial[0, n_rows-1, :], initial[0, :, 0], initial[0, :, n_cols-1] = 0, 0, 0, 0

# ca = cpl.evolve2d(
#     initial, 
#     # timesteps=10,
#     timesteps=cpl.until_fixed_point(),
#     apply_rule=sandpile, neighbourhood="von Neumann") # "Moore"

# # print("Number of timesteps to reach fixed point: %s" % len(ca))

# cpl.plot2d_animate(ca, colormap='viridis', save=True) ## to save evolve.gif

# cpl.plot2d_slice(ca, colormap='viridis')


import cellpylib as cpl

# Glider
cellular_automaton = cpl.init_simple2d(60, 60)
cellular_automaton[:, [28,29,30,30], [30,31,29,31]] = 1

# Blinker
cellular_automaton[:, [40,40,40], [15,16,17]] = 1

# Light Weight Space Ship (LWSS)
cellular_automaton[:, [18,18,19,20,21,21,21,21,20], [45,48,44,44,44,45,46,47,48]] = 1

# evolve the cellular automaton for 60 time steps
cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=60, neighbourhood='Moore',
                                  apply_rule=cpl.game_of_life_rule, memoize='recursive')

cpl.plot2d_animate(cellular_automaton)