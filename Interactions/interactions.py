import particle as pcl
import Interactions.bremsstrahlung_pdf as brem_pdf
import Interactions.pair_production_pdf as pair_pdf
import numpy as np

def pair_production(photon):
    """A function to simulate pair production when given a photon"""

    if photon.name!="photon":
        raise TypeError("Did not input a valid photon for pair production")
    else:

        k_checked = photon.energy
        E_neg_checked = pair_pdf.sample_secondary_energy(k_checked)
        E_plus_checked = k_checked - E_neg_checked

        return [pcl.Particle("electron", E_neg_checked, photon.position, photon.direction),
                pcl.Particle("positron", E_plus_checked, photon.position, photon.direction)]


def bremsstrahlung(particle):

    if particle.name=="photon":
        raise TypeError("Did not input a valid particle for Bremsstrahlung")
    else:
        E_0_checked = particle.energy
        k_checked = brem_pdf.sample_secondary_energy(E_0_checked)
        E_checked = E_0_checked - k_checked
        particle.energy = E_checked

        return [particle,
                pcl.Particle("photon", k_checked, particle.position, particle.direction)]
