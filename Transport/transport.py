import numpy as np
import Transport.get_cross_sections as get_cross_sections
import Transport.energy_loss as energy_loss

def move(particle):
    print("move")

    sigmas=get_cross_sections.get_total_cross_sections(particle)
    total_cross_section=np.array(list(sigmas.values())).sum()
    lambd=1/total_cross_section

    sample_N_lambda = -np.log(np.random.random())

    dx=sample_N_lambda*lambd #approximately

    cartesian_direction=np.array([np.sin(particle.direction[0])*np.cos(particle.direction[1]),np.sin(particle.direction[0])*np.sin(particle.direction[1]), np.cos(particle.direction[1])])

    print("TOTAL PATH LENGTH IS: ", dx)

    if particle.charge==0:
        #easy photon transport
        particle.position+=dx*cartesian_direction
        print(particle.position)
        print("INTERACTION")

    else:
        #charged particle transport
        dEdx = energy_loss.find_energy_loss_rate(particle)
        particle.energy+=dEdx*dx
        print("ENERGY CHANGED TO: ", particle.energy)


    return particle
