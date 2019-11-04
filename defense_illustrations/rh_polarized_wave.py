import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

n = 1000
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

a = 0.02
# Plot a helix along the x-axis
theta_max = 500 * np.pi
theta = np.linspace(-theta_max, theta_max, n)
x = theta
z =  np.sin(-a*theta)
y =  np.cos(a*theta)
ax.plot(x, y, z, 'b', lw=2)

# An line through the centre of the helix
ax.plot((-theta_max/np.pi, theta_max), (0,0), (0,0), color='k', lw=2)
ax.plot((0, 0), (-1,1), (0,0), color='k', lw=2)
ax.plot((0, 0), (0,0), (-1,1), color='k', lw=2)
# sin/cos components of the helix (e.g. electric and magnetic field
# components of a circularly-polarized electromagnetic wave
#ax.plot(x, y, 0, color='r', lw=1, alpha=0.5)
#ax.plot(x, [0]*n, z, color='m', lw=1, alpha=0.5)

# Remove axis planes, ticks and labels
ax.text(500, 0.2, 0, 'z', None, fontsize=20)
ax.text(-.5, -1.5, 0, 'x', None, fontsize=20)
ax.text(-1, 0, -1.5, 'y', None, fontsize=20)
ax.set_axis_off()
ax.auto_scale_xyz([0, 500], [-1, 1], [-1, 1])
plt.show()