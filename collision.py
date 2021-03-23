# collision.py>

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