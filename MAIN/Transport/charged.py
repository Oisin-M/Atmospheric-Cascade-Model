import numpy as np
from constants import *
from .scattering.energy_loss import find_energy_loss_rate
from .interact_bool.interact_bool import get_total_macro_cross_section

def sample_d():
    zeta=np.random.random()
    return lambda_r*np.log(2)*-1*np.log(zeta)

def max_step_size(energy):

    gamma=energy/m
    beta=np.sqrt(1-gamma**(-2))

    t_s=2*X_0*energy*beta**2/E_checked_s

    return eps_P_max*t_s

def move(particle):

    step=max_step_size(particle[2])
    print("max: ",step)

    d=sample_d()
    print("d: ",d)

    q,r=divmod(d, step)
    print(q,r)

    sigma_first=get_total_macro_cross_section(particle)

    for i in range(int(q)):
        x=particle[3]+d*np.sin(particle[6])*np.cos(particle[7])
        y=particle[4]+d*np.sin(particle[6])*np.sin(particle[7])
        z=particle[5]+d*np.cos(particle[7])
        print("energy loss rate: ", find_energy_loss_rate(particle))
        print("energy loss: ", find_energy_loss_rate(particle)*step)
        E=particle[2]+find_energy_loss_rate(particle)*step

        particle[2]=E
        particle[3]=x
        particle[4]=y
        particle[5]=z

    x=particle[3]+d*np.sin(particle[6])*np.cos(particle[7])
    y=particle[4]+d*np.sin(particle[6])*np.sin(particle[7])
    z=particle[5]+d*np.cos(particle[7])
    print("energy loss rate: ", find_energy_loss_rate(particle))
    print("energy loss: ", find_energy_loss_rate(particle)*r)
    E=particle[2]+find_energy_loss_rate(particle)*r

    particle[2]=E
    particle[3]=x
    particle[4]=y
    particle[5]=z

    sigma_final=get_total_macro_cross_section(particle)

    interact=np.random.random()<=sigma_final/sigma_first
    print("interact: ", interact)

    return particle, interact
