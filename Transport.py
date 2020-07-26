def get_cross_sections(particle):

    if particle.name=="photon":
        return {'pair production': 0.02} #made up for now
    else:
        raise Exception("NOT EVEN PRETENDING THIS IS IMPLEMENTED ERROR")

def move(particle):

    sigmas=get_cross_sections(particle)
    total_cross_section=np.array(sigmas.values).sum()
    lambd=1/total_cross_section

    sample_N_lambda = -np.log(np.random.random())

    dx=sample_N_lambda*lambd
    print(dx)

    if particle.charge==0:
        #charged particle transport
        print("photon")

    else:
        #easy photon transport
        print("charged particle")

    return particle
