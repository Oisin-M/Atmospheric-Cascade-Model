import Particle as pcl

import numpy as np

def pair_production(photon):
    """A function to simulate pair production when given a photon"""
    
    if photon.name!="photon":
        raise TypeError("Did not input a valid photon for pair production")
    else:
        new_energy = (photon.energy - 2*pcl.name_to_mass['electron'])/2
       
        p_e = np.sqrt( (new_energy**2 - (pcl.name_to_mass['electron']*(3*10**8)**2)**2) / (3*10**8)**2 )
        dtheta = np.arcsin(photon.energy/(2*p_e))
        
        return [pcl.Particle("electron", new_energy, photon.position, photon.theta-dtheta),
                pcl.Particle("positron", new_energy, photon.position, photon.theta+dtheta)]


def bremsstrahlung(particle):

    if particle.name=="photon":
        raise TypeError("Did not input a valid particle for Bremsstrahlung")

