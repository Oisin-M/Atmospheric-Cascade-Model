import Particle as pcl

import numpy as np

def pair_production(photon, energy_electron, energy_positron):
    """A function to simulate pair production when given a photon"""

    if photon.name!="photon":
        raise TypeError("Did not input a valid photon for pair production")
    else:
        #new_energy = (photon.energy - 2*pcl.name_to_mass['electron'])/2

        #p_e = np.sqrt( (photon.energy**2/4 - (pcl.name_to_mass['electron']*(3*10**8)**2)**2) / (3*10**8)**2 )

        dtheta = 0 #must have a recoiling nucleus somewhere for pair production, so angle change is normally negligible

        return [pcl.Particle("electron", energy_electron, photon.position, photon.theta),
                pcl.Particle("positron", energy_positron, photon.position, photon.theta)]


def bremsstrahlung(particle):

    if particle.name=="photon":
        raise TypeError("Did not input a valid particle for Bremsstrahlung")
