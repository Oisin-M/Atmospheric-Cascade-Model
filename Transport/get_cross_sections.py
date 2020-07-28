def get_total_macro_cross_sections(particle):

    if particle.name=="photon":
        return {'pair production': 0.02} #made up for now
    elif particle.name=="electron" or particle.name=="position":
        return {'bremsstrahlung': 0.05}
    else:
        raise Exception("Have not implemented other particles yet.")
