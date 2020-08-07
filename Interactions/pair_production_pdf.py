import numpy as np
import constants as const

def Delta_E(eps, k_checked):

    return 1/(k_checked*eps*(1-eps))

def Delta_C():

    return 136*const.m*np.exp(const.Z_G)

def delta_prime(eps, k_checked):

    return Delta_E(eps, k_checked)*Delta_C()

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

def A(delta_prime, k_checked):

    if k_checked>50:
        return (3*phi_1(delta_prime)-phi_2(delta_prime)+8*const.Z_V)/(2/3+8*(np.log(184.15)+const.Z_V))
    else:
        return (3*phi_1(delta_prime)-phi_2(delta_prime)+8*const.Z_G)/(2/3+8*(np.log(184.15)+const.Z_G))

def C(delta_prime, k_checked):

    if k_checked>50:
        return (3*phi_1(delta_prime)+phi_2(delta_prime)+16*const.Z_V)/(-2/3 + 16*np.log(184.15)+const.Z_V)
    else:
        return (3*phi_1(delta_prime)+phi_2(delta_prime)+16*const.Z_G)/(-2/3 + 16*np.log(184.15)+const.Z_G)

def alpha_1(k_checked):

    if k_checked>50:
        return 2/3-1/(38*np.log(184.15)*(1+const.Z_U))
    else:
        return 2/3-1/(38*np.log(184.15)*(1+const.Z_P))

def f_1(eps):

    return 1

def g_1(eps, k_checked):

    if (eps*k_checked>const.m and eps*k_checked<k_checked-const.m):
        return C(delta_prime(eps, k_checked), k_checked)
    else:
        return 0

def alpha_2(k_checked):

    if k_checked>50:
        return 1/12*(4/3+1/(9*np.log(184.15)*(1+const.Z_U)))
    else:
        return 1/12*(4/3+1/(9*np.log(184.15)*(1+const.Z_P)))

def f_2(eps):

    return 12*(eps-0.5)**2

def g_2(eps, k_checked):

    if (eps*k_checked>const.m and eps*k_checked<k_checked-const.m):
        return A(delta_prime(eps, k_checked), k_checked)
    else:
        return 0

def sample_f_1():

    return np.random.random()

def sample_f_2():

    zeta_1=np.random.random()
    zeta_2=np.random.random()
    zeta_3=np.random.random()
    return 1-np.max([zeta_1, zeta_2, zeta_3])

def sample_secondary_energy(k_checked):

    zeta_1 = np.random.random()
    zeta_3 = np.random.random()
    alphas = np.array([alpha_1(k_checked), alpha_2(k_checked)])

    if alphas[0] < zeta_1 * alphas.sum():
        #i=2
        eps_ = sample_f_2()
        if zeta_3 < g_2(eps_, k_checked):
            return eps_*k_checked
        else:
            return sample_secondary_energy(E_0_checked)
    else:
        #i=1
        eps_ = sample_f_1()
        if zeta_3 < g_1(eps_, k_checked):
            return eps_*k_checked
        else:
            return sample_secondary_energy(k_checked)
