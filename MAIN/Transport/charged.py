import numpy as np
from constants import *

def sample_d():
    zeta=np.random.random()
    return lambda_r*np.log(2)*-1*np.log(zeta)

def max_step_size(energy):

    gamma=energy/m
    beta=np.sqrt(1-gamma**(-2))

    t_s=2*X_0*energy*beta**2/E_checked_s

    return eps_P_max*t_s

def move(particle):

    print("max: ",max_step_size(particle[2]))

    d=sample_d()

    x=particle[3]+d*np.sin(particle[6])*np.cos(particle[7])
    y=particle[4]+d*np.sin(particle[6])*np.sin(particle[7])
    z=particle[5]+d*np.cos(particle[7])

    return x, y, z
