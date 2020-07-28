import numpy as np
import Transport.get_cross_sections as get_cross_sections
import Transport.energy_loss as energy_loss
import Transport.deflection as deflection

def move(particle):
    print("movement initiated")

    sigmas=get_cross_sections.get_total_macro_cross_sections(particle)
    total_cross_section=np.array(list(sigmas.values())).sum()
    lambd=1/total_cross_section

    sample_N_lambda = -np.log(np.random.random())

    dx=sample_N_lambda*lambd #approximately, in cm


    print("TOTAL PATH LENGTH IS: ", dx)

    if particle.charge==0:
        #easy photon transport
        cartesian_direction=np.array([np.sin(particle.direction[0])*np.cos(particle.direction[1]),np.sin(particle.direction[0])*np.sin(particle.direction[1]), np.cos(particle.direction[1])])
        particle.position+=dx*cartesian_direction
        print("MOVED TO: ", particle.position)
        print("INTERACTION (not handled by code yet)")

    else:
        #charged particle transport
        cartesian_direction=np.array([np.sin(particle.direction[0])*np.cos(particle.direction[1]),np.sin(particle.direction[0])*np.sin(particle.direction[1]), np.cos(particle.direction[1])])
        particle.position+=dx*cartesian_direction

        dEdx = energy_loss.find_energy_loss_rate(particle)
        new_Theta = deflection.find_Theta(particle, dx, lambd)
        new_phi = deflection.find_phi(particle)
        particle.energy += dEdx*dx
        particle.direction[0] = new_Theta
        particle.direction[1] = new_phi
        print("MOVED TO: ", particle.position)
        print("ENERGY CHANGED TO: ", particle.energy)
        print("DIRECTION CHANGED TO: ", particle.direction)


    return particle
