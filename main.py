import numpy as np 
from numpy import random
import matplotlib.pyplot as plt


# Declare some values.
N = 100 # Number of particles.
N_dim = 3 # Number of dimensions.
box_side = 2 # Side length of box.
v0 = 1 # Velocity scale factor.
dt = 0.1 # Time step.

# Random array of initial particle positions,
# such that particles lie within box centred at (0,0,0).
x = random.rand(N, 3) * box_side - 0.5*box_side

# Random array of initial particle velocities.
v = random.rand(N, 3) * v0 - 0.5*v0

#print(x)
#print(v)

def update_positions(x0, v0, dt):
    """
    Calculates the positions after time dt, given particle positions and velocities.

    Acceleration assumed to be zero, so this is exact.

    Arguments:
    x0: 2D numpy array of particle position coordinates.
    v0: 2D numpy array of particle velocity components.
    dt: the time step to be used.
    
    Returns:
    2D numpy array of positions
    """	
    return x0 + v0*dt	




fig, ax = plt.subplots(figsize = (5,10))
ax.plot(x[:,0], x[:,1], 'ko', ms = 2.0)

for i in range(10):
	x = update_positions(x,v,dt)


ax.plot(x[:,0], x[:,1], 'bo', ms = 2.0)
plt.show()