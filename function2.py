#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      USER
#
# Created:     08/03/2017
# Copyright:   (c) USER 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(4, -4, -0.02)
Y = np.arange(4, -4, -0.02)
X, Y = np.meshgrid(X, Y)

#drop wave function
a=-1*(1+(np.cos(12*np.sqrt(X**2+Y**2))))
b=0.5*(X**2+Y**2)+2
Z = a/b

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.gist_stern,
                       linewidth=0, antialiased=False)

# Customize the z axis.
# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()


