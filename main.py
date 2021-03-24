import numpy as np 
from numpy import random
import matplotlib.pyplot as plt
from collision import collisionWall, collisionParticles
import time


# Declare some values.
N = 100 # Number of particles.
N_dim = 3 # Number of dimensions.
box_side = 2 # Side length of box.
v0 = 1 # Velocity scale factor.
dt = 0.02 # Time step.
T = 1 # Total simulation time.
N_it = int(T/dt) # Number of iteration steps.
radius = 0.1 # Radius of each particle 
               # (should be much smaller than ((box_side**3)/N)**(1/3)).

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

# Check if there are any collisions, then calculate new velocities.
# Then calculate subsequent positions after time dt.
for i in range(N_it):
    v = collisionParticles(x, v, radius)
    v = collisionWall(x, v, box_side)
    x = updatePositions(x, v, dt)
    


toc = time.process_time()
print("Calculation time =", (toc-tic), "s")
print("Number of particles =", N)
print("Number of time steps =", N_it)

# Plot particle positions at the end of simulation 
# (check they remain inside box).
ax.plot(x[:,0], x[:,1], 'bo', ms = 2.0)
plt.show()
