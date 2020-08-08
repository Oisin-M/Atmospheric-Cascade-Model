import numpy as np
import constants as const

def sample_direction(E_0_checked):

    phi = np.random.random()*2*np.pi #random angle
    dtheta = const.m/E_0_checked*np.random.choice([-1,1])
    return phi, dtheta
