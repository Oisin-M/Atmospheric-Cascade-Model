import Transport.get_brem_macro_cross_section as brem
import Transport.get_pair_macro_cross_section as pair

def get_total_macro_cross_sections(particle):

    if particle.name=="photon":
        return {'pair production': pair.get_total_macro_cross_section(particle)}

    elif particle.name=="electron" or particle.name=="positron":
        return {'bremsstrahlung': brem.get_total_macro_cross_section(particle)}

    else:
        raise Exception("Have not implemented other particles yet.")
