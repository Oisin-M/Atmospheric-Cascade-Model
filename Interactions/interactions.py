import particle as pcl
import Interactions.bremsstrahlung_pdf as brem_pdf
import Interactions.pair_production_pdf as pair_pdf
import Interactions.bremsstrahlung_direction_sampling as brem_dir
import Interactions.pair_production_direction_sampling as pair_dir
import numpy as np

def pair_production(photon):

    if photon.name!="photon":
        raise TypeError("Did not input a valid photon for pair production")
    else:

        k_checked = photon.energy
        E_neg_checked = pair_pdf.sample_secondary_energy(k_checked)
        E_plus_checked = k_checked - E_neg_checked

        phi, dtheta = brem_dir.sample_direction(k_checked)
        e_minus_dir = np.array([photon.direction[0]+dtheta, phi])
        e_plus_dir = np.array([photon.direction[0]+dtheta, -phi])

        return [pcl.Particle("electron", E_neg_checked, photon.position, e_minus_dir),
                pcl.Particle("positron", E_plus_checked, photon.position, e_plus_dir)]


def bremsstrahlung(particle):

    if particle.name=="photon":
        raise TypeError("Did not input a valid particle for Bremsstrahlung")
    else:
        E_0_checked = particle.energy
        k_checked = brem_pdf.sample_secondary_energy(E_0_checked)
        E_checked = E_0_checked - k_checked
        particle.energy = E_checked

        phi, dtheta = brem_dir.sample_direction(E_0_checked)
        direction = np.array([particle.direction[0]+dtheta, phi])

        return [particle,
                pcl.Particle("photon", k_checked, particle.position, direction)]
