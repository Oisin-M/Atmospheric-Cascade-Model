import numpy as np
import Transport.get_cross_sections as get_cross_sections
import Transport.energy_loss as energy_loss
import Transport.deflection as deflection
import constants as const

def t_s(E_checked):

    gamma = E_checked/const.m
    beta = np.sqrt(1 - gamma**(-2))
    return const.X_0*2*E_checked*beta**2/const.E_checked_s

def move(particle):
    # print("!!! movement initiated")

    sigmas=get_cross_sections.get_total_macro_cross_sections(particle)
    total_cross_section=np.array(list(sigmas.values())).sum()
    lambd=1/total_cross_section

    sample_N_lambda = -np.log(np.random.random())

    dx=sample_N_lambda*lambd #approximately, in cm



    if particle.charge==0:
        #easy photon transport
        cartesian_direction=np.array([np.sin(particle.direction[0])*np.cos(particle.direction[1]),np.sin(particle.direction[0])*np.sin(particle.direction[1]), np.cos(particle.direction[1])])
        particle.position+=dx*cartesian_direction
        # print("MOVED TO: ", particle.position)
        interaction_bool = True

    else:
        #charged particle transport

        #should split dx into smaller steps
        t_P_max = const.eps_P_max*t_s(particle.energy) #max chunk size
        # print("MAX: ", t_P_max)
        # print("DX: ", dx)
        if t_P_max>=dx:
            chunk_size=dx
        else:
            chunk_size = 0.9*t_P_max #chunk size

        quot,rem = divmod(dx, chunk_size)

        for i in range(int(quot)):
            cartesian_direction=np.array([np.sin(particle.direction[0])*np.cos(particle.direction[1]),np.sin(particle.direction[0])*np.sin(particle.direction[1]), np.cos(particle.direction[1])])
            particle.position+=chunk_size*cartesian_direction
            #split into smaller chunks, this should multiple movements, not one
            dEdx = energy_loss.find_energy_loss_rate(particle)
            new_Theta = deflection.find_Theta(particle, chunk_size, lambd)
            #print("THETA: ", new_Theta)
            new_phi = deflection.find_phi(particle)
            particle.energy += dEdx*chunk_size
            particle.direction[0] = new_Theta
            particle.direction[1] = new_phi
            # print("MOVED TO: ", particle.position)
            # print("ENERGY CHANGED TO: ", particle.energy)
            # print("DIRECTION CHANGED TO: ", particle.direction)
            if particle.energy<const.AE:
                break

        if rem!=0 and particle.energy>const.AE:
            #do remainder
            cartesian_direction=np.array([np.sin(particle.direction[0])*np.cos(particle.direction[1]),np.sin(particle.direction[0])*np.sin(particle.direction[1]), np.cos(particle.direction[1])])
            particle.position+=rem*cartesian_direction

            #split into smaller chunks, this should multiple movements, not one
            dEdx = energy_loss.find_energy_loss_rate(particle)
            new_Theta = deflection.find_Theta(particle, rem, lambd)
            #print("THETA: ", new_Theta)
            new_phi = deflection.find_phi(particle)
            particle.energy += dEdx*rem
            particle.direction[0] = new_Theta
            particle.direction[1] = new_phi
            # print("MOVED TO: ", particle.position)
            # print("ENERGY CHANGED TO: ", particle.energy)
            # print("DIRECTION CHANGED TO: ", particle.direction)


        #find if interaction occurs
        NEW_sigmas=get_cross_sections.get_total_macro_cross_sections(particle)
        NEW_total_cross_section=np.array(list(sigmas.values())).sum()
        zeta = np.random.random()
        if zeta<=NEW_total_cross_section/total_cross_section:
            interaction_bool = True ####NEED TO CHANGE THIS
        else:
            interaction_bool = False

    # print("TOTAL PATH LENGTH IS: ", dx)

    return particle, dx, interaction_bool
