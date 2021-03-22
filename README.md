# particles-box
A simple physics simulation of particles in a box (personal project)

Primary goals:
(1) Write code in Python to simulate particles of an ideal gas in a 3D box at some temperature T, accounting for
       (i) collisions with walls of container,
       (ii) collisions with other particles.
    Calculate total energy at each time step (to make sure it is conserved).
    
(2) Calculate average pressure of walls on the container and the speed distribution.
(3) Compare speed distribution to Maxwell Boltzmann distribution using some curve fitting method
    and thus verify that system equilibrates at the expected temperature.
(4) Make suitable plots. Repeat calculation for various temperatures, etc...
    Investigate the physics basically.
    

More ambitious goals:    
(5) Rewrite the calculation part in C++ for faster runtime.
(6) Turn on long-range interactions between the particles, i.e. investigate non-ideal gases.
(7) Add some sort of background potential --> might lead to e.g. free electron model of electrons in solids (Fermi gas).
