import constants as const
import scipy.optimize as opt
import numpy as np

lambd = 2
mu = 1
g_2_Norm = 1.8
g_3_Norm = 4.05

def get_B(particle, t):
    gamma = particle.energy/const.m
    beta = np.sqrt(1 - gamma**(-2))
    b_c = const.b_c
    omega_0 = b_c*t/(beta**2)
    b = np.log(omega_0)

    if b <= 2 - np.log(2):
        return 2/(2-np.log(2)) * b
    else:
        ans = opt.fsolve(lambda x: x-np.log(x)-b, 2)
        return ans[ans>=1][0]

def get_X_c(particle, t):
    gamma = particle.energy/const.m
    beta = np.sqrt(1 - gamma**(-2))
    X_cc = const.X_cc
    E_MS = particle.energy

    return X_cc*np.sqrt(t)/(E_MS*beta**2)
