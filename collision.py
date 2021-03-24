# collision.py>

import numpy as np
from numpy import random

def collisionWall(x, v, box_side_length):
    """
	Checks if particle has moved beyond box boundary (i.e. collided with walls)
	and reverses appropriate velocity component to simulate an elastic collision with wall.

	Arguments:
    x: 2D numpy array of position coordinates.
    v: 2D numpy array of velocity components.
    wall_side_length: float, side length of box containing the particles.
    """
    
    side = box_side_length/2
    
    for i in range(len(x[:,0])):
        for j in range(len(x[0,:])):
    	    # If particle outside box, reverse v component.
    	    if x[i,j] <= -side or x[i,j] >= side:
                v[i,j] = -v[i,j]

    return v




def elasticCollision(x1, x2, dx, v1, v2):
    """
    Calculates velocities after an elastic collision between the two particles.

    Arguments:
    x1 = position (vector i.e. 1D array) of particle 1.
    x2 = position of particle 2.
    dx = unit vector between particle 1 and particle 2.
    v1 = velocity of particle 1.
    v2 = velocity of particle 2.

    Returns:
    Updated velocities after elastic collision.
    """
    
    if np.abs(np.linalg.norm(dx) - 1) >= 0.01:
        print("Warning: dx is not a unit vector")	
    v_rel_12 = v1 - v2 # Velocity of particle 1 relative to particle 2.
    if np.inner(v_rel_12, dx) >= 0:
        # Collision occurs (particle 1's velocity relative to particle 2 has a component towards particle 2).
        print("collision")
        
        # First calculate velocity components parallel to line joining centres of each particle
        # i.e. the velocity component along the line of action of the "impulse" that would act between them.
        v1_par = np.inner(v1, dx)*dx
        v2_par = np.inner(v2, dx)*dx

        # After elastic collision, these just get "swapped" around (because equal masses).
        v1 = v1 - v1_par + v2_par
        v2 = v2 - v2_par + v1_par
        return v1, v2
        
    else:
        # Collision does not occur.
        return v1, v2	






def collisionParticles(x, v, r):
    """
    Checks if particles are within distance 2r of each other. If yes, calls elasticCollision().

    Arguments:
    x: 2D numpy array of position coordinates.
    v: 2D numpy array of velocity components.
    r: radius of each particle (assumed identical).

    Returns:
    Updated 2D numpy array of particle velocities.
    """
    
    for i in range(len(x[:,0])):
        k = i+1
        for j in range(len(x[k:,0])): # Avoid double counting.
            x1 = x[i,:]
            x2 = x[j+k,:]
            #print(x1)
            #print(x2)
            v1 = v[i,:]
            v2 = v[j+k,:]
            #print(v1)
            #print(v2)
            dx = x2-x1 # Vector from particle 1 to particle 2.
            magnitude_dx = np.linalg.norm(dx)
            #print(dx)
            #print(magnitude_dx)
            
            if magnitude_dx <= 2*r:
                dx_norm = dx / magnitude_dx
                #print(dx_norm)
                v[i,:], v[j+k,:] = elasticCollision(x1, x2, dx_norm, v1, v2)



    return v






# Test that collisionParticles() samples all the collisions without double counting (uncomment print statements).
#x = np.array([[1,2,3],[10,20,30],[100,200,300],[1000,2000,3000]])
#v = random.rand(4, 3)

#collisionParticles(x, v, r=200)
