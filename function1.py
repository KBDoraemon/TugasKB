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
X = np.arange(2, -2, -0.02)
Y = np.arange(2, -2, -0.02)
X, Y = np.meshgrid(X, Y)

#Function Six-hump camel back
Z = (4-2.1*X**2+X**4/3)*X**2+X*Y+(-4+4*Y**2)*Y**2
# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.gist_stern,
                       linewidth=0, antialiased=False)

# Customize the z axis.
# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()


