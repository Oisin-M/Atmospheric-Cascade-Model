import numpy as np

def get_cross_sections(particle):

    if particle.name=="photon":
        return {'pair production': 0.02} #made up for now
    elif particle.name=="electron" or particle.name=="position":
        return {'bremsstrahlung': 0.05}
    else:
        raise Exception("NOT EVEN PRETENDING THIS IS IMPLEMENTED ERROR")

def move(particle):
    print("move")

    sigmas=get_cross_sections(particle)
    total_cross_section=np.array(list(sigmas.values())).sum()
    lambd=1/total_cross_section

    sample_N_lambda = -np.log(np.random.random())

    dx=sample_N_lambda*lambd

    cartesian_direction=np.array([np.sin(particle.direction[0])*np.cos(particle.direction[1]),np.sin(particle.direction[0])*np.sin(particle.direction[1]), np.cos(particle.direction[1])])

    if particle.charge==0:
        #easy photon transport
        particle.position+=dx*cartesian_direction
        print(particle.position)
        print("interaction")

    else:
        #charged particle transport
        print("charged particle")

    return particle
