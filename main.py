import numpy as np 
from numpy import random
import matplotlib.pyplot as plt
from collision import collisionWall
import time


# Declare some values.
N = 1000 # Number of particles.
N_dim = 3 # Number of dimensions.
box_side = 2 # Side length of box.
v0 = 1 # Velocity scale factor.
dt = 0.02 # Time step.
T = 1 # Total simulation time.
N_it = int(T/dt) # Number of iteration steps.

# Random array of initial particle positions,
# such that particles lie within box centred at (0,0,0).
x = random.rand(N, 3) * box_side - 0.5*box_side

# Random array of initial particle velocities.
v = random.rand(N, 3) * v0 - 0.5*v0

#print(x)
#print(v)

def updatePositions(x0, v0, dt):
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



# Plot particle positions at t=0.
fig, ax = plt.subplots(figsize = (5,10))
ax.plot(x[:,0], x[:,1], 'ko', ms = 2.0)


tic = time.process_time() # For timing calculation time.

# Calculate subsequent positions and velocities.
for i in range(N_it):
    x = updatePositions(x, v, dt)
    v = collisionWall(x, v, box_side)


toc = time.process_time()
print("Calculation time =", (toc-tic), "s")
print("Number of particles =", N)
print("Number of time steps =", N_it)

# Plot particle positions at the end of simulation 
# (check they remain inside box).
ax.plot(x[:,0], x[:,1], 'bo', ms = 2.0)
plt.show()
