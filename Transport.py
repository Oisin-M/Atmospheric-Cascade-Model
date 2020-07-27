import numpy as np

atmosphere_comp={
'O2': 0.7809,
'N2': 0.2095,
'Ar': 0.0093
} #https://en.wikipedia.org/wiki/Atmosphere_of_Earth for now

new_percs=np.array([0.7809*2, 0.2095*2, 0.0093])
new_percs*=1/new_percs.sum()

air_data={
8: new_percs[0],
7: new_percs[1],
18: new_percs[2]
} #Z to % dict

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

    dx=sample_N_lambda*lambd #approximately

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
