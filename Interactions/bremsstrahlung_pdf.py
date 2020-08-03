import numpy as np
import constants as const

def Delta_E(eps, E_O_checked):

    return (1-eps)/(eps*E_0_checked)

def Delta_C():

    return 136*const.m*np.exp(const.Z_G)

def delta_prime(eps, E_O_checked):

    return Delta_E(eps, E_O_checked)*Delta_C()

def phi_1(delta):

    if delta<=1:
        return 20.867-3.242*delta+0.625*delta**2
    else:
        return 21.12-4.184*np.log(delta+0.952)

def phi_2(delta):

    if delta<=1:
        return 20.029-1.93*delta+0.086*delta**2
    else:
        return 21.12-4.184*np.log(delta+0.952)

def A(delta_prime, E_0_checked):

    if E_0_checked>50:
        return (3*phi_1(delta_prime)-phi_2(delta_prime)+8*const.Z_V)/(2/3+8*(np.log(184.15)+const.Z_V))
    else:
        return (3*phi_1(delta_prime)-phi_2(delta_prime)+8*const.Z_G)/(2/3+8*(np.log(184.15)+const.Z_G))

def B(delta_prime, E_0_checked):

    if E_0_checked>50:
        return (phi_1(delta_prime)+4*const.Z_V)/(4*(np.log(184.15)+const.Z_V))
    else:
        return (phi_1(delta_prime)+4*const.Z_G)/(4*(np.log(184.15)+const.Z_G))

def alpha_1(E_0_checked):
    if E_0_checked>50:
        return np.log(2)*(4/3+1/(9*np.log(184.15)*(1+const.Z_U)))
    else:
        return np.log(2)*(4/3+1/(9*np.log(184.15)*(1+const.Z_P)))

def f_1(eps):

    return 1/np.log(2) * (1-eps)/eps

def g_1(eps, E_0_checked):

    if (eps*E_0_checked>const.AP and eps*E_0_checked<E_0_checked-const.m):
        return A(delta_prime(eps, E_0_checked))
    else:
        return 0

def alpha_2():

    return 0.5

def f_2(eps):

    return 2*eps

def g_2(eps, E_0_checked):

    if (eps*E_0_checked>const.AP and eps*E_0_checked<E_0_checked-const.m):
        return B(delta_prime(eps, E_0_checked))
    else:
        return 0

def get_N_Brem(E_0_checked):

    eqn_soln = -1*np.log(const.AP/E_0_checked)/np.log(2)

    return int(np.floor(eqn_soln))
