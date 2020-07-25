import Particle as pcl

def pair_production(photon):
    """A function to simulate pair production when given a photon"""
    
    if photon.name!="photon":
        raise TypeError("Did not input a valid photon for pair production")
    else:
        new_energy = (photon.energy - 2*pcl.name_to_mass['electron'])/2
        
        return [pcl.Particle("electron", new_energy, photon.position, photon.theta),
                pcl.Particle("positron", new_energy, photon.position, photon.theta)]


def bremsstrahlung(particle):

    if particle.name=="photon":
        raise TypeError("Did not input a valid particle for Bremsstrahlung")

