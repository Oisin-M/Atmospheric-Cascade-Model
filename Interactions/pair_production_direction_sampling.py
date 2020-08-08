import numpy as np
import constants as const

def sample_direction(k_checked):

    phi = np.random.random()*2*np.pi #random angle
    dtheta = const.m/k_checked*np.random.choice([-1,1])
    return phi, dtheta
