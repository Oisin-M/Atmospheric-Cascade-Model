import numpy as np
import constants as const

def Delta_E(eps, E_0_checked):

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
        delta_prime_ = delta_prime(eps, E_0_checked)
        return A(delta_prime_, E_0_checked)
    else:
        return 0

def alpha_2():

    return 0.5

def f_2(eps):

    return 2*eps

def g_2(eps, E_0_checked):

    if (eps*E_0_checked>const.AP and eps*E_0_checked<E_0_checked-const.m):
        delta_prime_ = delta_prime(eps, E_0_checked)
        return B(delta_prime_, E_0_checked)
    else:
        return 0

def get_Nbrem(E_0_checked):

    eqn_soln = -1*np.log(const.AP/E_0_checked)/np.log(2)

    return int(np.floor(eqn_soln))

def alpha_1j():

    return 1

def f_1j(j, eps):

    if eps<=2**(-j):
        return 1/np.log(2) * 2**(j-1)
    elif eps>=2**(-j+1):
        return 0
    else:
        return 1/np.log(2) * (1-eps*2**(j-1))/eps

def g_1j(eps):

    return 1

def sample_j(Nbrem):

    zeta = np.random.random()
    return int(np.floor(Nbrem*zeta)+1)

def p(j):

    return 2**(1-j)

def eps_prime(eps, p):

    return eps/p

def g_eps_prime(eps_prime):

    if eps_prime<=1/2:
        return 1/np.log(2)
    else:
        return 1/np.log(2) * (1-eps_prime)/eps_prime

def alpha_1_prime():

    return 1/(2*np.log(2))

def f_1_prime(eps_prime):

    if eps_prime<=1/2:
        return 2
    else:
        return 0

def g_1_prime(eps_prime):

    return 1

def alpha_2_prime():

    return 1-1/(2*np.log(2))

def f_2_prime(eps_prime):

    if eps_prime<=1/2:
        return 0
    else:
        1/(np.log(2)-0.5) * (1-eps_prime)/eps_prime

def g_2_prime(eps_prime):

    return 1

def eps_prime(x):

    return 1-0.5*x

def alpha_prime_prime():

    return 1/(4*np.log(2)-2)

def f_prime_prime(x):

    return 2*x

def g_prime_prime(x):

    return 1/(2-x)

def sample_f_prime_prime():

    zeta_1=np.random.random()
    zeta_2=np.random.random()
    return np.max([zeta_1, zeta_2])

def sample_f_1_prime():

    return np.random.random()/2

def sample_f_2():

    zeta_1=np.random.random()
    zeta_2=np.random.random()
    return np.max([zeta_1, zeta_2])

def sample_f_2_prime():

    x = sample_f_prime_prime()

    zeta_3 = np.random.random()
    if zeta_3<g_prime_prime(x):
        return eps_prime(x)
    else:
        return sample_f_2_prime()

def sample_f_1_j(j):

    zeta_1 = np.random.random()
    zeta_3 = np.random.random()
    p_ = p(j)
    alphas = np.array([alpha_1_prime(), alpha_2_prime()])

    if alphas[0] < zeta_1 * alphas.sum():
        #i=2
        eps_prime = sample_f_2_prime()
        if zeta_3 < g_2_prime(eps_prime):
            return eps_prime*p_
        else:
            return sample_f_1_j(j)
    else:
        #i=1
        eps_prime = sample_f_1_prime()
        if zeta_3 < g_1_prime(eps_prime):
            return eps_prime*p_
        else:
            return sample_f_1_j(j)

def sample_f_1(E_0_checked):

    zeta_1 = np.random.random()
    zeta_3 = np.random.random()

    Nbrem = get_Nbrem(E_0_checked)
    j_max = sample_j(Nbrem)
    js = np.array(list(range(1, j_max+1)))
    alphas = alpha_1j()*np.ones(j_max)
    continue_bool = True
    for j in js:
        if continue_bool:
            if alphas[0:j-1].sum() < zeta_1 * alphas.sum():
                continue_bool = False

                eps = sample_f_1_j(j)
                if zeta_3 < g_1j(eps):
                    return eps
                else:
                    return sample_f_1(E_0_checked)

def sample_secondary_energy(E_0_checked):
    
    zeta_1 = np.random.random()
    zeta_3 = np.random.random()
    alphas = np.array([alpha_1(E_0_checked), alpha_2()])

    if alphas[0] < zeta_1 * alphas.sum():
        #i=2
        eps_ = sample_f_2()
        if zeta_3 < g_2(eps_, E_0_checked):
            return eps_*E_0_checked
        else:
            return sample_secondary_energy(E_0_checked)
    else:
        #i=1
        eps_ = sample_f_1(E_0_checked)
        if zeta_3 < g_1(eps_, E_0_checked):
            return eps_*E_0_checked
        else:
            return sample_secondary_energy(E_0_checked)
