import numpy as np
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

# Make data.
X = np.arange(4, -4, -0.02)
Y = np.arange(4, -4, -0.02)
X, Y = np.meshgrid(X, Y)

#drop wave function
a=-1*(1+(np.cos(12*np.sqrt(X**2+Y**2))))
b=0.5*(X**2+Y**2)+2
Z = a/b

num_func_params = 2
num_swarm = 100
position = -3 + 6 * np.random.rand(num_swarm, num_func_params)
velocity = np.zeros([num_swarm, num_func_params])
personal_best_position = np.copy(position)
personal_best_value = np.zeros(num_swarm)

for i in range(num_swarm):
    #a=-1*(1+(np.cos(12*np.sqrt(X**2+Y**2))))
    #b=0.5*(X**2+Y**2)+2
    #Z = a/b
    first=-1*(1+(np.cos(12*np.sqrt(position[i][0]**2+position[i][1]**2))))
    second=0.5*(position[i][0]**2+position[i][1]**2)+2
    personal_best_value[i]= first/second

tmax = 200
c1 = 0.001
c2 = 0.002
levels = np.linspace(-0.8, 0, 100)
global_best = np.min(personal_best_value)
global_best_position = np.copy(personal_best_position[np.argmin(personal_best_value)])

for t in range(tmax):
    for i in range(num_swarm):
        error = first/second
        if personal_best_value[i] > error:
            personal_best_value[i] = error
            personal_best_position[i] = position[i]
    best = np.min(personal_best_value)
    best_index = np.argmin(personal_best_value)
    if global_best > best:
        global_best = best
        global_best_position = np.copy(personal_best_position[best_index])
        
    for i in range(num_swarm):
        #update velocity
        velocity[i] += c1 * np.random.rand() * (personal_best_position[i]-position[i]) \
                    +  c2 * np.random.rand() * (global_best_position - position[i])
        position[i] += velocity[i]
    
    fig = plt.figure()
    CS = plt.contour(X, Y, Z, levels =levels, cmap=cm.gist_stern)
    plt.gca().set_xlim([-4,4])
    plt.gca().set_ylim([-4,4])
    for i in range(num_swarm):
        plt.plot(position[i][0], position[i][1], 'go')
    plt.plot(global_best_position[0], global_best_position[1], 'ro')
    
    plt.title('{0:03d}'.format(t))
    filename = 'img{0:03d}.png'.format(t)
    plt.savefig(filename, bbox_inches='tight')
    plt.close(fig)