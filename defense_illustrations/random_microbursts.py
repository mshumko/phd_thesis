import numpy as np
import matplotlib.pyplot as plt

# Toggle between showing a few microbursts with circles to showing many 
# microburst centers only.
ILLUSTRATION = True 
MICROBUST_AREA_OUTLINE=False
grid_size = 2
microburst_radius = 1
sc_locations = np.array([[0, 0.7], [0, -0.7]])

microburst = {}

if ILLUSTRATION:
    n_microbursts = 3
    microburst['radius'] = microburst_radius*np.ones(n_microbursts)
    microburst['center'] = np.array([[0.5, 0], [-0.25, 1], [-1.5, -1]])
else:
    n_microbursts = 10_000
    microburst['radius'] = microburst_radius*np.ones(n_microbursts)
    microburst['center'] = np.random.uniform(-grid_size, grid_size, (n_microbursts, 2))

fig, ax = plt.subplots()

plot_n = n_microbursts
circles = plot_n*[None]
centers = plot_n*[None]

# # Determine if the circle intersects one, or both spacecraft
condition_A = np.where(np.linalg.norm([microburst['center'][:, 0]-sc_locations[0, 0],
                microburst['center'][:, 1]-sc_locations[0, 1]], axis=0) < microburst_radius)[0]
condition_B = np.where(np.linalg.norm([microburst['center'][:, 0]-sc_locations[1, 0],
                microburst['center'][:, 1]-sc_locations[1, 1]], axis=0) < microburst_radius)[0]

for c in range(plot_n):
    if (c in condition_A and c in condition_B):
        # If microburst seen by both spacecraft
        color='r'
    elif c in condition_A:
        # If microburts seen by lower spacecraft
        color = 'b'
    elif c in condition_B:
        # If microburts seen by lower spacecraft
        color = 'b'
    else: 
        color='k'

    if ILLUSTRATION:
        circles[c] = plt.Circle((microburst['center'][c, 0], microburst['center'][c, 1]), 
                        microburst['radius'][c], color=color, alpha=0.1, lw=2)
        ax.add_artist(circles[c])

        if MICROBUST_AREA_OUTLINE:
            # Outline the center area around top spacecraft
            ax.add_artist(plt.Circle(sc_locations[0], microburst_radius, color='b', ls='--', fill=False))
    centers[c] = plt.scatter(microburst['center'][c, 0], microburst['center'][c, 1], c=color)
    
# Spacecraft ceneter locations.
ax.scatter([sc_locations[0, 0], sc_locations[1, 0]], 
            [sc_locations[0, 1], sc_locations[1, 1]], s=100, c='g', marker='s')
ax.set_ylim(-grid_size, grid_size)
ax.set_xlim(-grid_size, grid_size)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

ax.set_aspect(1.0)
plt.tight_layout()
plt.show()

