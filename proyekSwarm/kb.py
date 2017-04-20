import numpy as np
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

X = np.arange(4, -4, -0.02)
Y = np.arange(4, -4, -0.02)
X, Y = np.meshgrid(X, Y)
a=-1*(1+(np.cos(12*np.sqrt(X**2+Y**2))))
b=0.5*(X**2+Y**2)+2
Z = a/b
def fun(X,Y):
    a=-1*(1+(np.cos(12*np.sqrt(X**2+Y**2))))
    b=0.5*(X**2+Y**2)+2
    Z = a/b
    return Z

num_func_params = 2
num_swarm = 100
position = -4 + 8 * np.random.rand(num_swarm, num_func_params)
velocity = np.zeros([num_swarm, num_func_params])
personal_best_position = np.copy(position)
personal_best_value = np.zeros(num_swarm)

for i in range(num_swarm):
    #Z = (1-X)**2 + 1 *(Y-X**2)**2
    personal_best_value[i] = fun(position[i][0],position[i][1])

tmax = 350
c1 = 0.001
c2 = 0.002
v1=0.2
v2=0.1
levels = np.linspace(-1, 35, 100)
global_best = np.max(personal_best_value)
global_best_position = np.copy(personal_best_position[np.argmax(personal_best_value)])
predator_velocity = np.zeros([1,2])
pack_velocity = np.zeros([3,2])
mini_position=np.zeros([1,2])
buffalo_status=['alive']*num_swarm
run = np.zeros([num_swarm, num_func_params])
tipe = 1 #type 1 pso, mencari dataran tinggi, type 2 diserang singa, mencari tmpt aman

for t in range(tmax):
    for i in range(num_swarm):
        if buffalo_status[i] == 'alive':
            error = fun(position[i][0],position[i][1])
            if personal_best_value[i] > error:
                personal_best_value[i] = error
                personal_best_position[i] = position[i]
    best = np.max(personal_best_value)
    best_index = np.argmax(personal_best_value)
    if global_best > best:
        global_best = best
        global_best_position = np.copy(personal_best_position[best_index])
    if tipe == 1:
        for i in range(num_swarm):
            #update velocity
            if buffalo_status[i] == 'alive':
                velocity[i] =velocity[i]*0.8+ c1 * np.random.rand() * (personal_best_position[i]-position[i]) \
                            +  c2 * np.random.rand() * (global_best_position - position[i])
                position[i] += velocity[i]
        encounter_lion=np.random.rand()
        if encounter_lion<0.03:
            tipe=2
            predator_position = -4 + 8 * np.random.rand(1,2)
            pack_position = predator_position[0] + 1 * np.random.rand(3,2)
    elif tipe==2:
        for i in range(num_swarm):
            #make an asumption of the first buffalo being the closest one
            if buffalo_status[i]=='alive':
                mini = np.abs(predator_position[0][0]-position[i][0]) + np.abs(predator_position[0][1]-position[i][1])
                mini_position[0]=position[i]
                break
        for i in range(num_swarm):
            #check nearest with predator
            if mini > np.abs(predator_position[0][0]-position[i][0]) + np.abs(predator_position[0][1]-position[i][1]) and buffalo_status[i]=='alive':
                mini_position[0] = position[i]
                mini = np.abs(predator_position[0][0]-position[i][0]) + np.abs(predator_position[0][1]-position[i][1])
        for i in range(num_swarm):
            #update velocity
            run[i] = -1 * v2 * (predator_position[0] - position[i])
            if position[i][0] + run[i][0] > -4 and position[i][0] + run[i][0] < 4:
                position[i][0] += run[i][0]
            if position[i][1] + run[i][1] > -4 and position[i][1] + run[i][1] < 4:
                position[i][1] += run[i][1]

        #check if buffalo dead
        for i in range(num_swarm):
            if np.abs(predator_position[0][0]-position[i][0]) < 0.1 and np.abs(predator_position[0][1] - position[i][1])<0.1:
                buffalo_status[i]='dying'
                victim=i
                tipe=3
                counter=20
                break
        predator_velocity[0] = v1*(mini_position[0]-predator_position[0])
        if predator_position[0][0]+predator_velocity[0][0] > -4 and predator_position[0][0]+predator_velocity[0][0] < 4:
            predator_position[0][0] += predator_velocity[0][0]
        if predator_position[0][1]+predator_velocity[0][1] > -4 and predator_position[0][1]+predator_velocity[0][1] < 4:
            predator_position[0][1] += predator_velocity[0][1]
    else:
        for i in range(3):
            pack_velocity[i] = v1*(predator_position[0]-pack_position[i])
            pack_position[i]+=pack_velocity[i]
        counter-=1
        if counter==0:
            tipe=1
            buffalo_status[victim] = 'dead'
        for i in range(num_swarm):
            #update velocity
            if buffalo_status[i] == 'alive':
                velocity[i] =velocity[i]*0.8+ c1 * np.random.rand() * (personal_best_position[i]-position[i]) \
                            +  c2 * np.random.rand() * (global_best_position - position[i])
                position[i] += velocity[i]

    fig = plt.figure()
    CS = plt.contour(X, Y, Z, levels =levels, cmap=cm.gist_stern)
    plt.gca().set_xlim([-4,4])
    plt.gca().set_ylim([-4,4])
    for i in range(num_swarm):
        if buffalo_status[i]=='alive' or buffalo_status[i]=='dying':
            plt.plot(position[i][0], position[i][1], 'go')
    if tipe==2 or tipe==3:
        plt.plot(predator_position[0][0], predator_position[0][1], 'ro')
        for i in range(3):
            plt.plot(pack_position[i][0],pack_position[i][1],'ro')
    plt.title('Swarm '+'{0:03d}'.format(t))
    filename = 'img{0:03d}.png'.format(t)
    plt.savefig(filename, bbox_inches='tight')
    plt.close(fig)