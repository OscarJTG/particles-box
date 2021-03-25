import numpy as np 
from numpy import random
import matplotlib.pyplot as plt
from collision import collisionWall, collisionParticles
from analyse import calculateKineticEnergy
import time


# Declare some values.
N = 10 # Number of particles.
N_dim = 3 # Number of dimensions.
box_side = 2 # Side length of box.
v0 = 1 # Velocity scale factor.
dt = 0.02 # Time step.
T = 500 # Total simulation time.
N_it = int(T/dt) # Number of iteration steps.
radius = 0.1 # Radius of each particle 
               # (should be much smaller than ((box_side**3)/N)**(1/3)).


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




def iterateOneSecond(x, v, box_side, radius, dt):
    """
    Progresses simulation iteratively over one second of simulated time.

    Arguments:
    x: 2D numpy array of particle positions.
    v: 2D numpy array of particle velocities.
    box_side: side length of the cubic box confining the particles.
    radius: atomic radius of each particle (modelled as hard spheres).
    dt: timestep for interations.

    Returns:
    Updated 2D numpy arrays x, v
    """
    
    if np.abs((1/dt) - np.floor(1/dt)) > 0.001:
        print("Warning: timestep dt does not allow for integer number of iterations in 1 second")
        # but still carry on with program after this warning.


    N = int(np.floor(1/dt))
    for i in range(N):
        # Check if there are any collisions, then calculate new velocities.
        # Then calculate subsequent positions after timestep dt.
        #v = collisionParticles(x, v, radius)
        v = collisionWall(x, v, box_side)
        x = updatePositions(x, v, dt)

    return [x, v]




# Generate random array of initial particle positions,
# such that particles lie within box centred at (0,0,0).
x = random.rand(N, 3) * box_side - 0.5*box_side

# Generate random array of initial particle velocities.
v = random.rand(N, 3) * v0 - 0.5*v0


# Plot particle positions at t=0.
fig, ax = plt.subplots(figsize = (5,10))
ax.plot(x[:,0], x[:,1], 'ko', ms = 2.0)

E = np.zeros(T+1)
E[0] = calculateKineticEnergy(v)
tic = time.process_time() # For timing calculation time.

for i in range(T):
    x, v = iterateOneSecond(x, v, box_side, radius, dt)
    E[i+1] = calculateKineticEnergy(v)


toc = time.process_time()
print("Calculation time =", (toc-tic), "s")
print("Number of particles =", N)
print("Number of time steps =", N_it)

energy_mean = np.mean(E)
energy_std = np.std(E)
energy_frac_dev = energy_std / energy_mean

print("Energy =", energy_mean, "+-", energy_std)
print("Energy fractional deviation =", energy_frac_dev)

# Plot particle positions at the end of simulation 
# (check they remain inside box).
ax.plot(x[:,0], x[:,1], 'bo', ms = 2.0)

t1 = np.arange(0,T+1)
fig1, ax1 = plt.subplots()
ax1.plot(t1, E)
ax1.set_xlabel("Simulated time / s")
ax1.set_ylabel("Energy (per unit mass) / m$^2$ s$^{-2}$")
ax1.set_title("Plot to show if energy is conserved")

plt.show()
