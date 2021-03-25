# analyse.py>

import numpy as np

def calculateKineticEnergy(v):
    """
    Calculates specific kinetic energy (i.e. per unit mass)
    N.B. all gas atoms assumed to have same mass.

    
    Argument:
    v: a 2D numpy array of particle velocities

    Returns:
    scalar (float) energy
    """

    return 0.5 * np.sum(np.linalg.norm(v, axis=1))