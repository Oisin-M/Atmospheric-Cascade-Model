import numpy as np
import constants as const
from Transport.get_brem_macro_cross_section import dSigma_dkchecked
import scipy.integrate as integrate

def dEdx_BREM(particle):

    E_0_checked = particle.energy

    return const.X_0*integrate.quad(lambda k: k*dSigma_dkchecked(E_0_checked, k), 0, const.AP)[0]

def dEdx_ATOMIC_ELECTRONS(particle):

    pi = np.pi
    r_0 = const.r_0
    m = const.m
    n = const.n
    gamma = particle.energy/m
    beta = np.sqrt(1 - gamma**(-2))
    r = gamma - 1
    T_E = const.T_E
    T_prime_E = T_E/const.m_e
    y = 1/(gamma+1)
    I_adj = const.I_adj

    eta = np.sqrt(gamma**2 - 1)
    x = np.log(eta)/np.log(10)
    #v_P = np.sqrt( n*r_0**2*const.c**2 / np.pi) #not needed
    x_1 = const.x_1
    x_0 = const.x_0

    if x < x_0:
        delta = 0
    elif x > x_1:
        C = const.C #could be calculated but using from table
        delta = 2*np.log(10)*x+C
    else:
        a = const.a
        C = const.C #could be calculated but using from table
        m_s = const.m_s
        delta = 2*np.log(10)*x+C+a*(x_1-x)**m_s

    if particle.name=="electron":
        T_prime_max = r/2
        Delta = np.minimum(T_prime_E, T_prime_max)
        F = -1-beta**2+np.log((r-Delta)*Delta)+ r/(r-Delta)
        F += gamma**(-2)*(0.5*Delta**2 +(2*r+1)*np.log(1-Delta/r))
    elif particle.name=="positron":
        T_prime_max = r
        Delta = np.minimum(T_prime_E, T_prime_max)
        F = np.log(r*Delta)
        F -= beta**2/r*(r+2*Delta-1.5*Delta**2*y-(Delta-Delta**3/3)*y**2-(0.5*Delta**2-r*Delta**3/3+Delta**4/4)*y**3)


    return n*2*pi*r_0**2*m/beta**2 * (np.log(2*(r+2)/(I_adj/m))+F-delta)

def find_energy_loss_rate(particle):

    return -dEdx_BREM(particle)-dEdx_ATOMIC_ELECTRONS(particle)
